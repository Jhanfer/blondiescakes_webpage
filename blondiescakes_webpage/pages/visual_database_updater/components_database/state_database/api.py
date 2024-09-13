from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.supabase_database import SupabaseAPI,Featured, Highlights, WinData, ReviewsBase, IndexSumary, AboutUs, Purposes
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.about_us_supabase import AboutUsSupabase
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.sumary_supabase import SumarySupabase
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.goolge_reviews_supabase import GoogleReviewsSupabase
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.windows_supabase import WindowsSupabase
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.highlight_supabase import HighlightSupabase

supabase_api = SupabaseAPI()
about_us = AboutUsSupabase()
sumary = SumarySupabase()
google_reviews = GoogleReviewsSupabase()
windows = WindowsSupabase()
highlight = HighlightSupabase()

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
    return highlight.get_highlight()

def update_highlight(title:str, description:str, image_url:str):
    highlight.highlight_updater(title, description, image_url)


# Windows #
async def get_windows_data() -> list[WinData]:
    return windows.get_windows()

def update_windows(id:str, title:str, description:str, image_url:str, text:str):
    windows.windows_updater(id,title,description,image_url,text)


# Reviews #
async def get_reviews_data_api() -> list[ReviewsBase]:
    return google_reviews.get_reviews_data()

def update_reviews(google_json):
    google_reviews.update_reviews_data(google_json)


# Sumary Texts #
async def get_sumary_data() -> list[IndexSumary]:
    return sumary.get_index_sumary_text()

def update_sumary_data(index_text_json:dict):
    sumary.update_sumary_data(index_text_json)


# About us #
async def get_about_us() -> list[AboutUs]:
    return about_us.about_us()

def update_about_us():
    pass

async def get_pros() -> list[Purposes]:
    return about_us.pros()

async def get_purposes() -> list[Purposes]:
    return about_us.vision_mision()

