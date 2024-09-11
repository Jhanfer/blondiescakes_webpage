from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.supabase_database import SupabaseAPI,Featured, Highlights, WinData, ReviewsBase, IndexSumary, AboutUs, Purposes


supabase_api = SupabaseAPI()


# Items #
async def get_all_data_database() -> Featured:
    return supabase_api.get_all_data()

async def get_data_alter_api(categorie:str) -> Featured:
    return supabase_api.get_data_alter(categorie)

def upload_supabase(id:str,image_url:str,item_description:str,title:str,categorie:str):
    supabase_api.insert_data(id,image_url,item_description,title,categorie)

def delete_content(id_list:list):
    supabase_api.delete_data(id_list)


#Pages components changer 

# Highlight #
async def get_highlight_data() -> Highlights:
    return supabase_api.get_highlight()

def update_highlight(title:str, description:str, image_url:str):
    supabase_api.highlight_updater(title, description, image_url)


# Windows #
async def get_windows_data() -> list[WinData]:
    return supabase_api.get_windows()

def update_windows(id:str, title:str, description:str, image_url:str, text:str):
    supabase_api.windows_updater(id,title,description,image_url,text)


# Reviews #
async def get_reviews_data_api() -> list[ReviewsBase]:
    return supabase_api.get_reviews_data()

def update_reviews(google_json):
    supabase_api.update_reviews_data(google_json)


# Sumary Texts #
async def get_sumary_data() -> list[IndexSumary]:
    return supabase_api.get_index_sumary_text()

def update_sumary_data(index_text_json:dict):
    supabase_api.update_sumary_data(index_text_json)


# About us #
async def get_about_us() -> list[AboutUs]:
    return supabase_api.about_us()


async def get_pros() -> list[Purposes]:
    return supabase_api.pros()


async def get_purposes() -> list[Purposes]:
    return supabase_api.vision_mision()

