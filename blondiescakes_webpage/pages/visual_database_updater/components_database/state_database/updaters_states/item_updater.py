import reflex as rx
import uuid
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import upload_supabase,delete_content
from blondiescakes_webpage.pages.redirect_pages.backend_reloader import Refresh


#Backend Images
class BackendUpdater(rx.State):
    """Backend image update API"""

    #Image data
    image_id:str
    image_url:str
    item_description:str
    categorie:str
    title:str
    price:int

    #refresh states
    state:bool
    refresh:bool=False
    
    #Image manager
    selected_items:list
    items:list
    checked:bool=True

    def set_id(self):
        """Set ID function"""
        _uuid=uuid.uuid4()
        _id=_uuid.bytes[0]
        _id=int(bin(_id)[2:], 2)
        self.image_id=_id

    def set_title(self,title:str):
        """Set title function"""
        self.set_id()
        self.title=title

    def set_image_url(self,image_url:str):
        """Set image url function"""
        self.image_url=image_url

    def set_price(self, price:int):
        """Set the article prices"""
        self.price = price

    def set_item_description(self,item_description:str):
        """Set url purchase function"""
        self.item_description=item_description

    def set_categorie(self,categorie:str):
        """Set categorie for upload"""
        self.categorie = categorie

    
    def reset_data(self):
        """this function reset the data"""
        self.image_id=None
        self.image_url=None
        self.item_description=None
        self.title=None

    def update_data(self):
        """Upload data function"""
        if self.image_id and self.item_description and self.title and self.categorie and self.price:
            upload_supabase(self.image_id,self.image_url,self.item_description,self.title,self.categorie, self.price)
            self.refresh=True
            if self.refresh==True:
                return rx.toast.success("Subido con éxito")
        else:
            self.refresh=False
            return rx.toast.error("no se ha podido subir")
    
    def refresh_page(self):
        """"Refresh page
        This is no longer used"""
        if self.refresh == True:
            return Refresh.redirect_system()
        

    def refresh_state_refresh(self):
        """Refresh states"""
        self.state=False
    

    def select(self,featured_id:str,checked:bool):
        """Selec function"""
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
        """This function deletes the data selected"""
        if self.selected_items:
            delete_content(self.selected_items)
            self.refresh=True
            self.checked=True
            return rx.toast.success("Eliminado con éxito")
        else:
            return rx.toast.error("Error: no eliminado")