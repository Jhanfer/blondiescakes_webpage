import reflex as rx
from blondiescakes_webpage.styles import styles as st
#from blondiescakes_webpage.components.wrapping_react.sidebar import 

class DrawerState(rx.State):
    show_right: bool = False
    show_top: bool = False

    def right(self):
        self.show_right = not (self.show_right)

def drawer() -> rx.Component:
    return rx.chakra.vstack(
        rx.vstack(
                rx.image(
                    src="/navbar/navbar.png",
                    width="6em",
                    height="auto",
                    position="relative",
                    alt="Logo de Blondie´s Cake"
                ),
                rx.text("MENÚ",size="2",color=st.ColorPalette.ENFASIS.value),
                rx.icon(tag="chevron-down",size=20,color=st.ColorPalette.LINES.value),
                spacing="0",
                align="center",
                justify="center",
                on_click=DrawerState.right,
                style={"cursor":"pointer"}
            ),
        rx.chakra.drawer(
            rx.chakra.drawer_overlay(
                rx.chakra.drawer_content(
                    rx.chakra.drawer_header(
                                rx.image(
                                    src="/navbar/navbar.png",
                                    background_color=st.ColorPalette.MAIN.value,
                                    border_radius="15px",
                                    padding="1em",
                                    margin_bottom="1em",
                                    on_click=[DrawerState.right,rx.redirect("/")],
                                    alt="Logo de Blondie´s Cake",
                                    style={
                                        "cursor":"pointer"
                                    }
                                ),
                            "Menú",
                            color=st.ColorPalette.MAIN.value,
                            justify="center"
                    ),
                    rx.chakra.drawer_body(
                            rx.chakra.vstack(
                                menu_button("INICIO","/","home"),
                                menu_button("CONTACTO","/nosotros#contacto","phone"),
                                menu_button("ENVÍOS","/nosotros#envios","truck"),
                                menu_button("NOSOTROS","/nosotros","user"),
                                menu_button("VISIÓN","/nosotros#vision","telescope"),
                                menu_button("MISIÓN","/nosotros#mision","circle-slash"),

                                width="100%",
                                spacing="4"
                            ),
                        display=["flex", "flex", "flex", "flex", "none"],
                    ),
                    rx.chakra.drawer_footer(
                        rx.button(
                                rx.chakra.hstack(
                                    rx.icon(tag="ban",color=st.ColorPalette.MAIN.value,size=20),
                                    rx.text("Cerrar",color=st.ColorPalette.MAIN.value),
                                    spacing="9"
                                ),
                            width="100%",
                            on_click=[DrawerState.right],
                            padding="0.5em",
                            style={
                                "justify-content":"normal",
                                "variant":"ghost",
                                "border-radius":"15px",
                                "background_color":"transparent",
                            }
                        ),
                    ),
                    bg="#463626",
                )
            ),
            is_open=DrawerState.show_right,
            close_on_esc=True,
            close_on_overlay_click=True,
            on_esc=DrawerState.right,
            on_overlay_click=DrawerState.right,
            size="xs"
            
        ),
    )



def menu_button(title:str,route:str,icon:str) -> rx.Component:
    return  rx.button(
                    rx.chakra.hstack(
                        rx.icon(tag=icon,color=st.ColorPalette.MAIN.value,size=20),
                        rx.text(title,color=st.ColorPalette.MAIN.value),
                        spacing="9"
                    ),
                width="100%",
                on_click=[DrawerState.right,rx.redirect(route)],
                padding="0.5em",
                style={
                    "justify-content":"normal",
                    "variant":"ghost",
                    "border-radius":"15px",
                    "background_color":"transparent",
                }
            )