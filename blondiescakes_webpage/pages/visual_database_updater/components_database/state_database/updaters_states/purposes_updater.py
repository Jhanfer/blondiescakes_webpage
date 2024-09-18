import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import update_purpose_data

class PurposesUpdater(rx.State):
    vision_title: str
    vision_sumary: str
    mision_title: str
    mision_sumary: str

    @property
    def is_data_available(self):
        """Check that no data is None"""
        return bool(self.vision_title and self.vision_sumary and self.mision_title and self.mision_sumary)

    def set_vision_title(self,title:str):
        """Set vision title function"""
        self.vision_title = title

    def set_vision_sumary(self,sumary:str):
        """Set vision sumary function"""
        self.vision_sumary = sumary

    def set_mision_title(self,title:str):
        """Set mision title function"""
        self.mision_title = title

    def set_mision_sumary(self,sumary:str):
        """Set mision sumary function"""
        self.mision_sumary = sumary

    def update_data(self):
        """Update data function"""
        if self.is_data_available == True:
            data = {
                "mision":{
                    "type":"mision",
                    "title":self.mision_title,
                    "sumary":self.mision_sumary
                },
                "vision":{
                    "type":"vision",
                    "title":self.vision_title,
                    "sumary":self.vision_sumary
                }
            }
            update_purpose_data(data)
            return [rx.toast.success("Subido correctamente"),rx.call_script("window.location.reload()")]
        else:
            
            print(self.vision_sumary)
            
            print(self.mision_sumary)
            return rx.toast.error("Falta algún campo")
        
    def set_none_data(self):
        """Set all data to none"""
        self.vision_title = None
        self.vision_sumary = None
        self.mision_title = None
        self.mision_sumary = None