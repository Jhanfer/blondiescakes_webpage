import reflex as rx
from blondiescakes_webpage.components.navbar.navbar import navbar
from blondiescakes_webpage.views.index_body.footer.footer import footer
from blondiescakes_webpage.styles import styles as st
import re
from blondiescakes_webpage.styles import constants as ct
from blondiescakes_webpage.utils import utils as ut

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
    route=ut.ABOUTUS_ROUTE,
    title=ut.about_us_title,
    description=ut.about_us_description,
    meta=ut.about_us_meta,

)

def us() -> rx.Component:
    return rx.vstack(
        ut.lang(),
        navbar(),

        rx.flex(
            rx.heading("Detrás de los postres",position="relative",style={"font-size":"clamp(1.875rem, 1.301rem + 2.449vw, 3.95rem)"}),
            rx.flex( 
                rx.box(    
                    rx.image(
                            src="/body/badge_carousel2.jpeg",
                            width="clamp(1rem, 9vw + 20rem, 30rem)",
                            height="auto",
                            class_name="image-container",
                            alt="Foto de Joselyn, fundadora de Blondie´s Cake sosteniendo su logo"
                    ),
                    class_name="container-image"
                ),
                rx.vstack(
                    rx.heading("¡Hola! ¡Soy la chef y pastelera de Blondie’s Cake, Joselyn!",
                            style={"font-size":"clamp(2rem, 1.5vw + 1.8rem, 1.8rem)"}
                    ),
                    rx.text("""
                            Apesar de tener mas 8 años de experiencia en el sector,
                            Blondies nace en un momento de aislamiento social con sus
                            restricciones, la Pandemia del Covid 2019, tuve que
                            enfrentar muchas dificultades por falta de trabajo, debido a
                            que la empresa donde laboraba cerrò sus puertas, la falta
                            de movilidad entre otros obstáculos, me vi en la necesidad
                            de crear productos de pasteleria y reposterìa
                            personalizados, ofreciendo una gran variedad de opciones y
                            alternativas a mis clientes, creando asì una nueva demanda
                            en la modalidad virtual, mirando hacia el futuro con la
                            esperanza de crecer, de brindarle a nuestros clientes un
                            buen servicio, adaptàndonos a nuevos escenarios que
                            puedan surjir en el futuro.
                            """,
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
                rx.heading("""
                        ¿Qué mejor manera de celebrar un momento importante que 
                        con un pastel delicioso elaborado con maestría y cuidado?
                        """,
                        style={"font-size":"clamp(2rem, 1.5vw + 1.8rem, 1.8rem)"}
                ),
                rx.text(
                    """ 
                    En Blondies, nos adaptamos a los nuevos tiempos, ofreciendo 
                    nuestros servicios de manera virtual, pero siempre con la misma 
                    calidad y atención personalizada. Nuestro objetivo es crecer junto 
                    a ti, brindándote el mejor servicio y los pasteles más deliciosos 
                    para tus momentos especiales."
                    """,

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
                        rx.heading("Versatilidad en Eventos"),
                        rx.text("""
                                Ofrecemos una amplia gama de opciones para 
                                diversos tipos de eventos, incluyendo corporativos, 
                                cumpleaños, aniversarios y bodas. Nuestra flexibilidad 
                                nos permite adaptarnos a las necesidades específicas de cada cliente.
                                """
                        ),
                    width="20em",
                    direction="column"
                    ),
                    rx.flex(
                        rx.heading("2"),
                        rx.heading("Descuentos por Volumen"),
                        rx.text("""
                                Premiamos la confianza de nuestros clientes ofreciendo 
                                descuentos adicionales en pedidos de mayor volumen. Además, 
                                brindamos opciones de personalización de productos para hacer 
                                cada orden única.
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
                        rx.heading("Compromiso Social"),
                        rx.text("""
                                Trabajamos en colaboración con la Fundación Gamaliel, 
                                canalizando parte de nuestros ingresos hacia causas benéficas. 
                                Con cada compra, nuestros clientes contribuyen indirectamente
                                a esta labor social.
                                """
                        ),
                    width="20em",
                    direction="column"
                    ),
                    rx.flex(
                        rx.heading("4"),
                        rx.heading("Apoyo Comunitario"),
                        rx.text("""
                                Nuestro compromiso se extiende a diversas comunidades locales. 
                                Distribuimos almuerzos, productos de limpieza y artículos de aseo 
                                personal a ancianatos, refugios caninos y hogares infantiles de la 
                                ciudad, acompañando estas donaciones con palabras de aliento y apoyo.
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
                    Posicionarnos en 10 años como una empresa
                    comercializadora de productos arteanales de primera calidad
                    en Cali, comprometidos con nuestra comunidad llevàndoles
                    dìa a dìa experiencias ùnicas que deleiten todos sus sentidos
                    en cada una de sus celebraciones.
                    """,
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
                    Crear una experiencia gastronòmica memorable a traves de
                    nuestros productos de pastelerìa y reposterìa horneados y
                    frescos de manera artesanal brindando una experiencia ùnica
                    y agradable a nuestros clientes.
                    """,
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
                        position="relative",
                        alt="Imagen de un repartidor en moto"
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
                        rx.text("escríbenos a nuestro WhatsApp!",color=st.ColorPalette.MAIN.value),
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
