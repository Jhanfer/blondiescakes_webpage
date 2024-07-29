import reflex as rx 
import re
from blondiescakes_webpage.views.index_body.footer.footer  import footer
from blondiescakes_webpage.components.navbar.navbar import navbar
from blondiescakes_webpage.styles import styles as st

class Blur(rx.State):
    blur:str = "blur(2px)"
    def sum_blur(self):
        self.blur = "blur(4px)"
    def res_blur(self):
        self.blur = "blur(2px)"


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
    route="/contactanos",
    title="Contacto | Blondie's Cakes",
    description="Página de contacto",

)

def contact_page() -> rx.Component: 
    return rx.vstack(
        navbar(),
        rx.vstack(
            width="100%",
            position="absolute",
            class_name="header",
            style={"filter": Blur.blur,
                "overflow":"hidden"}
        ),

        rx.image(src="/navbar/Logotipo-blondies-uso redes.png",
                position="sticky",
                width="18em",
                height="18em",
                border_radius="100em 100em",
                #left="10em",
                top="6em",
                style={"display":"block",
                        "margin":"auto"
                }
        ),

        rx.box(
            rx.heading("contactanos",
                position="sticky",
                color=st.ColorPalette.ENFASIS.value,
                style={"font-size":"3.2em"}
            ),
        top="11em",
        left="1em",
        position="relative",
        ),

        rx.box(
                rx.card(
                    rx.vstack(    
                        rx.chakra.avatar(
                            size="xl"
                        ),

                        rx.text("Llamanos a nuestro teléfono o"),
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
                    padding_left="1em",
                    padding_right="1em"
                ),
                title="contacto",
                size="5",
                variant="surface",
                on_mouse_enter=Blur.sum_blur,
                on_mouse_leave=Blur.res_blur,
            ),
            position="relative",
            top="12em",
            padding="1em",
            margin_bottom="15em",
        ),

        footer(), 
        justify="between",
        spacing="0",
        style={"overflow":"hidden"}

    )


"""
Fondo rosa pastel claro (hexadecimal: #FFC0CB):

Negro: #000000
Marron oscuro: #333333
Azul marino: #000080
Verde oscuro: #298A48
Fondo blanco crema (hexadecimal: #F5F5DC):

Negro: #000000
Marron oscuro: #422000
Azul marino: #000080
Verde oscuro: #336910
Fondo marrón claro (hexadecimal: #E9D6B7):

Negro: #000000
Marron oscuro: #654327
Azul marino: #003380
Verde oscuro: #4C5100

"""


"""
1. Colores metálicos:

Dorado: #FFD700 (brillo y elegancia)
Plateado: #C0C0C0 (sofisticación y neutralidad)
Cobre: #B87333 (calidez y contraste)
2. Colores vibrantes:

Fucsia: #FF00FF (energía y contraste)
Turquesa: #00FFFF (frescura y realce)
Naranja: #FFA500 (alegría y dinamismo)
3. Colores pastel con sombra:

Rosa pastel con sombra negra: #FFC0CB con sombra #000000 (legibilidad y contraste)
Azul pastel con sombra marrón oscuro: #E6E6FA con sombra #422000 (delicadeza y profundidad)
Verde pastel con sombra gris oscuro: #D3D3D3 con sombra #696969 (armonía y equilibrio)

"""