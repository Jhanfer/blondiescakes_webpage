import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import update_about_us, update_about_us_second_text

class AboutUsUpdater(rx.State):
    title:str
    sub_title:str
    image_url:str
    sumary:str
    second_title:str
    second_sumary:str

    @property
    def is_data_available(self):
        """Check that no data is None"""
        return bool(self.title and self.sub_title and self.image_url and self.sumary and self.second_title and self.second_sumary)

    def set_title(self,title:str):
        """Set title function"""
        self.title = title
    
    def set_second_title(self,title:str):
        """Set second title function"""
        self.second_title = title

    def set_sub_title(self,sub_title:str):
        """Set sub_title function"""
        self.sub_title = sub_title

    def set_sumary(self,sumary:str):
        """Set sumary function"""
        self.sumary = sumary

    def set_second_sumary(self,sumary:str):
        """Set second sumary function"""
        self.second_sumary = sumary

    def set_image(self,image:str):
        """Set image function"""
        self.image_url = image

    def update_data(self):
        """Update data function"""
        if self.is_data_available == True:
            update_about_us(self.title,self.sub_title,self.image_url,self.sumary)
            update_about_us_second_text(self.second_title,self.second_sumary)
            return [rx.toast.success("Subido correctamente"),rx.call_script("window.location.reload()")]
        else:
            return rx.toast.error("Falta algún campo")
        
    def set_none_data(self):
        """Set all data to none"""
        self.title = None
        self.sub_title = None
        self.sumary = None
        self.second_sumary = None
        self.second_title = None