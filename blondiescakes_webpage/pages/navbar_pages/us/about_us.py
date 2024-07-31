import reflex as rx
from blondiescakes_webpage.components.navbar.navbar import navbar
from blondiescakes_webpage.views.index_body.footer.footer import footer

class Test(rx.State):
    path:str

    def generar_zigzag(self, amplitud, frecuencia, longitud, offset_x=650):
        path = f'M {offset_x},0'
        for i in range(1, longitud + 1):
            x = (i % 2) * frecuencia + offset_x
            y = i * amplitud
            path += f' L {x},{y}'
        #print(path)
        self.path = path



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
        padding_bottom="10em",
        align="center",
        spacing="9",
        justify="center",
        direction="column",
        
        ),

        footer(),

        
        align="center",
        spacing="9",
        style={"overflow":"hidden"}
    )






"""
rx.flex(
                    rx.flex(


                        rx.flex(
                            rx.heading("1",size="8"),
                            rx.heading("Creo, diseño y horneo:", size="8"),
                            rx.text(""
                                    cada torta es una obra de arte única, hecha a 
                                    mano, y diseñada especialmente para usted. 
                                    Desde la primera idea hasta la última pincelada, 
                                    me involucro en la creación de cada pastel para 
                                    garantizar que su pastel sea perfecto."
                            ),
                        width="20em",
                        direction="column",
                        wrap="wrap",
                        ),

                        rx.flex(
                            rx.heading("2",size="8"),
                            rx.heading("Creo, diseño y horneo:", size="8"),
                            rx.text(""
                                    cada torta es una obra de arte única, hecha a 
                                    mano, y diseñada especialmente para usted. 
                                    Desde la primera idea hasta la última pincelada, 
                                    me involucro en la creación de cada pastel para 
                                    garantizar que su pastel sea perfecto."
                            ),
                        width="20em",
                        direction="column",
                        wrap="wrap",
                        ),
                    spacing="9",
                    wrap="wrap",
                    direction="row",
                    justify="center",
                    align="center",
                    width="100%"
                    ),

                    rx.hstack(
                        rx.vstack(
                            rx.heading("3",size="8"),
                            rx.heading("Creo, diseño y horneo:", size="8"),
                            rx.text(""
                                    cada torta es una obra de arte única, hecha a 
                                    mano, y diseñada especialmente para usted. 
                                    Desde la primera idea hasta la última pincelada, 
                                    me involucro en la creación de cada pastel para 
                                    garantizar que su pastel sea perfecto.""
                            ),
                        ),

                        rx.vstack(
                            rx.heading("4",size="8"),
                            rx.heading("Creo, diseño y horneo:", size="8"),
                            rx.text(""
                                    cada torta es una obra de arte única, hecha a 
                                    mano, y diseñada especialmente para usted. 
                                    Desde la primera idea hasta la última pincelada, 
                                    me involucro en la creación de cada pastel para 
                                    garantizar que su pastel sea perfecto.""
                            )
                        ),
                    spacing="9"
                    ),

                style={"border-radius":"10px"},
                wrap="wrap"
                
                ),
"""



""""

rx.vstack(
        navbar(),
        rx.vstack( 
            rx.box(
                    rx.heading("¿Quienes somos?", size="7"),
                    rx.text(""¡Hola! ¡Soy la chef y pastelera Joselyn de Blondie’s Cake!
                            Me encanta hacer tortas personalizadas que se ajusten a tu estilo
                            y el tema de tu evento. Desde tortas de cumpleaños temáticas hasta
                            tortas de bodas, ¡Lo hago todo! ¿Deseas una deliciosa torta cubierta
                            con buttercream y flores comestibles? ¡Llámame! ¿Quieres una clásica
                            torta de chocolate con un toque moderno? ¡También! ¡Envíame un mensaje
                            para convertir tu idea en una realidad azucarada! #cakes #cakeshop 
                            #blondiescake #weddingcake #birthdaycake"",

                            size="6"
                    ),
                position="relative",
                top="25em",
                left="4em",
                style={"display":"block",
                        #"margin-left":"auto",
                        "margin-right":"auto",
                        #"background-color":"white"
                },
                width="25em",
                height="20em"
            ),

            class_name="container",
            width="100%",
            height="100em",
            top="-5em",
            on_mount=Test.generar_zigzag(100,100,20),
            #style={"clip-path": f"path('{Test.path}')"}
            #style={"clip-path":"path('M 0,100 L 750,100 L 650,200 L 750,300 L 650,400 L 750,500 L 650,600 L 750,700 L 650,800 L 750,900 L 650,1000 L 750,1100 L 650,1200 L 750,1300 L 650,1400 L 750,1500 L 650,1600 L 750,1700 L 650,1800 L 750,1900 L 0,2000')"}
        ),
        rx.box(
            footer(),
            width="100%",
            top="95em",
            position="relative"
        ),
        spacing="0"
    
    )



"""


