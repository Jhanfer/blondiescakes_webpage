import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import get_highlight_data
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.supabase_database import Highlights
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updater_components.update_highlight_gui import updater_highlight

class IndexHighLight(rx.State):

        highlight_data:list[Highlights]
        title:str
        description:str
        image_url:str
        switch:bool

        async def get_data(self):
                highlight_data = await get_highlight_data()
                self.title = highlight_data[0].title
                self.description = highlight_data[0].description
                self.image_url = highlight_data[0].image_url
                self.switch = highlight_data[0].switch


def highlight() -> rx.Component:
        return rx.cond(
                IndexHighLight.switch,
                rx.flex(
                                rx.flex(
                                        rx.image(
                                                src="/body/decoration.svg",
                                                width="20em",
                                                #height="10em",
                                                id="productos",
                                                alt="Decoración en forma de ramas y corazón"
                                        ),
                                        top="110em"
                                ),
                                motion(
                                        rx.flex(
                                                rx.vstack(
                                                        rx.text(
                                                                IndexHighLight.title,
                                                                style={
                                                                        "line-height":"0.9em",
                                                                        "font-size":"clamp(3rem, 3.5vw + 1.8rem, 3.8rem)",
                                                                        "--line-height":"var(--heading-line-height-9)",
                                                                        "font-family":"pertili",
                                                                        "align":"center",
                                                                        "justify_content":"center",
                                                                        "text-align":"-webkit-center"
                                                                },
                                                                position="relative"
                                                        ),
                                                
                                                        rx.text(IndexHighLight.description,
                                                                style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}
                                                        ),
                                                        max_width="35em",
                                                        padding="1em",
                                                        spacing="8"
                                                ),

                                                rx.image(
                                                        src=IndexHighLight.image_url,
                                                        width="35em",
                                                        height="auto",
                                                        alt="Pastel de cumpleaños"
                                                ),

                                                width="100%",
                                                spacing="9",
                                                wrap="wrap",
                                                padding_top="1em",
                                                padding_bottom="5em",
                                                padding_left="1em",
                                                padding_right="1em",
                                                direction="row",
                                                justify="center",
                                                align="center",
                                ),
                                initial={"opacity": 0, "scale": 0.5},
                                animate={"opacity": 1, "scale": 1},
                                transition={"duration": 0.2,"ease":"easeOut"},
                                style={"display":"inline-block"}
                        ),
                justify="center",
                align="center",
                direction="column"
                )
        )





def highlight_backend() -> rx.Component:
        return rx.card(
                rx.cond(
                IndexHighLight.switch,
                        rx.flex(
                                rx.vstack(
                                        rx.text(
                                                IndexHighLight.title,
                                                position="relative",
                                                size="5"
                                        ),
                                
                                        rx.text(IndexHighLight.description,
                                                position="relative",
                                                size="5"
                                        ),

                                        max_width="35em",
                                        padding="1em",
                                        spacing="8"
                                ),

                                rx.image(
                                        src=IndexHighLight.image_url,
                                        width="20em",
                                        height="auto",
                                        alt="Pastel de cumpleaños"
                                ),

                                width="100%",
                                spacing="9",
                                wrap="wrap",
                                padding_top="1em",
                                padding_bottom="5em",
                                padding_left="1em",
                                padding_right="1em",
                                direction="row",
                                justify="center",
                                align="center",
                        ),
                ),
                updater_highlight(button_text="actualizar", published_title=IndexHighLight.title, published_description=IndexHighLight.description, published_img_url=IndexHighLight.image_url)
        )



