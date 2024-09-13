import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import update_highlight

class AboutUsUpdater(rx.State):
    title:str
    sub_title:str
    image_url:str
    sumary:str

    def set_image(self,image:str):
        self.image_url = image