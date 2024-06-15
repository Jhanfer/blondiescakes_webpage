import reflex as rx
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.body_badge.body_header_textimage.textimage import textimage

def header() -> rx.Component:
    return rx.hstack(
        rx.text("@BLONDIES_CAKE",color=st.ColorPalette.ENFASIS.value),
        rx.spacer(),
        textimage("header/header_image_example.png","Regala amor, regala dulce"),
        rx.spacer(),
        rx.text("PASTELERÍA A LA CARTA",color=st.ColorPalette.ENFASIS.value),

        spacing="9",
        align="center",
        justify="center",
        width="100%",
        padding_top="5em",
        padding_left="3em",
        padding_right="3em",
        padding_bottom="5em"
    )