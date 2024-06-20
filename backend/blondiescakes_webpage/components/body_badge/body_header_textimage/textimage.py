import reflex as rx
from blondiescakes_webpage.styles import styles as st
from typing import Optional

def textimage(image:str,text:str,color:Optional[str]=st.ColorPalette.ENFASIS.value,size:Optional[str]="6") -> rx.Component:
    return rx.box(
                rx.text(text,
                        size=size,
                        color=color,
                        align="center",
                        justify="center",
                        position="relative"),

                rx.image(
                    src=image,
                    width="18em",
                    height="auto",
                    position="static",
                    object_fit="cover"),
                    
                align="center",
                justify="center")