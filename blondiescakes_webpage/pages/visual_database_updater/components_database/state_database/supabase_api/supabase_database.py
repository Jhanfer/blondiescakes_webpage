import time
import datetime
import reflex as rx
import os
from supabase import create_client, Client
import dotenv
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.classes_base import Featured,IndexSumary,WinData,Highlights,ReviewsBase,AboutUs,Purposes


#Supabase API
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

    def __act_data_test(self):
        self.act_data
        return self.supabase

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
                        categorie=featured_item["categorie"]
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
                        categorie=featured_item["categorie"]
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


    def insert_data(self,id:str,image_url:str,item_description:str,title:str,categorie:str):
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
                self.supabase.table("Images_database").insert({"id":id, "image_url":image_url,"item_description":item_description,"title":title,"upload_time":f"{format}","categorie":categoria_backend}).execute()
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


    ##Pages Updater##

    # Highlight updater #
    def get_highlight(self):
        self.act_data
        response = self.supabase.table("Destacado Página principal").select("*").eq("id", 1).execute()
        highlight = []
        if len(response.data) > 0:
            switch=True
            for featured_item in response.data:
                highlight.append(
                    Highlights(
                        title=featured_item["title"],
                        description=featured_item["description"],
                        image_url=featured_item["image_url"],
                        switch=switch
                    )
                )
        return highlight

    def highlight_updater(self, title:str, description:str, image_url:str):
        self.act_data
        response = self.supabase.table("Destacado Página principal").update({"title": title, "description":description, "image_url":image_url}).eq("id", 1).execute()


    # Windows updater #
    def get_windows(self):
        self.act_data
        response = self.supabase.table("windows_index_component").select("*").execute()
        windows_data = []
        windows_data_titles = []
        if len(response.data) > 0:
            switch = True
            for featured_items in response.data:
                if featured_items["id"] == 1:
                    windows_data_titles.append(
                        [featured_items["title"],
                        featured_items["description"]]
                    )
                    windows_data.append(
                        WinData(
                            id=featured_items["id"],
                            text=featured_items["text"],
                            image_url=f"url('{featured_items["image_url"]}')",
                            switch=switch
                        )
                    )
                else:
                    windows_data.append(
                        WinData(
                            id=featured_items["id"],
                            text=featured_items["text"],
                            image_url=f"url('{featured_items["image_url"]}')",
                            switch=switch
                        )
                    )
        return [windows_data_titles,windows_data]


    def windows_updater(self, id:str, title:str, description:str, image_url:str, text:str):
        self.act_data
        if not id == "1":
            response = self.supabase.table("windows_index_component").update({"title": title, "description":description, "image_url":image_url, "text":text}).eq("id", id).execute()
            print(response)
        else:
            response = self.supabase.table("windows_index_component").update({"title": title, "description":description, "image_url":image_url, "text":text}).eq("id", 1).execute()


    # Google Maps Reviews #
    def get_reviews_data(self):
        self.act_data
        response = self.supabase.table("google_review_data").select("*").execute()
        if len(response.data) > 0:
            dictionary = response.data
            reviews = dictionary[0]["data"]
            reviews_list = []
            for review in reviews:
                if "description" in review:
                    if len(review["description"]) > 190:
                        short = review["description"][:190] + "..."
                        reviews_list.append(
                            ReviewsBase(
                                username=review["username"],
                                rating=review["rating"],
                                description=short,
                                date=review["date"]
                            )
                        )
                    else:
                        reviews_list.append(
                            ReviewsBase(
                                username=review["username"],
                                rating=review["rating"],
                                description=review["description"],
                                date=review["date"]
                            )
                        )
                else:
                    pass
        return reviews_list

    def update_reviews_data(self,google_json):
        self.act_data
        response = self.supabase.table("google_review_data").update({"data":google_json}).eq("id", 1).execute()


    #Index sumary getter#
    def get_index_sumary_text(self):
        self.act_data
        response = self.supabase.table("index_about_us_texts").select("*").eq("id", 1).execute()
        paragraphs_list = []
        if len(response.data) > 0:
            for i in response.data[0]["texts"]:
                title = i
            for items in response.data[0]["texts"][title]:                
                paragraphs_list.append(
                    IndexSumary(
                        paragraph=response.data[0]["texts"][title][f"{items}"]
                    )
                )
        return [paragraphs_list,title]


    def update_sumary_data(self,index_text_json:dict):
        self.act_data
        response = self.supabase.table("index_about_us_texts").update({"texts":index_text_json}).eq("id", 1).execute()


    #About us getter# 
    def about_us(self):
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
        return [about_us_data,second_text]
    
    
    def pros(self):
        self.act_data
        response = self.supabase.table("index_about_us_texts").select("*").eq("id", 3).execute()
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
        response = self.supabase.table("index_about_us_texts").select("*").eq("id", 4).execute()
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
