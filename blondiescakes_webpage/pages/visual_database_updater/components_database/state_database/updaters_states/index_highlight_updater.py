import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import update_highlight


#Index Highlights
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
        """Set all data dfunction"""
        self.highlight_image_url = image_url
        self.highlight_description = description
        self.highlight_title = title

    def update_data(self):
        """Update data function"""
        if self.all_highlight_present:
            update_highlight(self.highlight_title, self.highlight_description, self.highlight_image_url)
            return rx.call_script("window.location.reload()")
        else:
            return rx.toast.error("Falta un segmento")

    def reset_data(self):
        self.highlight_title = None
        self.highlight_description = None
        self.highlight_image_url = None
