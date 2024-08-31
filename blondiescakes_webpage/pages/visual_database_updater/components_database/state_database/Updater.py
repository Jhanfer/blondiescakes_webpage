import reflex as rx
import uuid
import time
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import upload_supabase,delete_content,update_highlight,update_windows
from blondiescakes_webpage.pages.redirect_pages.backend_reloader import Refresh
import time






class BackendUpdater(rx.State):
    """Backend image update API"""

    #Image data
    image_id:str
    image_url:str
    item_description:str
    categorie:str
    title:str

    #refresh states
    state:bool
    refresh:bool=False
    
    #Image manager
    selected_items:list
    items:list
    checked:bool=True
    #loading = show_progress:bool = True 



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
        if self.image_id and self.item_description and self.title and self.categorie:
            upload_supabase(self.image_id,self.image_url,self.item_description,self.title,self.categorie)
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




class IndexHighlightUpdater(rx.State):
    highlight_title:str
    highlight_description:str
    highlight_image_url:str

    @property
    def all_highlight_present(self):
        """Check that no data is None"""
        return bool(self.highlight_title and self.highlight_description and self.highlight_image_url)

    def set_title(self,title:str):
        """Set title function"""
        self.highlight_title = title

    def set_description(self,description:str):
        """Set description function"""
        self.highlight_description = description

    def set_image_url(self,image_url:str):
        """Set image_url function"""
        self.highlight_image_url = image_url

    def set_all(self,title:str,image_url:str,description:str):
        self.highlight_image_url = image_url
        self.highlight_description = description
        self.highlight_title = title

    def update_data(self):
        if self.all_highlight_present:
            update_highlight(self.highlight_title, self.highlight_description, self.highlight_image_url)
            return rx.call_script("window.location.reload()")
        else:
            return rx.toast.error("Falta un segmento")
        

    def reset_data(self):
        self.highlight_title = None
        self.highlight_description = None
        self.highlight_image_url = None


class IndexWindowsUpdater(rx.State):
    windows_title:str
    windows_description:str
    windows_image_url:str
    windows_text:str
    windows_id_1_cond:bool = False
    windows_id:str
    windows_data:list
    windows_all_data:str

    @property
    def all_windows_present(self):
        """Check that no data is None"""
        return bool(self.windows_title and self.windows_description and self.windows_image_url and self.windows_text)

    def get_custom_values(self,id:str):
                return self.windows_data[int(id) - 1]

    def set_categorie(self,categorie:str):
        """Set the categories (ID numbers) 
        and reveal the title updater component"""
        if categorie[8] == "1" and self.windows_data:
            self.windows_id_1_cond = True
            self.windows_id = categorie[8]
            self.windows_text = self.get_custom_values(self.windows_id)["text"]
            url_string = self.get_custom_values(self.windows_id)["image_url"]
            cleaned_url = url_string.strip("url(')..")
            self.windows_image_url = cleaned_url

        elif not self.windows_data:
            self.windows_id_1_cond = False
            print("No data yet")
            
        else:
            self.windows_id_1_cond = False
            self.windows_id = categorie[8]
            self.windows_text = self.get_custom_values(self.windows_id)["text"]
            url_string = self.get_custom_values(self.windows_id)["image_url"]
            cleaned_url = url_string.strip("url(')..")
            self.windows_image_url = cleaned_url

    def get_all_data(self,data:list):
        print(data)
        self.windows_data = data


    def set_title(self,title:str):
        """Set title function"""
        self.windows_title = title

    def set_text(self, text:str):
        self.windows_text = text

    def set_description(self,description:str):
        """Set description function"""
        self.windows_description = description

    def set_image_url(self,image_url:str):
        """Set image_url function"""
        self.windows_image_url = image_url

    def set_all(self,title:str,image_url:str,description:str):
        self.windows_image_url = image_url
        self.windows_description = description
        self.windows_title = title

    def reset_data(self):
        self.windows_title = None
        self.windows_description = None
        self.windows_image_url = None

    def update_data(self):
        if self.all_windows_present:
            update_windows(self.windows_id, self.windows_title, self.windows_description, self.windows_image_url, self.windows_text)
            return rx.call_script("window.location.reload()")
        else:
            return rx.toast.error("Falta un segmento")
        






