import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_state.cookies import CookieState
import uuid 
import time

class Refresh(rx.State):
    id:str
    stored_id:str

    async def redirect_system(self):
        """This system gets an id and refresh the pages with a random URLS"""
        if not self.id:
            id=str(uuid.uuid4())
            time.sleep(2)
            self.stored_id=id
            return rx.redirect(f"/redirect/{id}")
        
        if self.id == self.stored_id:
            url = await self.get_state(CookieState)
            print(url.current_url)
            return rx.redirect(url.current_url)
        
    async  def on_load(self):
        """Verifies the id from the pages and the stored id"""
        if self.stored_id == self.id:
            url = await self.get_state(CookieState)
            """print(url.current_url)"""
            return rx.redirect(url.current_url)
        else:
            return rx.toast.error("Self.stored id no disponible")

@rx.page(
    route="/redirect/[id]",
    title="redirecting...",
    on_load=Refresh.on_load
)

def redirect():
    return rx.center(rx.text("Redireccionando... Por favor espere."))