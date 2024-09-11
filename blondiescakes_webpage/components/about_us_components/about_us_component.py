import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import get_about_us


class AboutUsComponent(rx.State):
    title:str
    sub_title:str
    sumary:str
    image_url:str
    second_title:str
    second_sumary:str

    async def get_data(self):
        data = await get_about_us()
        self.title = data[0][0].title
        self.sub_title = data[0][0].sub_title
        self.sumary = data[0][0].sumary
        self.image_url = data[0][0].image_url
        self.second_title = data[1][0].title
        self.second_sumary = data[1][0].sumary



def about_us() -> rx.Component:
    return rx.cond(AboutUsComponent.image_url,
            rx.flex(
                rx.heading(AboutUsComponent.title,position="relative",style={"font-size":"clamp(1.875rem, 1.301rem + 2.449vw, 3.95rem)"}),
                rx.flex( 
                    rx.box(    
                        rx.image(
                                src=AboutUsComponent.image_url,
                                width="clamp(1rem, 9vw + 20rem, 30rem)",
                                height="auto",
                                class_name="image-container",
                                alt="Foto de Joselyn, fundadora de Blondie´s Cake sosteniendo su logo"
                        ),
                        class_name="container-image"
                    ),
                    rx.vstack(
                        rx.heading(AboutUsComponent.sub_title,
                                style={"font-size":"clamp(2rem, 1.5vw + 1.8rem, 1.8rem)"}
                        ),
                        rx.text(AboutUsComponent.sumary,
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
                    rx.heading(
                        AboutUsComponent.second_title,
                        style={"font-size":"clamp(2rem, 1.5vw + 1.8rem, 1.8rem)"}
                    ),
                    rx.text(
                        AboutUsComponent.second_sumary,
                        style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}

                    ),
                width="auto",
                max_width="50em",
                padding="2em"
                ),
                

            top="10em",
            position="relative",
            align="center",
            spacing="9",
            justify="center",
            direction="column",
            on_mount=AboutUsComponent.get_data
            )
    )