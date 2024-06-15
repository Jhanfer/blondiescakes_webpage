import reflex as rx 
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.body_badge.body_header_textimage.textimage import textimage

def badge() -> rx.Component:
    return rx.hstack(
            rx.image(src="body/badge_item1.png",width="6em",height="6em"),
            rx.vstack(
                    textimage("body/main_badge.png","Más de 3 años de experiencia"),
                    rx.button("Donde estamos",variant="solid",radius="none",background_color=st.ColorPalette.MAIN.value,color=st.ColorPalette.ENFASIS.value),
                align="center"),
            rx.image(src="body/badge_item2.png",width="6em",height="6em",margin_top="12em"),

            justify="center",
            padding="12em",
            margin_bottom="0em",
            width="100%",
            bg=st.ColorPalette.ENFASIS.value
)