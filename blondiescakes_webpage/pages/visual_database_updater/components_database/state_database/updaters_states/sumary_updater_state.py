import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import update_sumary_data



class IndexSumaryUpdater(rx.State):
    """Index Sumary class method,
    change title,
    change sumary
    """
    title:str
    texts_list:list
    texts:str

    @property
    def all_data_present(self):
        """Check that no data is None"""
        return bool(self.title and self.texts)
    
    def set_title(self,title:str):
        """Sets title"""
        self.title = title

    def set_texts(self,texts:str):
        """Sets texts"""
        self.texts = texts

    def upload_sumary_data(self):
        """Update database data"""
        if self.all_data_present == True:
            update_sumary_data({self.title:{"1":self.texts}})
            return [rx.toast("Subido con éxito"),rx.call_script("window.location.reload()")]
        else:
            return rx.toast.error("falta algún campo")