import reflex as rx
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.body_badge.body_header_textimage.textimage import textimage

def header() -> rx.Component:
    return rx.hstack(

        rx.tablet_and_desktop(
            rx.hstack(
                    rx.text("@BLONDIES_CAKE",color=st.ColorPalette.ENFASIS.value,),
                    textimage("header/header_image_example.png","Regala amor, regala dulce"),
                    rx.text("PASTELERÍA A LA CARTA",color=st.ColorPalette.ENFASIS.value,),
                align="center",
                justify="center",
                spacing="9",
                padding_top="5em")),

        rx.mobile_only(
            rx.vstack(
                    rx.text("PASTELERÍA A LA CARTA"),
                    textimage("header/header_image_example.png","Regala amor, regala dulce"),
                align="center",
                justify="center",
                padding_top="7em"),
        ),

        spacing="9",
        align="center",
        justify="center",
        width="100%",
        padding_top="3em",
        padding_left="3em",
        padding_right="3em",
        padding_bottom="5em"
    )