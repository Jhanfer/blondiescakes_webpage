import reflex as rx
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.navbar.drawer import drawer
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion

def navbar() -> rx.Component:
    return  motion(
                    rx.hstack(
                        rx.box(
                                navbar_content(),
                            display=["none", "none", "none", "flex", "flex"],
                            height="100%",
                            width="100%"),
                            

                        rx.box(
                                navbar_content_mobile(),
                            display=["flex", "flex", "flex", "none", "none"],
                            width="100%",
                        ),
                        
                    class_name="gradient-element",
                    justify="center",
                    width="100%",
                    height="7em",
                    z_index = "5000",
                    id="navbar",
                    ),
                    
                
                z_index = "5000",
                width="100%",
                position="fixed",
                align="center",
                initial={"y":-100},
                animate={"y":0},
                transition={"type":"keyframes","ease":"easeIn","diration":1}
                ),
            




#Navbar components

def text(text:str,href:str) -> rx.Component:
    return rx.link(
            rx.text(text,
                    color=st.TextColor.TITLES.value,
                    size="5"
                    ),
                is_external=False,
                href=href,
                padding_left="1em",
                padding_right="1em"
            )

def navbar_content() -> rx.Component:
    return rx.hstack(

        rx.vstack(
            rx.flex(
                text("INICIO","/"),
                text("CONTACTO","/nosotros#contacto"),
                text("ENVÍOS","/nosotros#envios"),
                display=["none", "none", "none", "flex", "flex"],
                direction="row"
                ),

            rx.chakra.divider(decorative=True,color=st.ColorPalette.LINES.value,border_color=st.ColorPalette.LINES.value)),

        rx.image(
            src="/navbar/navbar.png",
            width="7.9em",
            height="5em",
            position="sticky",
            on_click=rx.redirect("/"),
            alt="Logo de Blondie´s Cake"
        ),

        rx.vstack(
            rx.flex(
                text("NOSOTROS","/nosotros"),
                text("VISIÓN","/nosotros#vision"),
                text("MISIÓN","/nosotros#mision"),
                display=["none", "none", "none", "flex", "flex"],
                direction="row"
                ),
            rx.chakra.divider(decorative=True,color=st.ColorPalette.LINES.value,border_color=st.ColorPalette.LINES.value)),

        width="100%",
        align="center",
        justify="center",
        spacing="8",
        style={"overflow":"hiddend"}
        )


def navbar_content_mobile() -> rx.Component:
    return rx.hstack(

        rx.divider(size="3",color_scheme="gold", decorative=True),
        drawer(),
        rx.divider(size="3",color_scheme="gold", decorative=True),
        
        spacing="8",
        justify="center",
        align="center",
        width="100%",
        padding_left="1em",
        padding_right="1em",
        height="7em"
    )

