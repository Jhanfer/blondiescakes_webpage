import reflex as rx
import uuid
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import upload_supabase,delete_content
import time

class BackendUpdater(rx.State):
    id:str
    image_url:str
    url_purchase:str
    title:str

    state:bool
    refresh:bool=False

    returns:dict
    

    selected_items:list
    items:list
    checked:bool=True
    #loading = show_progress:bool = True 

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
        self.id=None
        self.image_url=None
        self.url_purchase=None
        self.title=None

    def update_data(self):
        if self.id and self.url_purchase and self.title:
            upload_supabase(self.id,self.image_url,self.url_purchase,self.title)
            self.refresh=True
        else:
            self.refresh=False
        

    def refresh_page(self):
        if self.refresh == True:
            return rx.redirect("/database_updater/redirect")


    def refresh_state(self):
        self.state=True

    def refresh_state_refresh(self):
        self.state=False
    



    
    def select(self,featured_id:str,checked:bool):

        if checked == True:

            featured_id=[featured_id]
            self.selected_items=[]

            for i in featured_id:
                self.items.append(i)
        
            self.checked=False
            self.selected_items=self.items
            
        else:
            self.items.remove(featured_id)
            self.checked=True


    
    def delete_database_items(self):
        delete_content(self.selected_items)
        self.refresh=True
        self.checked=True



