#cosas a crear
"""
1 sistema que me permita ver las fotos que están subidas
2 sistema de autenticación de usuario
3 crear id, subir url de imagen, subir titulo, fecha de subida
4 eliominacion de imagenes
5 subida de imagenes
"""
import time
import datetime
import reflex as rx
import os
from supabase import create_client, Client
import dotenv

class SupabaseAPI():

    dotenv.load_dotenv()
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase:Client

    def act_data(self):
        dotenv.load_dotenv()
        if self.url and self.key:
            self.supabase: Client = create_client(self.url, self.key)
        else:
            pass


    def get_data(self):
        
        self.act_data()
        response = self.supabase.table('Images_database').select("*").execute()

        datos=[]
    
        if len(response.data) > 0:
            for featured_item in response.data: #itera
                datos.append( 
                    Featured( #se utiliza Featured ya que permite extraer los datos e iterar sobre ellos
                        id=featured_item["id"],
                        image_url=featured_item["image_url"],
                        url_purchase=featured_item["url_purchase"],
                        title=featured_item["title"],
                        upload_time=featured_item["upload_time"],
                    )
                )
        else:
            pass

        return datos
    

    def insert_data(self,id:str,image_url:str,url_purchase:str,title:str):
        
        self.act_data()

        timestamp=time.time()
        times=time.localtime(timestamp)
        format=f"{datetime.date.today()} {times.tm_hour}:{times.tm_min}:{times.tm_sec}"
        
        data, count = self.supabase.table("Images_database").insert({"id":id, "image_url":image_url,"url_purchase":url_purchase,"title":title,"upload_time":f"{format}"}).execute()
        
        print(data,count)
        return True




class Featured(rx.Base):
    id:str
    image_url:str
    url_purchase:str
    title:str
    upload_time:str
