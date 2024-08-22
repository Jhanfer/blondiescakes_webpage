import reflex as rx 
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.body_badge.body_badge_component.badge import badge,review
from blondiescakes_webpage.components.body_products_items.products_container import products_container

def body() -> rx.Component:
    return rx.box(
            badge(),
            products_container(),
            review(),
            rx.flex(
                    rx.vstack(
                            rx.icon(tag="wheat",color=st.ColorPalette.LINES.value),
                            rx.heading("Nuestra esencia",
                                    color=st.ColorPalette.ENFASIS.value,
                                    style={"font-size":"clamp(1rem, 0.5vw + 2.1rem, 3.5rem)"}
                            ),
                            rx.text(
                                    """
                                    En Blondies sabemos que regalar Amor es Regalar Dulce, es saber
                                    atesorar los momentos compartidos entre familiares y
                                    amigos,entendemos que cada pastel significa una gran ocasiòn, por
                                    eso trabajamos con ingredientes de excelente calidad de forma
                                    artesanal, nuestras recetas basadas en nuestra cultura y
                                    aprendizaje de la pastelerìa francesa han sido versionadas para
                                    cada gusto, estamos comprometidos para brindarte un servicio de
                                    calidad siendo empàticos, con disposicòn y creatividad para que
                                    tengas la mejor experiencia en tus eventos familiares y reuniones
                                    corporativas.
                                    """,
                                    color=st.ColorPalette.ENFASIS.value,
                                    style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}
                            ),

                            rx.text(
                                """
                                Desde nuestras propuestas como tortas, brownies, galletas,
                                cupcakes, hasta las tartas, y la gran variedad de postres, cada uno
                                esta elaborado con pasiòn colocando la calidad siempre por
                                delante, nos honra ofrecerles una experiencia diferente, por eso
                                tratamos de personalizar cada propuesta para que te sientas a
                                gusto.
                                """,
                                color=st.ColorPalette.ENFASIS.value,
                                style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}
                            ),

                            rx.text(
                                """
                                En Blondies no solo nos dedicamos a vender dulces, apostamos a
                                una comunidad alegre, consciente y unida con sus seres queridos,
                                hacièndonos partìcipes de sus celebraciones, te invitamos a
                                conoceros, y endulces tu vida con nuestras propuestas únicas.
                                """,
                                color=st.ColorPalette.ENFASIS.value,
                                style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}
                            ),

                            rx.icon(tag="cherry",color=st.ColorPalette.LINES.value),
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
                padding_bottom=st.Size.MEDIUM.value
            ),
        
        direction="column",
        width="100%",
        align="center"
    )