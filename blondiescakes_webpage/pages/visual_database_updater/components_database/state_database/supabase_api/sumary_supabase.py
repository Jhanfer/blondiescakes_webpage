import time
import datetime
import reflex as rx
import os
from supabase import create_client, Client
import dotenv
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.classes_base import IndexSumary


class SumarySupabase():
    """Supabase API for sumary index texts"""
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase:Client

    @property
    def act_data(self):
        """Update data and load envs"""
        dotenv.load_dotenv()
        if self.url and self.key:
            self.supabase: Client = create_client(self.url, self.key)

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
