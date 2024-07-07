import reflex as rx 
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.body_badge.body_header_textimage.textimage import textimage
from blondiescakes_webpage.components.wrapping_react.AwesomeSlider import carousel
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion
#from blondiescakes_webpage.components.wrapping_react.instagram_api import InstaAPI

def badge() -> rx.Component:
    return rx.vstack(
            rx.heading("Síguenos en instagram",color=st.ColorPalette.MAIN.value,position="absolute",padding_bottom="18em"),
            
            
            
            rx.vstack(
                    carousel(
                            rx.card(
                                    motion(
                                        rx.image(
                                            src="body/badge_carousel.jpeg",
                                            width="20em",
                                            height="auto",
                                            on_click=rx.redirect("https://www.instagram.com/p/C6y3SRtgcw3/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==")
                                        ),
                                    while_hover={"scale":1.1},
                                    while_tap={"scale":0.9},
                                    transition={"type": "spring", "stiffness":300,"damping":20}
                                    ),
                                size="5"
                            ),
                            rx.card(
                                    motion(
                                        rx.image(
                                            src="body/badge_carousel2.jpeg",
                                            width="20em",
                                            height="auto",
                                            on_click=rx.redirect("https://www.instagram.com/p/C6owde_gA7a/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==")
                                        ),
                                    while_hover={"scale":1.1},
                                    while_tap={"scale":0.9},
                                    transition={"type": "spring", "stiffness":300,"damping":20}    
                                    ),
                                size="4"
                            ),
                            rx.card(
                                    motion(
                                        rx.image(
                                            src="body/badge_carousel3.jpeg",
                                            width="20em",
                                            height="auto",
                                            on_click=rx.redirect("https://www.instagram.com/p/C1j5c2oAscv/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==")
                                        ),
                                    while_hover={"scale":1.1},
                                    while_tap={"scale":0.9},
                                    transition={"type": "spring", "stiffness":300,"damping":20}
                                    ),    
                                size="4"
                            ),
                        animation="fallAnimation",
                        mobile_touch=True,
                        bullets=False,
                        style={"width":"80%",
                                "--content-background-color":"transparent",
                                "--control-button-width":"30%",
                                "--slider-height-percentage":"80%",
                                "--organic-arrow-height":"20px",
                                "--organic-arrow-color":f"{st.ColorPalette.MAIN.value}"

                                }, 
                    ),
                    
                width="100%",
                justify="center",
                align="center",
                padding_bottom="2em",
                style={"overflow":"hidden"}
            ),
            
            justify="center",
            align="center",
            margin_bottom="3em",
            width="100%",
            bg=st.ColorPalette.ENFASIS.value,
            height="30em",
            z_index="10",
            padding_top="5em"
)


"""  rx.image(src="body/badge_item1.png",width="5em",height="5em"),

            rx.vstack(
                    textimage("body/main_badge.png","Más de 3 años de experiencia",st.ColorPalette.MAIN.value,"5"),
                    rx.button("Donde estamos",variant="solid",radius="none",background_color=st.ColorPalette.MAIN.value,color=st.ColorPalette.ENFASIS.value),
                align="center",
                justify="center"),

            rx.image(src="body/badge_item2.png",width="5em",height="5em",margin_top="12em"),
"""


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

def card(name:str,review:str,src:str) -> rx.Component:
    return rx.card(
            rx.vstack(
                        rx.chakra.avatar(name="I",size="xl",src=src),
                        rx.text(review,color=st.ColorPalette.ENFASIS.value),
                        rx.text(name,color=st.ColorPalette.ENFASIS.value),
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
    return (card("Lisue","Me encanta!","/body/lisue.jpeg"),
            card("Juan","Excelente sabor","/body/juan.jpeg"),
            card("Teressa","No existe mejor sabor!","/body/teressa.jpeg"))










def ig_image(image:list) -> rx.Component:
    return rx.card(
        rx.image(
            src=image
        )
    )