import reflex as rx
from blondiescakes_webpage.components.body_products_items.items import items
from blondiescakes_webpage.styles import constants as c
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion
from blondiescakes_webpage.components.wrapping_react.AwesomeSlider import carousel
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.page_state import PageState

def products_container() -> rx.Component:
        return rx.vstack(
                        rx.flex(
                                rx.image(
                                        src="/body/decoration.svg",
                                        width="15em",
                                        #height="10em",
                                ),
                                top="110em"
                        ),
                        rx.heading("DISFRUTA DEL DULCE CON",
                                size="9",
                                color=st.ColorPalette.ENFASIS.value,
                                style={"font-size":"clamp(1.8em, 3.5vw, 3.5em)"},
                                #padding_top="2em",
                                padding_bottom="1em"
                        ),
                        
                        rx.flex(
                                items(),

                                padding_top="1em",
                                padding_bottom="2em",
                                spacing="8",
                                wrap="wrap",
                                justify="center",
                                align="center",
                        ),

                        rx.hstack(
                                rx.vstack(
                                        rx.icon(tag="truck",width="2em",height="auto",color="black"),
                                        rx.heading("Envios a cali",
                                                justif="center",
                                                align="center",
                                                size="3",
                                                color=st.ColorPalette.ENFASIS.value
                                        ),
                                        
                                        rx.text("Ordena ahora!",
                                                justif="center",
                                                align="center",
                                                size="1",
                                                color=st.ColorPalette.ENFASIS.value,
                                                style={
                                                        "text-align":"normal"
                                                }
                                        ),

                                        justify="center",
                                        style={"align-items":"center",
                                                "max-width":"30%"}
                                ),

                                rx.divider(orientation="vertical",size="4",color_scheme="gold",height="9em"),
                        
                                rx.vstack(
                                        rx.icon(tag="message-circle-more",width="2em",height="auto",color="black"),
                                        rx.heading("Contacto",
                                                justif="center",
                                                align="center",
                                                size="3",
                                                color=st.ColorPalette.ENFASIS.value
                                        ),
                                        
                                        rx.text("Contáctanos en nuestras redes.",
                                                justif="center",
                                                align="center",
                                                size="1",
                                                color=st.ColorPalette.ENFASIS.value,
                                                style={
                                                        "text-align":"normal"
                                                }
                                        ),

                                        justify="center",
                                        style={"align-items":"center",
                                                "max-width":"30%"}
                                ),

                                rx.divider(orientation="vertical",size="4",color_scheme="gold",height="9em"),
                        
                                rx.vstack(
                                        rx.icon(tag="shield-plus",width="2em",height="auto",color="black"),
                                        rx.heading("Seguridad",
                                                justif="center",
                                                align="center",
                                                size="3",
                                                color=st.ColorPalette.ENFASIS.value
                                        ),
                                        
                                        rx.text("Compras 100% seguras.",
                                                justif="center",
                                                align="center",
                                                size="1",
                                                color=st.ColorPalette.ENFASIS.value,
                                                style={
                                                        "text-align":"normal"
                                                }
                                        ),

                                        justify="center",
                                        style={"align-items":"center",
                                                "max-width":"30%"}
                                ),
                        padding_bottom="3em",
                        justify="center",
                        align="center"
                        ),

                align="center",
                justify="center",
                style={"overflow":"hidden"}
        )

