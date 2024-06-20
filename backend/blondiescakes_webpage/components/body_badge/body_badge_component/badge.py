import reflex as rx 
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.body_badge.body_header_textimage.textimage import textimage

def badge() -> rx.Component:
    return rx.hstack(

            rx.image(src="body/badge_item1.png",width="5em",height="5em"),

            rx.vstack(
                    textimage("body/main_badge.png","Más de 3 años de experiencia",st.ColorPalette.MAIN.value,"5"),
                    rx.button("Donde estamos",variant="solid",radius="none",background_color=st.ColorPalette.MAIN.value,color=st.ColorPalette.ENFASIS.value),
                align="center",
                justify="center"),

            rx.image(src="body/badge_item2.png",width="5em",height="5em",margin_top="12em"),

            justify="center",
            align="center",
            margin_bottom="0em",
            width="100%",
            bg=st.ColorPalette.ENFASIS.value,
            height="30em",
            z_index="5"
)

def review() -> rx.Component:
    return rx.hstack(
                
                rx.flex(
                        stack(),
                    spacing="4",
                    display=["none","none","none","flex","flex"]
                ),

                rx.flex(
                        rx.grid(
                            rx.scroll_area(
                                rx.flex(
                                        stack(),
                                    spacing="4"
                                ),
                            scrollbars="horizontal",
                            type="always"
                        ),
                    padding="1em"),
                display=["flex","flex","flex","none","none","none"]),

            justify="center",
            align="center",
            margin_bottom="0em",
            width="100%",
            bg=st.ColorPalette.ENFASIS.value,
            height="30em",
            z_index="5"
)

def card(name:str,review:str) -> rx.Component:
    return rx.card(
            rx.vstack(
                        rx.chakra.avatar(name="RE",size="xl"),
                        rx.text(review),
                        rx.text(name),
                        rx.hstack(
                                rx.icon(tag="star",color="gold"),
                                rx.icon(tag="star",color="gold"),
                                rx.icon(tag="star",color="gold"),
                                rx.icon(tag="star-half",color="gold"),
                            spacing="0"    
                        )
                        
                    ),
            width="20em",
            height="15em",
            bg="white")

def stack() -> rx.Component:
    return (card("Ana María","Me encanta!"),
            card("Juan Alberto","Excelente sabor"),
            card("Teressa Gomez","No existe mejor sabor!"))