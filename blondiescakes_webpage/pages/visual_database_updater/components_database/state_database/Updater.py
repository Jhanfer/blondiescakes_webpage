import reflex as rx
import uuid
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import upload_supabase

class BackendUpdater(rx.State):
    id:str
    image_url:str
    url_purchase:str
    title:str


    def set_id(self,):

        _uuid=uuid.uuid4()
        _id=_uuid.bytes[0]
        _id=int(bin(_id)[2:], 2)
        self.id=_id


    def set_title(self,title:str):
        self.set_id()
        self.title=title


    def set_image_url(self,image_url:str):
        self.image_url=image_url


    def set_url_purchase(self,url_purchase:str):
        self.url_purchase=url_purchase


    def reset_data(self):
        self.id=str
        self.image_url=str
        self.url_purchase=str
        self.title=str



    def update_data(self):
        self.set_id()
        upload_supabase(self.id,self.image_url,self.url_purchase,self.title)

