import time
import datetime
import reflex as rx
import os
from supabase import create_client, Client
import dotenv
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.classes_base import Featured,IndexSumary,WinData,Highlights,ReviewsBase,AboutUs,Purposes

class SupabaseAPI():
    """Api from SUPABASE Database"""
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase:Client

    @property
    def act_data(self):
        """Update data and load envs"""
        dotenv.load_dotenv()
        if self.url and self.key:
            self.supabase: Client = create_client(self.url, self.key)

    def get_all_data(self):
        """Gets all data"""
        self.act_data
        response = self.supabase.table("Images_database").select("*").execute()
        datos = []
        if len(response.data) > 0:
            for featured_item in response.data:
                datos.append(
                    Featured(
                        id=featured_item["id"],
                        image_url=featured_item["image_url"],
                        item_description=featured_item["item_description"],
                        title=featured_item["title"],
                        upload_time=featured_item["upload_time"],
                        categorie=featured_item["categorie"],
                        price=featured_item["price"]
                    )
                )
        return datos

    def get_data_alter(self,categorie:str):
        """Get data based on the type data required"""
        self.act_data
        response = self.supabase.table("Images_database").select("*").execute()
        datos = []
        if len(response.data) > 0:
            for featured_item in response.data:
                datos.append(
                    Featured(
                        id=featured_item["id"],
                        image_url=featured_item["image_url"],
                        item_description=featured_item["item_description"],
                        title=featured_item["title"],
                        upload_time=featured_item["upload_time"],
                        categorie=featured_item["categorie"],
                        price=featured_item["price"]
                    )
                )
            buttercream = []
            frias = []
            saludables = []
            tradicionales = []
            database = []
            # Iteramos sobre la lista de Featured y los asignamos a la categoría correspondiente
            categorias = {
                "class_buttercream": buttercream,
                "class_frias": frias,
                "class_saludables": saludables,
                "class_tradicionales": tradicionales,
                "class_database": database
            }
            for item in datos:
                if item.categorie in categorias:
                    categorias[item.categorie].append(item)
                else:
                    print(f"Categoría no reconocida: {item.categorie}")

            # añadir más elif para otras categorías si es necesario
            categories_json = {
                "buttercream":buttercream,
                "frias":frias,
                "saludables":saludables,
                "tradicionales":tradicionales,
                "database":database
            }
            
            if categorie in categories_json:
                return categories_json[categorie]
        else:
            pass

    def insert_data(self,id:str,image_url:str,item_description:str,title:str,categorie:str, price:int):
        """Insert data on database
        purchase_url has been changed to "Description" prompt
        """
        self.act_data
        category_to_table = {
            "Pagina principal": "Images_database",
            "Buttercream": "class_buttercream",
            "Frios": "class_frias",
            "Saludables": "class_saludables",
            "Tradicionales": "class_tradicionales"
        }

        # Obtener el nombre de la tabla
        categoria_backend = category_to_table.get(categorie, "default_table")
        timestamp=time.time()
        times=time.localtime(timestamp)
        format=f"{datetime.date.today()} {times.tm_hour}:{times.tm_min}:{times.tm_sec}"
        
        if not categoria_backend == "default_table":
            if image_url and item_description and title != None:
                self.supabase.table("Images_database").insert({"id":id, "image_url":image_url,"item_description":item_description,"title":title,"upload_time":f"{format}","categorie":categoria_backend,"price":price}).execute()
                print("Subido con éxito")
                
            else:
                print("No se pudo subir")

    def delete_data(self,id:list):
        """Deletes Data"""
        self.act_data
        if id and isinstance(id, list):
            deleted = False
            for i in id:
                try:
                    id_int = int(i)
                    self.supabase.table("Images_database").delete().eq("id", id_int).execute()
                    print(f"Eliminado con éxito: id {id_int}")
                    deleted = True
                except Exception as e:
                    print(f"Error al eliminar id {i}: {str(e)}")
            
            if not deleted:
                print("No se eliminó ningún elemento")
        else:
            print("No eliminado: ID no válido")       

    def get_google_json_credential(self):
        """Gets Google API Credential for works"""
        self.act_data
        response = self.supabase.table("Google analytics API Credentials").select("*").execute()
        datos = {}
        if len(response.data) > 0:
            for item in response.data:
                datos.update(item)
        datos = datos.get("json-credentials")
        return datos
