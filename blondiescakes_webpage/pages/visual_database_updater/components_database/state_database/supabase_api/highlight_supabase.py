import os
from supabase import create_client, Client
import dotenv
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.classes_base import Highlights



class HighlightSupabase():
    """Supabase API for highlight component"""
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase:Client

    @property
    def act_data(self):
        """Update data and load envs"""
        dotenv.load_dotenv()
        if self.url and self.key:
            self.supabase: Client = create_client(self.url, self.key)

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