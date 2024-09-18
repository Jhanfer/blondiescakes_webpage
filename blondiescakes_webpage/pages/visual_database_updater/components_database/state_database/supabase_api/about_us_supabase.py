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

    # About us getter # 
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
    
    # About us setter # 
    def update_about_us(self,title:str,sub_title:str,image_url:str,sumary:str):
        self.act_data
        response = self.supabase.table("index_about_us_texts").update({"texts":{"about_us":{"title":title,"sumary":sumary,"sub_title":sub_title,"image_url":image_url} }}).eq("id", 2).execute()
        print(response)

    def update_about_us_second_text(self, title:str,sumary:str):
        self.act_data
        response = self.supabase.table("index_about_us_texts").update({"texts":{"second_text":{"title":title,"sumary":sumary}}}).eq("id", 3).execute()
        print(response)

    # Pros getter #
    def pros(self):
        self.act_data
        response = self.supabase.table("index_about_us_texts").select("*").eq("id", 4).execute()
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
    
    # Pros setter #
    def update_about_us_pros(self, title_1: str, sumary_1: str, title_2: str, sumary_2: str, title_3: str, sumary_3: str, title_4: str, sumary_4: str):
        self.act_data
        data = {
            "pros": {
                f"item_{i}": {
                    "title": title,
                    "sumary": sumary
                }
                for i, (title, sumary) in enumerate([
                    (title_1, sumary_1),
                    (title_2, sumary_2),
                    (title_3, sumary_3),
                    (title_4, sumary_4)
                ], start=1)
            }
        }
        response = self.supabase.table("index_about_us_texts").update({"texts":data}).eq("id", 4).execute()
        print(response)

    # Purposes getter #
    def vision_mision(self):
        self.act_data
        response = self.supabase.table("index_about_us_texts").select("*").eq("id", 5).execute()
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

    # Purposes setter #
    def mision_vision_updater(self, data:dict):
        self.act_data
        response = self.supabase.table("index_about_us_texts").update({"texts":data}).eq("id",5).execute()
        print(response)