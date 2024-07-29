import reflex as rx
from blondiescakes_webpage.styles import styles as st

def drawer() -> rx.Component:
    return rx.drawer.root(
                    rx.drawer.trigger(
                        
                                rx.vstack(
                                    rx.image(src="/navbar/navbar.png",
                                        width="4.9em",
                                        height="3em",
                                        position="relative"),
                                    rx.text("MENÚ",size="2",color=st.ColorPalette.ENFASIS.value),
                                    rx.icon(tag="chevron-down",size=20,color=st.ColorPalette.LINES.value),
                                    spacing="0",
                                    align="center",
                                    justify="center"),
                                
                    padding_top="0.3em"),

                    rx.drawer.overlay(z_index="6"),

                    rx.drawer.portal(
                        rx.drawer.content(
                            rx.vstack(

                                rx.flex(
                                    rx.drawer.close(rx.box(rx.button("Cerrar",radius="none"),align="end")),
                                    padding_left="13em",
                                    direction="column"),

                                menú_button("INICIO","/"),
                                menú_button("CONTACTO","/contactanos"),
                                menú_button("ENVÍOS",""),
                                menú_button("NOSOTROS",""),
                                menú_button("VISIÓN",""),
                                menú_button("MISIÓN",""),
                                justify="start",
                                align="center"),

                            top="auto",
                            right="auto",
                            left="2.7em",
                            height="100%",
                            width="100%",
                            padding="2em",
                            background_color=st.TextColor.TITLES.value)),
            direction="right")

def menú_button(title:str,route:str) -> rx.Component:
    return  rx.button(
                title,
                width="100%",
                radius="none",
                on_click=rx.redirect(route)
            )
