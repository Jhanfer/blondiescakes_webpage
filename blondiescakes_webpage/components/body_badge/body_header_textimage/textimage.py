import reflex as rx
from blondiescakes_webpage.styles import styles as st


def textimage(image:str,text:str) -> rx.Component:
    return rx.box(
                rx.text(text,size="6",position="absolute",margin="0.7em",padding_top="1em",color=st.ColorPalette.ENFASIS.value),
                rx.image(
                    src=image,
                    width="18em",
                    height="18em")),