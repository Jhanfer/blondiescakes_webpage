import time
import datetime
import reflex as rx
import os
from supabase import create_client, Client
import dotenv
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.classes_base import AboutUs, Purposes



class AboutUsSupabase():
    """Supabase API for AboutUS"""
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase:Client

    @property
    def act_data(self):
        """Update data and load envs"""
        dotenv.load_dotenv()
        if self.url and self.key:
            self.supabase: Client = create_client(self.url, self.key)

    #About us getter# 
    def about_us(self):
        self.act_data
        response_1 = self.supabase.table("index_about_us_texts").select("*").eq("id", 2).execute()
        response_2 = self.supabase.table("index_about_us_texts").select("*").eq("id", 3).execute()
        if len(response_1.data) > 0 and len(response_2.data) > 0:
            data_1 = response_1.data[0]["texts"]["about_us"]
            data_2 = response_2.data[0]["texts"]["second_text"]
            about_us_data = [
                AboutUs(
                        title=data_1["title"],
                        sub_title=data_1["sub_title"],
                        sumary=data_1["sumary"],
                        image_url=data_1["image_url"]
                    ),
            ]
            second_text = [
                AboutUs(
                    title=data_2["title"],
                    sumary=data_2["sumary"]
                )
            ]
        return [about_us_data,second_text]
    
    #About us setter# 
    def update_about_us(self, data:dict):
        self.act_data
        response = self.supabase.table("index_about_us_texts").update({"texts":data}).eq("id", 2).execute()
        print(response)


    def pros(self):
        self.act_data
        response = self.supabase.table("index_about_us_texts").select("*").eq("id", 5).execute()
        if len(response.data) > 0:
            data = response.data[0]["texts"]["pros"]
            pros_list = []
            for items in data:
                pros_list.append(
                    Purposes(
                        title=data[items]["title"],
                        sumary=data[items]["sumary"]
                    )
                )
        return pros_list
    
    def vision_mision(self):
        self.act_data
        response = self.supabase.table("index_about_us_texts").select("*").eq("id", 6).execute()
        if len(response.data) > 0:
            data = response.data[0]["texts"]
            purposes_list = []
            for items in data:
                purposes_list.append(
                    Purposes(
                        title=data[items]["title"],
                        sumary=data[items]["sumary"],
                        type=data[items]["type"]
                    )
                )
        return purposes_list




data = {
    "about_us": {
        "title": "Detrás de los postres",
        "sumary": "Apesar de tener mas 8 años de experiencia en el sector, Blondies nace en un momento de aislamiento social con sus restricciones, la Pandemia del Covid 2019, tuve que enfrentar muchas dificultades por falta de trabajo, debido a que la empresa donde laboraba cerrò sus puertas, la falta de movilidad entre otros obstáculos, me vi en la necesidad de crear productos de pasteleria y reposterìa personalizados, ofreciendo una gran variedad de opciones y alternativas a mis clientes, creando asì una nueva demanda en la modalidad virtual, mirando hacia el futuro con la esperanza de crecer, de brindarle a nuestros clientes un buen servicio, adaptàndonos a nuevos escenarios que puedan surjir en el futuro.",
        "image_url": "https://i.ibb.co/tz9rLF1/badge-carousel2.jpg",
        "sub_title": "¡Hola! ¡Soy la chef y pastelera de Blondie’s Cake, Joselyn!"
    }
}



{
    "second_text": {
        "title": "¿Qué mejor manera de celebrar un momento importante que con un pastel delicioso elaborado con maestría y cuidado?",
        "sumary": "En Blondies, nos adaptamos a los nuevos tiempos, ofreciendo nuestros servicios de manera virtual, pero siempre con la misma calidad y atención personalizada. Nuestro objetivo es crecer junto a ti, brindándote el mejor servicio y los pasteles más deliciosos para tus momentos especiales."
    }
}







"""def about_us(self):
        self.act_data
        response = self.supabase.table("index_about_us_texts").select("*").eq("id", 2).execute()
        data = response.data[0]["texts"]["about_us"]
        data_second_text = response.data[0]["texts"]["second_text"]
        if len(response.data) > 0:
            about_us_data = [
                AboutUs(
                        title=data["title"],
                        sub_title=data["sub_title"],
                        sumary=data["sumary"],
                        image_url=data["image_url"]
                    ),
            ]
            second_text = [
                AboutUs(
                    title=data_second_text["title"],
                    sumary=data_second_text["sumary"],
                    sub_title="",
                    image_url=""
                )
            ]
        return [about_us_data,second_text]"""