import reflex as rx
from blondiescakes_webpage.components.navbar.navbar import navbar
from blondiescakes_webpage.views.index_body.footer.footer import footer
from blondiescakes_webpage.styles import styles as st
import re
from blondiescakes_webpage.styles import constants as ct


class SendWatsAppMessage(rx.State):
    message:str
    def send_message(self):
        if not len(self.message) == 0:
            message = f"https://wa.me/{ct.CONTACT_NUMBER}?text={re.sub(r'(\S)\s+(\S)', r'\1%20\2', self.message.strip())}"
            print(message)
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
                        rx.heading("Diseño personalizado"),
                        rx.text("""
                                Soy una arquitecta de sabores. Hago tus cosas y diseño 
                                tartas, tan deliciosas como bellos. Desde el primer bocado
                                de tela hasta tu último aliento gracias al último toque de 
                                glaseado, tu torta será un trabajo de arte delicioso.
                                """
                        ),
                    width="20em",
                    direction="column"
                    ),
                    rx.flex(
                        rx.heading("2"),
                        rx.heading("Colaboración"),
                        rx.text("""
                                Trabajamos mano a mano para crear tortas que enamoren 
                                todos tus sentidos. Tu visión, mi pasión, juntos creamos 
                                momentos dulces para recordar. Cada bocado es una experiencia 
                                única, diseñada para deleitar tu paladar y sorprender a tus invitados.
                                """
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
                        rx.heading("3"),
                        rx.heading("Ingredientes naturales"),
                        rx.text("""
                                Mis pasteles son más que simples postres; son una oda 
                                a los ingredientes frescos y de temporada. Cada mordisco 
                                es un viaje por los sabores más genuinos, solo utilizo 
                                productos frescos y de la mejor calidad. Ya sean frutas 
                                jugosas o nueces crujientes, cada ingrediente se elige 
                                con esmero para proporcionar una experiencia eterna.
                                """
                        ),
                    width="20em",
                    direction="column"
                    ),
                    rx.flex(
                        rx.heading("4"),
                        rx.heading("Innovación"),
                        rx.text("""
                                Estoy constantemente innovando e intentando nuevas 
                                formas de impresionar y encantar a mis clientes. 
                                Me encanta probar con nuevos sabores y técnicas para 
                                destacarme con tortas únicas e inolvidables. 
                                Desde variantes modernas de sabores clásicos núcleo 
                                y corteza, a rellenos exóticos y texturas completamente 
                                innovadoras.
                                """
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
                    style={"font-size":"clamp(1.8rem, 1.5vw + 1.8rem, 1.8rem)"}
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
                    style={"font-size":"clamp(1.8rem, 1.5vw + 1.8rem, 1.8rem)"}
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
                    rx.image(
                        src="/nosotros/delivery.svg",
                        width="28em",
                        heigth="auto",
                        position="relative"
                    ),

                    #Mobile
                    rx.flex(
                            rx.text("""• Garantizamos una entrega segura y a tiempo.""",
                                    position="relative",
                                    
                            ),
                            
                            rx.text("""• Utilizamos empaques especiales para garantizar 
                                    que llegue a tu hogar en perfectas condiciones.""",
                                    position="relative",
                                    
                            ),
                            rx.text("• Te ofrecemos opciones de entrega flexibles.",
                                    position="relative",
                                    
                            ),
                            
                            rx.text("""• Contáctanos y te brindaremos toda la 
                                    información que necesitas para hacer tu pedido.""",
                                    position="relative",
                                    
                            ),
                        width="20em",
                        max_width="35em",
                        direction="column",
                        spacing="5",
                        display=["flex", "flex", "none", "none", "none"]
                    ),
                    
                    #Desktop
                    rx.flex(
                            rx.text("""• Garantizamos una entrega segura y a tiempo.""",
                                    position="relative",
                                    left="-10em"
                            ),
                            
                            rx.text("""• Utilizamos empaques especiales para garantizar 
                                    que llegue a tu hogar en perfectas condiciones.""",
                                    position="relative",
                                    left="-6em"
                            ),
                            rx.text("• Te ofrecemos opciones de entrega flexibles.",
                                    position="relative",
                                    left="-5em"
                            ),
                            
                            rx.text("""• Contáctanos y te brindaremos toda la 
                                    información que necesitas para hacer tu pedido.""",
                                    position="relative",
                                    left="-3em"
                            ),
                        width="20em",
                        max_width="35em",
                        direction="column",
                        spacing="5",
                        display=["none", "none", "flex", "flex", "flex"],
                    ),


                    justify="center",
                    align="center",
                    direction="row",
                    wrap="wrap",
                    padding_bottom="2em"
                ),
            height="auto",
            width="100%",
            background_color="#D1C3B2",
            justify="center",
            align="center",
            id="envios"
        ),


        rx.flex(
                rx.vstack(
                    rx.heading("¿Te apetece algo?",
                        color=st.ColorPalette.ENFASIS.value,
                        style={"font-size":"clamp(1rem, 0.5vw + 2.1rem, 3.5rem)"},
                        
                    ),

                    rx.text("""¡Escríbenos! Haremos realidad tu pastel de ensueño. 
                            Personalizamos cada creación para que sea única y especial""",
                            style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}
                    ),
                    
                    #width="50%",
                    spacing="4",
                    id="contacto",
                    justify="center",
                    align="center",
                    padding_top="3em",
                    width="auto",
                    max_width="30em",
                    wrap="wrap",
                ),

                
                rx.text(f"Llámanos a nuestro teléfono ",rx.link(ct.CONTACT_NUMBER,href=f"tel: {ct.CONTACT_NUMBER}"), " o"),
                rx.card(
                    rx.vstack(    
                        rx.chakra.avatar(
                            size="2xl"
                        ),
                        rx.text("escríbenos a nuestro WhatsApp!"),
                        rx.text_area(
                                    size="3",
                                    placeholder="escribe tu mensaje",
                                    on_blur=SendWatsAppMessage.update_message,
                                    on_change=SendWatsAppMessage.update_message,
                                    on_focus=SendWatsAppMessage.update_message,
                                    color_scheme="gray"
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
                variant="classic",
                padding="5em",
                background_color=st.ColorPalette.ENFASIS.value,
                
            ),
            position="relative",
            padding="1em",
            margin_bottom="5em",
            direction="column",
            justify="center",
            align="center",
            spacing="5",
            
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
