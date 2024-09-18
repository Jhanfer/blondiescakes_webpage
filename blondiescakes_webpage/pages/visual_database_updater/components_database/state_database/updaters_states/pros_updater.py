import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import update_about_us_pros_function

class ProsUpdater(rx.State):
    item_1_title: str
    item_1_sumary: str

    item_2_title: str
    item_2_sumary: str

    item_3_title: str
    item_3_sumary: str

    item_4_title: str
    item_4_sumary: str

    @property
    def is_data_available(self):
        """Check that no data is None"""
        return bool(self.item_1_title and 
                    self.item_1_sumary and 
                    self.item_2_title and 
                    self.item_2_sumary and 
                    self.item_3_title and 
                    self.item_3_sumary and 
                    self.item_4_title and 
                    self.item_4_sumary
                )

    def set_title_1(self,title:str):
        """Set title function"""
        self.item_1_title = title

    def set_title_2(self,title:str):
        """Set title function"""
        self.item_2_title = title

    def set_title_3(self,title:str):
        """Set title function"""
        self.item_3_title = title

    def set_title_4(self,title:str):
        """Set title function"""
        self.item_4_title = title

    def set_sumary_1(self,sumary:str):
        """Set sumary function"""
        self.item_1_sumary = sumary

    def set_sumary_2(self,sumary:str):
        """Set sumary function"""
        self.item_2_sumary = sumary

    def set_sumary_3(self,sumary:str):
        """Set sumary function"""
        self.item_3_sumary = sumary

    def set_sumary_4(self,sumary:str):
        """Set sumary function"""
        self.item_4_sumary = sumary


    def update_data(self):
        """Update data function"""
        if self.is_data_available == True:
            update_about_us_pros_function(
                item_1_title=self.item_1_title, 
                item_1_sumary=self.item_1_sumary,

                item_2_title=self.item_2_title, 
                item_2_sumary=self.item_2_sumary,

                item_3_title=self.item_3_title,
                item_3_sumary=self.item_3_sumary, 

                item_4_title=self.item_4_title, 
                item_4_sumary=self.item_4_sumary
            )
            return [rx.toast.success("Subido correctamente"),rx.call_script("window.location.reload()")]
        else:
            return rx.toast.error("Falta algún campo")
        
    def set_none_data(self):
        """Set all data to none"""
        self.item_1_title = None
        self.item_1_sumary = None
        self.item_2_title = None
        self.item_2_sumary = None
        self.item_3_title = None
        self.item_3_sumary = None
        self.item_4_title = None
        self.item_4_sumary = None