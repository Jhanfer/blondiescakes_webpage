import reflex as rx
import uuid

class Refresh(rx.State):
    id:str
    stored_id:str

    def redirect_system(self,id:str):
        """This system gets an id and refresh the pages with a random URLS"""
        self.stored_id=id
        if not self.id:
            return rx.redirect(f"/redirect/{id}")
        if self.id == self.stored_id:
            return rx.redirect("/database_updater/")
        
    def on_load(self):
        """Verifies the id from the pages and the stored id"""
        if self.stored_id == self.id:
            return rx.redirect("/database_updater/")
        else:
            return rx.redirect("/")

@rx.page(
    route="/redirect/[id]",
    title="redirecting...",
    on_load=Refresh.on_load
)

def redirect():
    return rx.center(rx.text("Redireccionando... Por favor espere."))