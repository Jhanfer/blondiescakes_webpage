import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_database import SupabaseAPI,Featured

supabase_api=SupabaseAPI()

async def get_data()-> Featured:
    return supabase_api.get_data()

def upload_supabase(id:str,image_url:str,url_purchase:str,title:str):
    supabase_api.insert_data(id,image_url,url_purchase,title)