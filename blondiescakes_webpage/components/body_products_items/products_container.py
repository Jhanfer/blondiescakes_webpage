import reflex as rx
from blondiescakes_webpage.components.body_products_items.items import items
from blondiescakes_webpage.styles import constants as c
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion
from blondiescakes_webpage.components.wrapping_react.AwesomeSlider import carousel
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.page_state import PageState

def products_container() -> rx.Component:
        return rx.vstack(
                        
                        #Highlight - Hacer que se pudan cambiar las imagenes desde backend
                        rx.flex(
                                rx.image(
                                        src="/body/decoration.svg",
                                        width="20em",
                                        #height="10em",
                                        id="productos",
                                        alt="Decoración en forma de ramas y corazón"
                                ),
                                top="110em"
                        ),
                        #Desktop
                        rx.flex(
                                rx.vstack(
                                        rx.text(
                                                "Festeja en grande",
                                                style={
                                                        "line-height":"0.9em",
                                                        "font-size":"clamp(3rem, 3.5vw + 1.8rem, 3.8rem)",
                                                        "--line-height":"var(--heading-line-height-9)",
                                                        "font-family":"pertili",
                                                        "align":"center",
                                                        "justify_content":"center",
                                                        "text-align":"-webkit-center"
                                                },
                                                position="relative"
                                        ),
                                
                                        rx.text("""
                                                Nuestros pasteles de cumpleaños. 
                                                Su bizcocho esponjoso, su mousse 
                                                de chocolate y una capa de buttercream 
                                                que se derrite en la boca. Decorado 
                                                con delicadas piezas comestibles, 
                                                es un verdadero festín para los sentidos.
                                                """,
                                                style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}
                                        ),
                                        max_width="35em",
                                        padding="1em",
                                        spacing="8"
                                ),

                                rx.image(
                                        src="/header/header.jpeg",
                                        width="35em",
                                        height="auto",
                                        alt="Pastel de cumpleaños"
                                ),

                                width="100%",
                                spacing="9",
                                wrap="wrap",
                                padding_top="1em",
                                padding_bottom="5em",
                                padding_left="1em",
                                padding_right="1em",
                                direction="row",
                                justify="center",
                                align="center",
                        ),


                        #Heading and decorations
                        rx.flex(
                                rx.image(
                                        src="/body/decoration.svg",
                                        width="15em",
                                        #height="10em",
                                        id="productos",
                                        alt="Decoración en forma de ramas y corazón"
                                ),
                                top="110em"
                        ),
                        rx.text(
                                "DISFRUTA DEL DULCE CON",
                                size="9",
                                color=st.ColorPalette.ENFASIS.value,
                                style={
                                        "font-size":"clamp(1.8em, 3.5vw, 3.5em)",
                                        "font-family":"pertili",
                                        "align":"center",
                                        "justify_content":"center",
                                        "text-align":"-webkit-center"
                                },
                                #padding_top="2em",
                                padding_bottom="1em",
                                
                        ),
                        
                        #Items
                        rx.flex(
                                        items(),

                                padding_top="1em",
                                padding_bottom="2em",
                                spacing="8",
                                wrap="wrap",
                                justify="center",
                                align="center",
                        ),


                        
                        #Other products
                        rx.text(
                                "¡Más Sabores!", 
                                size="9",
                                padding_top="2em",
                                style={"font-family":"pertili"}
                        ),
                        rx.hstack(
                                
                                rx.flex(
                                        other_products("/body/other_products/cake.jpg","Pasteles"),
                                        other_products("/body/other_products/cookies.jpg","Galletas"),
                                        other_products("/body/other_products/cupcakes.jpg","Cupcakes"),
                                        other_products("/body/other_products/flan.jpg","Flan"),

                                spacing="4",
                                display=["none","none","none","flex","flex"]
                                ),

                                rx.flex(
                                        rx.grid(
                                                rx.scroll_area(
                                                        rx.flex(
                                                                other_products("/body/other_products/cake.jpg","Pasteles"),
                                                                other_products("/body/other_products/cookies.jpg","Galletas"),
                                                                other_products("/body/other_products/cupcakes.jpg","Cupcakes"),
                                                                other_products("/body/other_products/flan.jpg","Flan"),

                                                        spacing="4"
                                                        ),
                                                scrollbars="horizontal",
                                                type="always"
                                                ),
                                padding="1em"),
                                display=["flex","flex","flex","none","none","none"]
                                ),

                        justify="center",
                        align="center",
                        width="100%",
                        z_index="5",
                ),
                rx.flex(
                        rx.vstack(
                                rx.text(
                                        """
                                        En Blondie's Cake nos enorgullecemos de ofrecer productos 
                                        versátiles y de alta calidad, cuidadosamente elaborados 
                                        para brindarte la mejor experiencia. Desde delicados pasteles
                                        hasta nuestras creaciones más innovadoras.
                                        """,
                                        color=st.ColorPalette.ENFASIS.value,
                                        style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}
                                ),
                                max_width="60em",
                                width="100%",
                                padding="3em",
                                align="center",
                                justify="center",
                                spacing="6"
                        ),
                        align="center",
                        justify="center",
                        padding_top=st.Size.MEDIUM,
                        padding_bottom=st.Size.LARGE.value
                ),

                        #Icons
                        rx.hstack(
                                rx.vstack(
                                        rx.icon(tag="truck",width="2em",height="auto",color="black"),
                                        rx.heading("Envios a cali",
                                                justif="center",
                                                align="center",
                                                size="3",
                                                color=st.ColorPalette.ENFASIS.value
                                        ),
                                        
                                        rx.text("Ordena ahora!",
                                                justif="center",
                                                align="center",
                                                size="1",
                                                color=st.ColorPalette.ENFASIS.value,
                                                style={
                                                        "text-align":"normal"
                                                }
                                        ),

                                        justify="center",
                                        style={"align-items":"center",
                                                "max-width":"30%"}
                                ),

                                rx.divider(orientation="vertical",size="4",color_scheme="gold",height="9em"),
                        
                                rx.vstack(
                                        rx.icon(tag="message-circle-more",width="2em",height="auto",color="black"),
                                        rx.heading("Contacto",
                                                justif="center",
                                                align="center",
                                                size="3",
                                                color=st.ColorPalette.ENFASIS.value
                                        ),
                                        
                                        rx.text("Contáctanos en nuestras redes.",
                                                justif="center",
                                                align="center",
                                                size="1",
                                                color=st.ColorPalette.ENFASIS.value,
                                                style={
                                                        "text-align":"normal"
                                                }
                                        ),

                                        justify="center",
                                        style={"align-items":"center",
                                                "max-width":"30%"}
                                ),

                                rx.divider(orientation="vertical",size="4",color_scheme="gold",height="9em"),
                        
                                rx.vstack(
                                        rx.icon(tag="shield-plus",width="2em",height="auto",color="black"),
                                        rx.heading("Seguridad",
                                                justif="center",
                                                align="center",
                                                size="3",
                                                color=st.ColorPalette.ENFASIS.value
                                        ),
                                        
                                        rx.text("Compras 100% seguras.",
                                                justif="center",
                                                align="center",
                                                size="1",
                                                color=st.ColorPalette.ENFASIS.value,
                                                style={
                                                        "text-align":"normal"
                                                }
                                        ),

                                        justify="center",
                                        style={"align-items":"center",
                                                "max-width":"30%"}
                                ),
                        padding_bottom="3em",
                        justify="center",
                        align="center"
                        ),

                align="center",
                justify="center",
                style={
                        "overflow":"hidden"
                }
        )


def other_products(src:str,text:str) -> rx.Component:
        return motion(
                rx.flex(
                        
                        rx.flex(
                                rx.text(
                                        text,
                                        
                                        z_index="100000",
                                        color=st.ColorPalette.MAIN.value,
                                        style={
                                                "font-size":"2em",
                                        }
                                ),
                                width="17em",
                                height="18em",
                                style={ 
                                        "background-image":f"url('{src}')",
                                        "border-radius":"30em 30em 0em 0em",
                                        "background-size":"cover"
                                },
                                align="center",
                                justify="center",
                        ),
                        align="center",
                        justify="center",
                        width="17em",
                        height="18em",
                        
                ),
                
        while_hover={"opacity":0.9},
        transition={"damping":20,"swiftness":20}
        )


