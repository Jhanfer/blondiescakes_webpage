import reflex as rx
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.page_state import PageState
from blondiescakes_webpage.components.body_products_items.items import backend_items
from blondiescakes_webpage.pages.visual_database_updater.components_database.updater_component import updater
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.Updater import BackendUpdater
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_state.PyMongoAPI import mongo_client
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_state.cookies import CookieState
from blondiescakes_webpage.styles import constants as c

from jose import jwt
from jose import ExpiredSignatureError
import time

class VerifyID(rx.State):
    user_id:str
    page_id:str
    generated_uid:str
    generated_pid:str
    token_stored:dict

    sesion_cookie:dict
    
    show:bool=False
    
    username:str
    



    async def verify_token(self):
        
        token=self.token_stored
        await self.get_cookie()
        cookie=self.sesion_cookie

        
        if self.generated_uid == self.user_id and self.generated_pid == self.page_id:
            if not cookie == None:
                #print(cookie.get("access_token"))
                if not token == {}:

                    if self.show==False:
                        CookieState.show_page(True)
                        show= await self.get_state(CookieState)
                        self.show=show.show
                        

                    try:
                        payload=jwt.decode(token["access_token"],algorithms=c.AL,key=c.SEED)
                        self.username=payload.get("sub")
                    except ExpiredSignatureError:
                        return [rx.redirect("/"),rx.toast.error("Error!!!!!")]
                else:
                    return [rx.redirect("/"),rx.toast.error("Error!!!!!")]

                """user=mongo_client.test.users.find_one({"username":username})
                exp=payload.get("exp")"""
            else:
                return [rx.redirect("/"),rx.toast.error("Error!!!!!")]
        else:
            return [rx.redirect("/"),rx.toast.error("Error!!!!!")]




    def get_data(self,token:dict,pid:str,uid:str):
        self.token_stored=token
        self.generated_uid=uid
        self.generated_pid=pid
        return rx.redirect(f"/database_updater/{uid}/{pid}")

    async def get_cookie(self):
        cookie= await self.get_state(CookieState)
        self.sesion_cookie=cookie.sesion_token



@rx.page(
    route="/database_updater/[user_id]/[page_id]",
    title="Database",
    on_load=[PageState.get_database_data,VerifyID.verify_token]
)


def image_updater_page() -> rx.Component:
    return rx.vstack(
        
            rx.cond(VerifyID.show,
                    
                rx.vstack(
                    rx.heading(f"Bienvenid@ de vuelta, {VerifyID.username}!"),
                    rx.hstack(
                        
                            updater(),

                            rx.button("eliminar artículo",background_color="#ec1c1c",color="#000000",disabled=BackendUpdater.checked,on_click=lambda:[BackendUpdater.delete_database_items,BackendUpdater.refresh_page]),

                        width="90%",
                        bg="grey",
                        height="5em",
                        align="center",
                        justify="between",
                        padding_left="3em",
                        padding_right="3em"),

                    rx.text("ITEMS DE LA TIENDA"),
                    backend_items(),

                    align="center",
                    justify="center",
                    padding_top="3em"),
                    
                rx.flex()),
            rx.flex(),

        align="center")




