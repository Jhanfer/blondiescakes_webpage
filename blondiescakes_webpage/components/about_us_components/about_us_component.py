import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import get_about_us
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updater_components.update_about_us_gui import update_about_us

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

def skeleton(*,h:str,w:str) -> rx.Component:
    return rx.skeleton(rx.button("button-small"), height=h, width=w,loading=True,background_color="grey")

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
                                alt="Foto de Joselyn, fundadora de Blondie´s Cake"
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
            ),


            rx.flex(
                skeleton(h="4em",w="50em"),
                rx.hstack(
                    skeleton(h="16em",w="24em"),
                    rx.vstack(
                        skeleton(h="5em",w="33em"),
                        skeleton(h="10em",w="33em"),
                    ),
                ),
                skeleton(h="8em",w="33em"),
                skeleton(h="13em",w="33em"),
                rx.flex(
                        skeleton(h="8em",w="33em"),
                        skeleton(h="13em",w="33em"),
                    direction="row",
                    wrap="wrap",
                    max_width="45em",
                    width="100%",
                    spacing="9",
                    justify="center",
                    align="center"
                ),
                direction="column",
                padding_top="8em",
                spacing="4",
                justify="center",
                align="center"
            ),
            
    )


def about_us_component_backend():
    return  rx.card(
            rx.vstack(
                rx.heading(AboutUsComponent.title,position="relative",size="5"),
                rx.flex( 
                    rx.box(    
                        rx.image(
                                src=AboutUsComponent.image_url,
                                width="15em",
                                height="auto",
                                class_name="image-container",
                        ),
                        class_name="container-image"
                    ),
                    rx.vstack(
                        rx.heading(
                            AboutUsComponent.sub_title,
                            size="5"
                        ),
                        rx.text(
                            AboutUsComponent.sumary,
                            size="5"
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
                        size="5"
                    ),
                    rx.text(
                        AboutUsComponent.second_sumary,
                        size="5"

                    ),
                width="auto",
                max_width="50em",
                padding="2em"
                ),

                update_about_us(
                    button_text="Actualizar",
                    title=AboutUsComponent.title,
                    sub_title=AboutUsComponent.sub_title,
                    sumary=AboutUsComponent.sumary,
                    image_url=AboutUsComponent.image_url,
                    second_text_title=AboutUsComponent.second_title,
                    second_text_sumary=AboutUsComponent.second_sumary

                ),

                justify="center",
                align="center"
            ),
        on_mount=AboutUsComponent.get_data
    )