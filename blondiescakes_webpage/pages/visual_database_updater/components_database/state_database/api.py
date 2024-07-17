from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_database import SupabaseAPI,Featured

supabase_api=SupabaseAPI()


async def get_all_data_database() -> Featured:
    return supabase_api.get_all_data()

async def get_data_alter_api(categorie:str) -> Featured:
    return supabase_api.get_data_alter(categorie)

def upload_supabase(id:str,image_url:str,url_purchase:str,title:str,categorie:str):
    supabase_api.insert_data(id,image_url,url_purchase,title,categorie)

def delete_content(id_list:list):
    supabase_api.delete_data(id_list)