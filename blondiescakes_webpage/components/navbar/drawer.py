import reflex as rx
from blondiescakes_webpage.styles import styles as st
#from blondiescakes_webpage.components.wrapping_react.sidebar import 

class DrawerState(rx.State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)

def drawer() -> rx.Component:
    return rx.chakra.vstack(
        rx.vstack(
                rx.image(src="/navbar/navbar.png",
                    width="6em",
                    height="auto",
                    position="relative"),
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
                    rx.chakra.drawer_header("Confirm"),
                    rx.chakra.drawer_body(
                        "Do you want to confirm example?"
                    ),
                    rx.chakra.drawer_footer(
                        rx.chakra.button(
                            "Close",
                            on_click=DrawerState.right,
                        )
                    ),
                    bg="#463626",
                )
            ),
            is_open=DrawerState.show_right,
        ),
    )




#terminar el sidebar o buscar mejores opciones de sidebar



def erre(): 
    return rx.drawer.root(
                    rx.drawer.trigger(
                            rx.vstack(
                                rx.image(src="/navbar/navbar.png",
                                    width="6em",
                                    height="auto",
                                    position="relative"),
                                rx.text("MENÚ",size="2",color=st.ColorPalette.ENFASIS.value),
                                rx.icon(tag="chevron-down",size=20,color=st.ColorPalette.LINES.value),
                                spacing="0",
                                align="center",
                                justify="center"
                            ),
                    padding_top="0.3em",
                    ),

                    rx.drawer.overlay(z_index="6"),

                    rx.drawer.portal(
                        rx.drawer.content(
                            rx.vstack(

                                rx.flex(
                                    rx.drawer.close(rx.box(rx.button("Cerrar",radius="none"),align="end")),
                                    padding_left="13em",
                                    direction="column"),
                                
                                menu_button("INICIO","/"),
                                menu_button("CONTACTO","/nosotros#contacto"),
                                menu_button("ENVÍOS","/nosotros#envios"),
                                menu_button("NOSOTROS","/nosotros"),
                                menu_button("VISIÓN","/nosotros#vision"),
                                menu_button("MISIÓN","/nosotros#mision"),
                                
                                justify="start",
                                align="center"),
# rx.call_script("window.location.reload();")
                            top="auto",
                            right="auto",
                            left="2.7em",
                            height="100%",
                            width="100%",
                            padding="2em",
                            background_color=st.TextColor.TITLES.value)),
            direction="right",
            )

def menu_button(title:str,route:str) -> rx.Component:
    return  rx.link(
                rx.button(
                    title,
                    width="100%",
                    radius="none",
                ),
                href=route,
                is_external=False,
            )












"""


"""



"""def drawer_example():
    return rx.chakra.vstack(
        rx.chakra.button(
            "Abrir Drawer", on_click=DrawerState.toggle_drawer
        ),
        rx.chakra.drawer(
            rx.chakra.drawer_overlay(
                rx.chakra.drawer_content(
                    rx.chakra.drawer_header("Confirmar"),
                    rx.chakra.drawer_body(
                        "¿Quieres confirmar el ejemplo?"
                    ),
                    rx.chakra.drawer_footer(
                        rx.chakra.button(
                            "Cerrar y Actualizar",
                            on_click=DrawerState.close_and_refresh,
                        )
                    ),
                    bg="rgba(0, 0, 0, 0.3)",
                )
            ),
            is_open=DrawerState.show_right,
        ),
    )"""
