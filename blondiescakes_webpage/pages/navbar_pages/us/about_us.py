import reflex as rx
from blondiescakes_webpage.components.navbar.navbar import navbar
from blondiescakes_webpage.views.index_body.footer.footer import footer
from blondiescakes_webpage.styles import styles as st
import re
from blondiescakes_webpage.styles import constants as ct
from blondiescakes_webpage.utils import utils as ut
from blondiescakes_webpage.components.about_us_components.about_us_component import about_us, AboutUsComponent
from blondiescakes_webpage.components.about_us_components.pros_component import pros, ProsData
from blondiescakes_webpage.components.about_us_components.purposes_component import purposes, PurposesData

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
    on_load=[AboutUsComponent.get_data, ProsData.get_pros_data, PurposesData.get_purpose_data]

)

def us() -> rx.Component:
    return rx.vstack(
        ut.lang(),
        navbar(),
        about_us(),
        pros(),
        purposes(),
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
