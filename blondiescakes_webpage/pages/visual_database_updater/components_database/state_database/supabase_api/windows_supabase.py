import os
from supabase import create_client, Client
import dotenv
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.classes_base import WinData


class WindowsSupabase():
    """Supbasase API for Index Windows"""
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase:Client

    @property
    def act_data(self):
        """Update data and load envs"""
        dotenv.load_dotenv()
        if self.url and self.key:
            self.supabase: Client = create_client(self.url, self.key)

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