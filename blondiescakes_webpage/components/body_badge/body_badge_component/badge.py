import reflex as rx 
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.wrapping_react.AwesomeSlider import carousel
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion
from blondiescakes_webpage.components.wrapping_react.RatingStars import rating_stars
import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import get_reviews_data_api
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.supabase_database import ReviewsBase
import reflex_chakra as ch

class BadgeReviews(rx.State):
    reviews_data:list[ReviewsBase]

    async def get_reviews_data(self):
        self.reviews_data = await get_reviews_data_api()




def badge() -> rx.Component:
    return rx.vstack(

            rx.text("Síguenos en instagram",
                    color=st.ColorPalette.MAIN.value,
                    position="absolute",
                    padding_bottom="10em",
                    size="9",
                    display=["none","none","none","none","flex"],
                    style={"font-family":"pertili"}
            ),

            rx.text("Síguenos en instagram",
                    color=st.ColorPalette.MAIN.value,
                    position="absolute",
                    padding_bottom="18em",
                    size="7",
                    display=["flex","flex","flex","flex","none"],
                    style={"font-family":"pertili"}
            ),
            
            rx.vstack(

                rx.flex(
                    rx.image(
                        src="body/badge/header2HD.jpeg",
                        position="absolute",
                        width="8em",
                        height="auto",
                        top="58em",
                        left="5em",
                        alt="Imagen decorativa de pastel de rosas",
                        style={
                            "border-radius":"100px 100px 100px 100px"
                        }
                    ),
                    display=["none","none","flex","flex","flex"]
                ),
                
                rx.flex(
                    rx.image(
                        src="body/badge/header3HD.jpeg",
                        position="absolute",
                        width="8em",
                        height="auto",
                        top="97em",
                        right="6em",
                        alt="Imagen decorativa de pastel de cumpleaños",
                        style={
                            "border-radius":"100px 100px 100px 100px"
                        }
                    ),
                    display=["none","none","flex","flex","flex"]
                ),

                carousel(
                        rx.card(
                                motion(
                                    rx.image(
                                        src="body/badge_carousel.jpeg",
                                        width="25em",
                                        height="auto",
                                        alt="Foto de Joselyn, fundadora de Blondie´s con una batidora",
                                        on_click=rx.redirect("https://www.instagram.com/p/C6y3SRtgcw3/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==")
                                    ),
                                while_hover={"scale":1.1},
                                while_tap={"scale":0.9},
                                transition={"type": "spring", "stiffness":300,"damping":20}
                                ),
                            size="5"
                        ),
                        rx.card(
                                motion(
                                    rx.image(
                                        src="body/badge_carousel2.jpeg",
                                        width="25em",
                                        height="auto",
                                        alt="Foto de Joselyn, fundadora de Blondie´s con el logo de la empresa",
                                        on_click=rx.redirect("https://www.instagram.com/p/C6owde_gA7a/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==")
                                    ),
                                while_hover={"scale":1.1},
                                while_tap={"scale":0.9},
                                transition={"type": "spring", "stiffness":300,"damping":20}    
                                ),
                            size="4"
                        ),
                        rx.card(
                                motion(
                                    rx.image(
                                        src="body/badge_carousel3.jpeg",
                                        width="25em",
                                        height="auto",
                                        alt="Foto eventos a los que ha id Blondie´s",
                                        on_click=rx.redirect("https://www.instagram.com/p/C1j5c2oAscv/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==")
                                    ),
                                while_hover={"scale":1.1},
                                while_tap={"scale":0.9},
                                transition={"type": "spring", "stiffness":300,"damping":20}
                                ),    
                            size="4"
                        ),
                    animation="fallAnimation",
                    mobile_touch=True,
                    bullets=False,
                    style={"width":"93%",
                            "--content-background-color":"transparent",
                            "--control-button-width":"30%",
                            "--slider-height-percentage":"94%",
                            "--organic-arrow-height":"40px",
                            "--organic-arrow-color":f"{st.ColorPalette.MAIN.value}"

                            }, 
                ),
                    
                width="100%",
                justify="center",
                align="center",
                padding_bottom="2em",
                style={"overflow":"hidden"}
            ),
            
            rx.text("No te olvides del dulce",
                    color=st.ColorPalette.MAIN.value,
                    position="absolute",
                    padding_top="10em",
                    size="9",
                    display=["none","none","none","none","flex"],
                    style={"font-family":"pertili"}
            ),

            rx.text("No te olvides del dulce",
                    color=st.ColorPalette.MAIN.value,
                    position="absolute",
                    padding_top="20em",
                    size="7",
                    display=["flex","flex","flex","flex","none"],
                    style={"font-family":"pertili"}
            ),

            justify="center",
            align="center",
            margin_bottom="3em",
            width="100%",
            bg=st.ColorPalette.ENFASIS.value,
            height="60em",
            z_index="10",
            padding_top="5em",
            on_mount=BadgeReviews.get_reviews_data
)


def review() -> rx.Component:
    return rx.hstack(
            rx.cond(BadgeReviews.reviews_data,
                rx.vstack(
                    rx.text(
                        "Reviews de Google Maps",
                        color=st.ColorPalette.MAIN.value,
                        size="8"
                    ),
                    rx.flex(
                        rx.grid(
                            rx.scroll_area(
                                rx.flex(
                                        rx.foreach(
                                            BadgeReviews.reviews_data,
                                            card
                                        ),
                                    spacing="4"
                                ),
                            scrollbars="horizontal",
                            type="always"
                        ),
                        padding="1em"),
                    ),

                    justify="center",
                    align="center"
                ),
            ),

            justify="center",
            align="center",
            margin_bottom="0em",
            width="100%",
            bg=st.ColorPalette.ENFASIS.value,
            height="40em",
            z_index="5",
)



def card(featured:ReviewsBase):
    return rx.card(
            rx.vstack(
                        rx.hstack(
                            ch.avatar(
                                size="xl",
                                src="featured",
                                name=featured.username
                            ),

                            rx.vstack(    
                                rx.text(
                                    featured.username,
                                    color=st.ColorPalette.ENFASIS.value,
                                    size="7"
                                ),

                                rx.hstack(
                                    rating_stars(
                                        value=featured.rating,
                                        read_only=True,
                                        radius="small",
                                        width="7em"
                                    ),

                                    rx.text(
                                        featured.date,
                                        color="gray",
                                        justify="center"
                                    ),
                                ),

                                justify="center",
                                align="start"
                            ),

                            align="center"
                        ),
                        
                        rx.text(
                            featured.description,
                            color=st.ColorPalette.ENFASIS.value,
                            justify="center",
                            style={
                                "font-size":"clamp(1em, 0.5vw + 0.5em, 1.3em)"
                            }
                        ),
                        

                        justify="between",
                        align="between",
                        
                    ),
        width="30em",
        height="15em",
        bg="white"
    )


