import reflex as rx
from blondiescakes_webpage.components.body_products_items.items import items
from blondiescakes_webpage.styles import constants as c
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion

def products_container() -> rx.Component:
        return rx.vstack(


                motion(
                        rx.flex(
                                rx.text("ENVIOS A TODA CALI",
                                        color=st.TextColor.TITLES.value
                                ),
                        ),
                        animate={"x":[-1000,1000]},
                        transition={"duration":10,
                                "ease":"easeInOut",
                                "repeat":"Infinity",
                                }
                ),
        rx.text("DISFRUTA DEL DULCE",size="7",color=st.ColorPalette.ENFASIS.value),
        rx.flex(
                items(),
                padding_top="2em",
                spacing="8",
                wrap="wrap",
                justify="center",
                align="center"),

        padding_top="4em",
        align="center",
        justify="center",
        style={"overflow":"hidden"}
)


