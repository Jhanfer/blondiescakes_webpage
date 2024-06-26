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
        error=[rx.redirect("/"),rx.toast.error("Error 4")]
        token=self.token_stored
        await self.get_cookie()
        cookie=self.sesion_cookie

        """print(self.user_id,self.page_id)"""
        if self.generated_uid == self.user_id and self.generated_pid == self.page_id:
            if not cookie == None:
                if not token == {}:
                    if self.show==False:
                        CookieState.show_page(True)
                        show= await self.get_state(CookieState)
                        self.show=show.show
                    
                    try:
                        payload=jwt.decode(token["access_token"],algorithms=c.AL,key=c.SEED)
                        self.username=payload.get("sub")
                    except ExpiredSignatureError:
                        return [rx.toast.error("Error 4")]
                else:
                    return [rx.toast.error("Error 3")]

                """user=mongo_client.test.users.find_one({"username":username})
                exp=payload.get("exp")"""
            else:
                return [rx.toast.error("Error 2")]
        else:
            return [rx.toast.error("Error 1")]

    def get_data(self,token:dict,pid:str,uid:str):
        self.token_stored=token
        self.generated_uid=uid
        self.generated_pid=pid
        return [rx.redirect(f"/database_updater/{uid}/{pid}"),CookieState.update_current_url(f"/database_updater/{uid}/{pid}")]

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
                        rx.hstack(
                                rx.heading(f"Bienvenid@ de vuelta, {VerifyID.username}!",color="black"),
                                rx.link(rx.button("Cerrar sesión",on_click=CookieState.logout),href="/backend_login",is_external=False)
                            ),
                        rx.hstack(
                                rx.flex(
                                        updater("crear artículo"),
                                        rx.spacer(),
                                        rx.button("eliminar artículo",
                                                    background_color="#ec1c1c",
                                                    color="#000000",
                                                    disabled=BackendUpdater.checked,
                                                    on_click=lambda:[BackendUpdater.delete_database_items,BackendUpdater.refresh_page],
                                                    padding_left="1em"
                                                ),
                                    display=["none", "none", "flex", "flex", "flex"],
                                    justify="between",
                                    spacing="6",
                                    wrap="wrap"
                                ),
                                rx.flex(
                                        updater("nuevo"),
                                        rx.spacer(),
                                        rx.button("eliminar",
                                                    background_color="#ec1c1c",
                                                    color="#000000",
                                                    disabled=BackendUpdater.checked,
                                                    on_click=lambda:[BackendUpdater.delete_database_items,BackendUpdater.refresh_page],
                                                    padding_left="1em"
                                                ),
                                    display=["flex", "flex", "none", "none", "none"],
                                    justify="between",
                                    spacing="6",
                                    wrap="wrap"
                                ),
                            width="100%",
                            bg="grey",
                            height="5em",
                            align="center",
                            justify="center",
                            padding_left="3em",
                            padding_right="3em"
                        ),

                        rx.vstack(
                                rx.text("ITEMS DE LA TIENDA"),
                                backend_items(),
                            align="center",
                            justify="center",
                            width="100%"
                        ),

                    align="center",
                    justify="center",
                    padding_top="3em",
                    width="100%"
                ),
                    
                rx.flex()),
            rx.flex(),

        align="center",
        width="100%")




