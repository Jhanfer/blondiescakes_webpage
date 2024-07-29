from google.oauth2.service_account import Credentials
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Metric, Dimension, RunReportRequest
import pycountry
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_database import SupabaseAPI
import reflex as rx
import os


init = SupabaseAPI()

class GoogleAnalyticsAPI(rx.State):
    datos:list[dict]

    def get_country_name(self,country_code):
        try:
            return pycountry.countries.get(alpha_2=country_code).name
        except AttributeError:
            return country_code


    def get_analytics_data(self):
        property_id = os.environ.get("PROPERTY_ID")
        # Cargar credenciales desde el archivo JSON de la cuenta de servicio desde base de datos
        credentials = Credentials.from_service_account_info(
            init.get_google_json_credential(),
            scopes=['https://www.googleapis.com/auth/analytics.readonly']
        )

        # Crear el cliente
        client = BetaAnalyticsDataClient(credentials=credentials)

        # Configurar la solicitud
        request = RunReportRequest(
            property=f"properties/{property_id}",  # Reemplaza con tu ID de propiedad
            dimensions=[
                    Dimension(name="date"),
                    Dimension(name="country")
            ],
            metrics=[
                Metric(name="activeUsers"),
                Metric(name="sessions")
            ],
            date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
        )

        # Ejecutar el informe
        response = client.run_report(request)

        # Procesar y devolver los resultados
        results = []
        for row in response.rows:
            country_code = row.dimension_values[1].value
            country_name = self.get_country_name(country_code)
            results.append({
                "date": row.dimension_values[0].value,
                "country_code": country_code,
                "country_name": country_name,
                "active_users": row.metric_values[0].value,
                "sessions": row.metric_values[1].value
            })

        data = results
        # Calcular totales
        total_users = sum(int(item['active_users']) for item in data)
        total_sessions = sum(int(item['sessions']) for item in data)

        # Obtener países únicos y contar usuarios por país
        countries = {}
        for item in data:
            country_name = item['country_name']
            if country_name not in countries:
                countries[country_name] = {'users': 0, 'sessions': 0}
            countries[country_name]['users'] += int(item['active_users'])
            countries[country_name]['sessions'] += int(item['sessions'])

        #print(countries)
        #self.datos = countries.get("Spain")
        #print(self.datos)
        #print(f"\ nTotal de usuarios activos: {total_users}")
        #print(f"Total de sesiones: {total_sessions}")
        
        datos = []

        for country, stats in sorted(countries.items(), key=lambda x: x[1]['users'], reverse=True):
            datos.append({"country":country,"users":stats["users"],"sessions":stats["sessions"]})
        
        self.datos = datos
        #print(datos)
        #f"{country}: {stats['users']} usuarios, {stats['sessions']} sesiones"




data_example = [
    {"name": "Page A", "uv": 4000, "pv": 2400, "amt": 2400},
    {"name": "Page B", "uv": 3000, "pv": 1398, "amt": 2210},
    {"name": "Page C", "uv": 2000, "pv": 9800, "amt": 2290},
    {"name": "Page D", "uv": 2780, "pv": 3908, "amt": 2000},
    {"name": "Page E", "uv": 1890, "pv": 4800, "amt": 2181},
    {"name": "Page F", "uv": 2390, "pv": 3800, "amt": 2500},
    {"name": "Page G", "uv": 3490, "pv": 4300, "amt": 2100},
]



