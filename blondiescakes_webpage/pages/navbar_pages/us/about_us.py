import reflex as rx
from blondiescakes_webpage.components.navbar.navbar import navbar
from blondiescakes_webpage.views.index_body.footer.footer import footer
from blondiescakes_webpage.styles import styles as st
import re


class SendWatsAppMessage(rx.State):
    message:str
    def send_message(self):
        if not len(self.message) == 0:
            num="121212"
            message = f"https://wa.me/{num}?text={re.sub(r'(\S)\s+(\S)', r'\1%20\2', self.message.strip())}"
            return rx.redirect(message)
    def update_message(self,message:str):
        self.message = message



@rx.page(
    route="/nosotros"
)

def us() -> rx.Component:
    return rx.vstack(
        navbar(),

        rx.flex(
            rx.heading("¿Quienes Somos?",position="relative",style={"font-size":"clamp(1.875rem, 1.301rem + 2.449vw, 3.95rem)"}),
            rx.flex( 
                rx.box(    
                    rx.image(
                            src="/body/badge_carousel2.jpeg",
                            width="clamp(1rem, 9vw + 20rem, 30rem)",
                            height="auto",
                            class_name="image-container",
                    ),
                    class_name="container-image"
                ),
                rx.vstack(
                    rx.heading("¡Hola! ¡Soy la chef y pastelera de Blondie’s Cake, Joselyn!",
                            style={"font-size":"clamp(2rem, 1.5vw + 1.8rem, 1.8rem)"}
                    ),
                    rx.text("""
                            Me encanta hacer tortas personalizadas que se ajusten a tu estilo
                            y el tema de tu evento. Desde tortas de cumpleaños temáticas hasta
                            tortas de bodas, ¡Lo hago todo! ¿Deseas una deliciosa torta cubierta
                            con buttercream y flores comestibles? ¡Llámame! ¿Quieres una clásica
                            torta de chocolate con un toque moderno?¡Envíame un mensaje
                            para convertir tu idea en una realidad azucarada!""",
                            style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}
                        ),
                max_width="35em",
                padding="2em"
                ),
            spacing="9",
            direction="row",
            wrap="wrap",
            justify="center",
            align="center"
            ),
            
            rx.vstack(    
                rx.heading("""¿Hay algo más especial que celebrar un
                        momento importante con un pastel delicioso?""",
                        style={"font-size":"clamp(2rem, 1.5vw + 1.8rem, 1.8rem)"}
                ),
                rx.text("""Lo mío son los ingredientes frescos y de temporada.
                        Considero que una torta rica debe ser, además, sana.
                        Si los productos locales son lo tuyo y los sabores
                        auténticos te encantan, ¡aquí estamos para vos!
                        ¿Qué opinás de una torta de zanahoria con frosting 
                        de queso crema y nueces? ¿Y qué me decís de un red
                        velvet clásico pero regular y sin colorante artificial?""",
                        style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}
                        
                ),
            width="auto",
            max_width="50em",
            padding="2em"
            ),
            

            rx.flex(
                rx.flex(
                    rx.flex(
                        rx.heading("1"),
                        rx.heading("PRUEBA"),
                        rx.text("""Lorem ipsum dolor sit amet, consectetur 
                                adipiscing elit, sed do eiusmod tempor incididunt 
                                ut labore et dolore magna aliqua. Ut enim ad minim 
                                veniam, quis nostrud exercitation ullamco laboris 
                                nisi ut aliquip ex ea commodo consequat. Duis aute 
                                irure dolor in reprehenderit in voluptate velit esse 
                                cillum dolore eu fugiat nulla pariatur. Excepteur sint 
                                occaecat cupidatat non proident, sunt in culpa qui officia 
                                deserunt mollit anim id est laborum."""
                        ),
                    width="20em",
                    direction="column"
                    ),
                    rx.flex(
                        rx.heading("1"),
                        rx.heading("PRUEBA"),
                        rx.text("""Lorem ipsum dolor sit amet, consectetur 
                                adipiscing elit, sed do eiusmod tempor incididunt 
                                ut labore et dolore magna aliqua. Ut enim ad minim 
                                veniam, quis nostrud exercitation ullamco laboris 
                                nisi ut aliquip ex ea commodo consequat. Duis aute 
                                irure dolor in reprehenderit in voluptate velit esse 
                                cillum dolore eu fugiat nulla pariatur. Excepteur sint 
                                occaecat cupidatat non proident, sunt in culpa qui officia 
                                deserunt mollit anim id est laborum."""
                        ),
                    width="20em",
                    direction="column"
                    ),
                direction="row",
                wrap="wrap",
                max_width="45em",
                width="100%",
                spacing="9",
                justify="center",
                align="center"
                ),

                rx.flex(
                    rx.flex(
                        rx.heading("1"),
                        rx.heading("PRUEBA"),
                        rx.text("""Lorem ipsum dolor sit amet, consectetur 
                                adipiscing elit, sed do eiusmod tempor incididunt 
                                ut labore et dolore magna aliqua. Ut enim ad minim 
                                veniam, quis nostrud exercitation ullamco laboris 
                                nisi ut aliquip ex ea commodo consequat. Duis aute 
                                irure dolor in reprehenderit in voluptate velit esse 
                                cillum dolore eu fugiat nulla pariatur. Excepteur sint 
                                occaecat cupidatat non proident, sunt in culpa qui officia 
                                deserunt mollit anim id est laborum."""
                        ),
                    width="20em",
                    direction="column"
                    ),
                    rx.flex(
                        rx.heading("1"),
                        rx.heading("PRUEBA"),
                        rx.text("""Lorem ipsum dolor sit amet, consectetur 
                                adipiscing elit, sed do eiusmod tempor incididunt 
                                ut labore et dolore magna aliqua. Ut enim ad minim 
                                veniam, quis nostrud exercitation ullamco laboris 
                                nisi ut aliquip ex ea commodo consequat. Duis aute 
                                irure dolor in reprehenderit in voluptate velit esse 
                                cillum dolore eu fugiat nulla pariatur. Excepteur sint 
                                occaecat cupidatat non proident, sunt in culpa qui officia 
                                deserunt mollit anim id est laborum."""
                        ),
                    width="20em",
                    direction="column"
                    ),
                direction="row",
                wrap="wrap",
                max_width="45em",
                width="100%",
                spacing="9",
                justify="center",
                align="center"
                ),
            padding="2em",
            max_width="50em",
            wrap="wrap",
            spacing="9"
            ),


        top="10em",
        position="relative",
        align="center",
        spacing="9",
        justify="center",
        direction="column",
        
        ),


        rx.flex(
            rx.heading("""Nuestra visión es convertirnos en la pastelería de tortas 
                    artesanales y personalizadas de preferencia en Cali.""",
                    style={"font-size":"clamp(2rem, 1.5vw + 1.8rem, 1.8rem)"}
            ),
            rx.text("""
                    Queremos ser conocidos por nuestra calidad, creatividad con 
                    pasteles y el uso de ingredientes saludables y locales. Queremos 
                    construir una familia de adictos a los pasteles que entiendan 
                    la vida en la que reina el dulzor de la vida y la dulzura del amor.""",
                    style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}    
            ),
            direction="column",
            id="vision",
            padding_top="13em",
            width="auto",
            max_width="50em",
            wrap="wrap",
            spacing="3",
            padding_left="2em",
            padding_right="2em",

        ),

        rx.flex(
            rx.heading("""En Blondie’s Cakes, nuestra misión es proporcionar 
                    experiencias dulces y personalizadas""",
                    style={"font-size":"clamp(2rem, 1.5vw + 1.8rem, 1.8rem)"}
            ),
            rx.text("""
                    Usamos solo los mejores ingredientes, frescos y de temporada, 
                    junto con técnicas de la vieja escuela y un toque moderno, 
                    para crear trabajos de arte sabor específicos. 
                    Aquí en Blondie’s Cakes, nos enorgullecemos de la belleza 
                    que se disfruta a través de nuestros productos. Ya sea para 
                    ocasiones especiales, profesionales o simplemente disfrutando 
                    una ocasión única, parece que Blondie’s Cakes fue hecha para 
                    engendrar emociones y recuerdos duraderos.""",
                    style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}    
            ),
            direction="column",
            id="mision",
            padding_top="3em",
            width="auto",
            max_width="50em",
            wrap="wrap",
            spacing="3",
            padding_left="2em",
            padding_right="2em",

        ),


        rx.vstack(
                rx.heading("ENVIOS A TODA CALI",padding_top="2em"),
                rx.flex(
                    rx.image(src="/nosotros/delivery.svg",width="35em",heigth="auto"),
                    rx.flex(
                        rx.text("• Garantizamos una entrega segura y a tiempo."),
                        rx.text("• Utilizamos empaques especiales para garantizar que llegue a tu hogar en perfectas condiciones."),
                        rx.text("• Te ofrecemos opciones de entrega flexibles."),
                        rx.text("• Contáctanos y te brindaremos toda la información que necesitas para hacer tu pedido."),
                        width="20em",
                        max_width="35em",
                        direction="column",
                        spacing="5"
                    ),
                    
                    justify="center",
                    align="center",
                    direction="row",
                    wrap="wrap",
                    padding_bottom="2em"
                ),
            height="auto",
            width="100%",
            background_color="pink",
            justify="center",
            align="center",
            id="envios"
        ),


        rx.flex(
                rx.box(
                    rx.heading("contactanos",
                        position="sticky",
                        color=st.ColorPalette.ENFASIS.value,
                        style={"font-size":"clamp(1rem, 0.5vw + 2.8rem, 3.5rem)"}
                    ),
                    
                ),
                rx.text(f"Llámanos a nuestro teléfono ",rx.link("12345678",href="tel: +5712345678"), " o"),
                rx.card(
                    rx.vstack(    
                        rx.chakra.avatar(
                            size="xl"
                        ),
                        rx.text("escríbenos a nuestro WhatsApp!"),
                        rx.text_area(
                                    size="3",
                                    placeholder="escribe tu mensaje",
                                    on_blur=SendWatsAppMessage.update_message,
                                    on_change=SendWatsAppMessage.update_message,
                                    on_focus=SendWatsAppMessage.update_message
                        ),
                        rx.button("enviar whatsapp",on_click=SendWatsAppMessage.send_message),
                    
                        style={
                            "background-color":"transparent",
                        },
                    justify="center",
                    align="center",
                ),
                title="contacto",
                size="5",
                variant="surface",
                padding="5em"
            ),
            position="relative",
            margin_top="10em",
            padding="1em",
            margin_bottom="5em",
            direction="column",
            justify="center",
            align="center",
            spacing="6",
            id="contacto"
        ),


        rx.flex(
            rx.box(class_name="shape1"),
            rx.box(class_name="shape2"),
            position="absolute",
            z_index="-1",
            style={"filter":"blur(100px)"}
        ),

        rx.flex(
            rx.box(class_name="shape2"),
            rx.box(class_name="shape1"),
            position="absolute",
            top="40em",
            z_index="-1",
            style={"filter":"blur(100px)"}
        ),

        rx.box(
            footer(),
            width="100%"
        ),
        
        align="center",
        spacing="9",
        style={"overflow":"hidden"}
    )
