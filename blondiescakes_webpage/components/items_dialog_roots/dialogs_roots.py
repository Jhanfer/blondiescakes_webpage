import reflex as rx
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.styles import constants as ct

class SendMessage(rx.State):
    def send_message(self, title):
        return rx.redirect(f"https://wa.me/{ct.CONTACT_NUMBER}?text=Hola,+buenas.+Vi+\"{title}\"+en+su+pagina!")



def dialog(title:str,image:str,item_descirption:str,price:str,switch:bool) -> rx.Component:
    return  motion(
                rx.dialog.root(
                    rx.cond(switch,
                        rx.dialog.trigger(
                            rx.image(
                                src=image,
                                background=st.ColorPalette.MAIN.value,
                                width="20em",
                                height="20em",
                                alt=f"producto: {title}",
                                align="center",
                                display="block",#con esto hacemos que la imagen sea cuadrada sin estrechar
                                style={"overflow":"hidden", #con esto hacemos que la imagen sea cuadrada sin estrechar
                                        "object-fit":"cover",
                                        "border-radius":"15px"
                                },
                            ),
                        ),

                        rx.dialog.trigger(
                                rx.button(
                                    "Saber más",
                                    radius="small",
                                    width="100%",
                                    justify="center",
                                    size="3",
                                ),
                        ),
                    ),

                    rx.dialog.content(
                        rx.hstack(
                            rx.spacer(),
                            rx.dialog.close(
                                rx.button(
                                    rx.icon(tag="x"),
                                    radius="full",
                                    width="3em",
                                    justify="center",
                                ),
                            ),
                            justify="between"
                        ),
                        
                        rx.dialog.description(
                            rx.vstack(
                                rx.heading(title),
                                rx.flex(
                                    #mobile
                                    rx.flex(
                                        rx.image(
                                            src=image,
                                            background=st.ColorPalette.MAIN.value,
                                            width="16em",
                                            height="16em",
                                            alt=f"producto: {title}",
                                            align="center",
                                            display="block",#con esto hacemos que la imagen sea cuadrada sin estrechar
                                            style={"overflow":"hidden", #con esto hacemos que la imagen sea cuadrada sin estrechar
                                                    "object-fit":"cover",
                                                    "border-radius":"15px"
                                            },
                                        ),

                                        
                                        display=["flex", "none", "none", "none", "none"],
                                    ),
                                    rx.flex(
                                        rx.text(item_descirption,size="5"),

                                        rx.text(f"{price} COP", size="6"),
                                        width="17em",
                                        spacing="3",
                                        direction="column",
                                        display=["flex", "none", "none", "none", "none"],
                                    ),

                                    #Desktop
                                    rx.flex(
                                        rx.image(
                                            src=image,
                                            background=st.ColorPalette.MAIN.value,
                                            width="20em",
                                            height="20em",
                                            alt=f"producto: {title}",
                                            align="center",
                                            display="block",#con esto hacemos que la imagen sea cuadrada sin estrechar
                                            style={"overflow":"hidden", #con esto hacemos que la imagen sea cuadrada sin estrechar
                                                    "object-fit":"cover",
                                                    "border-radius":"15px"
                                            },
                                        ),
                                        display=["none", "flex", "flex", "flex", "flex"],
                                    ),
                                    rx.flex(
                                        rx.text(item_descirption, size="5"),
                                        rx.text(f"{price} COP", size="6"),
                                        
                                        width="25em",
                                        spacing="3",
                                        direction="column",
                                        display=["none", "flex", "flex", "flex", "flex"],
                                    ),

                                    direction="row",
                                    spacing="4",
                                    wrap="wrap",
                                    justify="center",
                                    align="center"
                                ),
                                
                                rx.button(
                                    "contacto",
                                    radius="small",
                                    width="50%",
                                    justify="center",
                                    on_click=SendMessage.send_message(title)
                                ),

                                justify="center",
                                align="center"
                            ),
                        ),

                        size="4",
                        style={
                            "max-width":"800px",
                            "background-color":"white",
                            "border-radius":"3em",
                            "animation":"rt-dialog-content-show 350ms cubic-bezier(0.16, 1, 0.3, 1)"
                        }
                    ),

                    style={
                        "filter":"blur(1em)"
                    }

                ),
            while_hover={"scale":1.1},
            while_tap={"scale":0.9},
            transition={"type": "spring", "stiffness":300,"damping":20}
            )