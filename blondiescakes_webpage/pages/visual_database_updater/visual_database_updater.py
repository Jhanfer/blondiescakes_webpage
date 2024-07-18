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
        CookieState.show_page(False)
        self.show = False
        token=self.token_stored
        await self.get_cookie()
        cookie=self.sesion_cookie
        

        if self.generated_uid != self.user_id or self.generated_pid != self.page_id:
            return [rx.toast.error("Error 1: ID de usuario o página no coinciden"),rx.redirect("/")]
        else:
            CookieState.show_page(True)
            show = await self.get_state(CookieState)
            self.show = show.show

        if cookie is None:
            return [rx.toast.error("Error 2: Cookie no encontrada")]

        if not token:
            return [rx.toast.error("Error 3: Token no válido")]

    
        try:
            payload = jwt.decode(token["access_token"], key=c.SEED, algorithms=[c.AL])
            self.username = payload.get("sub")
            return []  # Autenticación exitosa
        except ExpiredSignatureError:
            return [rx.toast.error("Error 4: Token expirado")]


    def logout(self):
        self.show = False


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
    on_load=[VerifyID.verify_token]
)


def image_updater_page() -> rx.Component:
    return rx.vstack(
        
            rx.cond(VerifyID.show,
                    
                rx.vstack(
                        rx.hstack(
                                rx.heading(f"Bienvenid@ de vuelta, {VerifyID.username}!",color="black"),
                                rx.link(rx.button("Cerrar sesión",on_click=[CookieState.logout,VerifyID.logout]),href="/backend_login",is_external=False)
                            ),
                        rx.hstack(
                                
                                #Desktop
                                rx.flex(
                                        updater("crear"),
                                        rx.spacer(),
                                        rx.button("eliminar",
                                                    background_color="#ec1c1c",
                                                    color="#000000",
                                                    disabled=BackendUpdater.checked,
                                                    on_click=lambda:[BackendUpdater.delete_database_items,BackendUpdater.refresh_page],
                                                    padding_left="1em"
                                                ),
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

                                rx.tabs.root(
                                    rx.tabs.list(
                                        rx.tabs.trigger("General", value="tab1"),
                                        rx.tabs.trigger("Buttercream", value="tab2"),
                                        rx.tabs.trigger("Frias", value="tab3"),
                                        rx.tabs.trigger("Tradicionales", value="tab4"),
                                        rx.tabs.trigger("Saludables", value="tab5"),
                                        style={"justify-content":"center"},
                                        size="1"
                                    ),
                                    rx.tabs.content(
                                        rx.box(
                                            backend_items("Pagina principal",PageState.general_database_data),
                                            on_mount=PageState.get_database_data,
                                            style={"justify-content":"center"}
                                        ),
                                        value="tab1",
                                        style={"justify-content":"center"}
                                    ),
                                    rx.tabs.content(
                                        rx.box(
                                            backend_items("Buttercream",PageState.class_buttercream),
                                            on_mount=PageState.get_database_data_alter("buttercream"),
                                            style={"justify-content":"center"}
                                        ),
                                        value="tab2",
                                    ),

                                    rx.tabs.content(
                                        rx.box(
                                            backend_items("Frias",PageState.class_frias),
                                            on_mount=PageState.get_database_data_alter("frias"),
                                            style={"justify-content":"center"}
                                        ),
                                        value="tab3",
                                    ),

                                    rx.tabs.content(
                                        rx.box(
                                            backend_items("Tradicionales",PageState.class_tradicionales),
                                            on_mount=PageState.get_database_data_alter("tradicionales"),
                                            style={"justify-content":"center"}
                                        ),
                                        value="tab4",
                                    ),

                                    rx.tabs.content(
                                        rx.box(
                                            backend_items("Saludables",PageState.class_saludables),
                                            on_mount=PageState.get_database_data_alter("saludables"),
                                            style={"justify-content":"center"}
                                        ),
                                        value="tab5",
                                    ),
                                    style={"justify-content":"center"},
                                    
                                ),

                                
                                
                            align="center",
                            justify="center",
                            width="100%",
                            style={"overflow":"hidden"}
                        ),

                    align="center",
                    justify="center",
                    padding_top="3em",
                    width="100%"
                ),
                    
                rx.vstack(
                    rx.spinner(),
                    justify="center",
                    align="center"
                )),
        align="center",
        justify="center",
        width="100%")




