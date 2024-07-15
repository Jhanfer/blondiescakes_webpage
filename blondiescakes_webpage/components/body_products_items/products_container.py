import reflex as rx
from blondiescakes_webpage.components.body_products_items.items import items
from blondiescakes_webpage.styles import constants as c
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion
from blondiescakes_webpage.components.wrapping_react.AwesomeSlider import carousel

def products_container() -> rx.Component:
        return rx.vstack(
                        
                        rx.hstack(
                                rx.vstack(
                                        rx.icon(tag="truck",width="2em",height="auto"),
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
                                                color=st.ColorPalette.ENFASIS.value
                                        ),

                                        justify="center",
                                        style={"align-items":"center",
                                                "max-width":"30%"}
                                ),

                                rx.divider(orientation="vertical",size="4",color_scheme="gold",height="9em"),
                        
                                rx.vstack(
                                        rx.icon(tag="message-circle-more",width="2em",height="auto"),
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
                                                color=st.ColorPalette.ENFASIS.value
                                        ),

                                        justify="center",
                                        style={"align-items":"center",
                                                "max-width":"30%"}
                                ),

                                rx.divider(orientation="vertical",size="4",color_scheme="gold",height="9em"),
                        
                                rx.vstack(
                                        rx.icon(tag="shield-plus",width="2em",height="auto"),
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
                                                color=st.ColorPalette.ENFASIS.value
                                        ),

                                        justify="center",
                                        style={"align-items":"center",
                                                "max-width":"30%"}
                                ),
                        padding_bottom="3em",
                        justify="center",
                        align="center"
                        ),

                        rx.text("DISFRUTA DEL DULCE CON",size="7",color=st.ColorPalette.ENFASIS.value),
                        rx.flex(
                                items(),
                                padding_top="1em",
                                padding_bottom="2em",
                                spacing="8",
                                wrap="wrap",
                                justify="center",
                                align="center"
                        ),
                #padding_top="4em",
                align="center",
                justify="center",
                style={"overflow":"hidden"}
        )



"""rx.hstack("

                                motion(        
                                        rx.box(
                                                rx.hstack(
                                                        rx.vstack(
                                                                rx.text("ENVIOS A CALI",
                                                                        size="3",
                                                                        color=st.TextColor.TITLES.value
                                                                ),
                                                                rx.text("hacemos envios a domicilio en toda cali!",
                                                                        size="1",
                                                                        color=st.TextColor.TITLES.value),
                                                        justify="center",
                                                        align="center",
                                                        ),
                                                        rx.icon(tag="truck",width="5em"),
                                                justify="center",
                                                align="center",
                                                max_width="70%"
                                                ),
                                        radius="full",
                                        width="15em",
                                        height="8em"
                                        ),
                                initial={"scale":1},
                                while_hover={"scale":1.1},
                                transition={
                                        "swiftness":260,
                                        "damping":20,
                                        "ease":"easeInOut"
                                        },
                                ),

                                motion(
                                        rx.box(        
                                                rx.hstack(        
                                                        rx.vstack(
                                                                rx.text("CONTACTACTA!",
                                                                        size="3",
                                                                        color=st.TextColor.TITLES.value
                                                                ),
                                                                rx.text("Nos puedes contactar a través de nuestras redes sociales!",
                                                                        size="1",
                                                                        color=st.TextColor.TITLES.value),
                                                        justify="center",
                                                        align="center",
                                                        
                                                        ),
                                                        rx.icon(tag="message-circle-more",width="5em"),
                                                justify="center",
                                                align="center",
                                                max_width="70%"
                                                ),
                                        radius="full",
                                        width="15em",
                                        height="8em"
                                        
                                        ),
                                initial={"scale":1},
                                while_hover={"scale":1.1},
                                transition={
                                        "swiftness":260,
                                        "damping":20,
                                        "ease":"easeInOut"
                                        },
                        
                                ),

                                motion(
                                        rx.box(        
                                                rx.hstack(        
                                                        rx.vstack(
                                                                rx.text("CONFIABLES",
                                                                        size="3",
                                                                        color=st.TextColor.TITLES.value
                                                                ),
                                                                rx.text("Somos una empresa confiable. Puedes contactar y realizar tu pedido con seguridad!",
                                                                        size="1",
                                                                        color=st.TextColor.TITLES.value),
                                                        justify="center",
                                                        align="center",
                                                        
                                                        ),
                                                        rx.icon(tag="shield-plus",width="5em"),
                                                justify="center",
                                                align="center",
                                                
                                                max_width="70%"
                                                ),
                                        radius="full",
                                        width="15em",
                                        height="8em"
                                        
                                        ),
                                initial={"scale":1},
                                while_hover={"scale":1.1},
                                transition={
                                        "swiftness":260,
                                        "damping":20,
                                        "ease":"easeInOut"
                                        },
        
                                ),
                        width="80%",
                        spacing="2",
                        justify="center",
                        align="center",
                        
                        ),"""