import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import update_windows


#Idex Windows 
class IndexWindowsUpdater(rx.State):
    windows_title:str
    windows_description:str
    windows_image_url:str
    windows_text:str
    windows_id:str
    windows_data:list
    windows_all_data:str

    windows_id_1_cond:bool = False


    @property
    def all_windows_present(self):
        """Check that no data is None"""
        if self.windows_id_1_cond == False:
            return bool(self.windows_image_url and self.windows_text)
        else:
            return bool(self.windows_title and self.windows_description and self.windows_image_url and self.windows_text)

    def get_custom_values(self,id:str):
        """Return the id of selected element"""
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
        """Gets all data"""
        self.windows_data = data

    def set_title(self,title:str):
        """Set title function"""
        self.windows_title = title

    def set_text(self, text:str):
        """Set text function"""
        self.windows_text = text

    def set_description(self,description:str):
        """Set description function"""
        self.windows_description = description

    def set_image_url(self,image_url:str):
        """Set image_url function"""
        self.windows_image_url = image_url

    def set_all(self,title:str,image_url:str,description:str,text:str):
        """Set all values"""
        self.windows_id_1_cond = False
        self.windows_text = text
        self.windows_image_url = image_url
        self.windows_description = description
        self.windows_title = title

    def reset_data(self):
        """Reset all values to None"""
        self.windows_id_1_cond = False
        self.windows_text = None
        self.windows_title = None
        self.windows_description = None
        self.windows_image_url = None

    def update_data(self):
        if self.all_windows_present and self.windows_id_1_cond == True:
            update_windows(self.windows_id, self.windows_title, self.windows_description, self.windows_image_url, self.windows_text)
            return rx.call_script("window.location.reload()")
        elif self.all_windows_present and self.windows_id_1_cond == False:
            update_windows(self.windows_id, "none", "none", self.windows_image_url, self.windows_text)
            return rx.call_script("window.location.reload()")
        else:
            return rx.toast.error("Falta un segmento")


