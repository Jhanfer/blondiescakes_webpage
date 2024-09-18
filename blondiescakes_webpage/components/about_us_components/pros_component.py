import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import get_pros, Purposes
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updater_components.update_pros_gui import update_pros_gui
class ProsData(rx.State):
    pros_list_item_1:list[Purposes]
    pros_list_item_2:list[Purposes]

    async def get_pros_data(self):
        data = await get_pros()
        self.pros_list_item_1 = [data[0],data[1]]
        self.pros_list_item_2 = [data[2],data[3]]

def pros() -> rx.Component:
    return  rx.flex(
                rx.flex(
                    rx.foreach(
                        ProsData.pros_list_item_1,
                        pros_paragraph
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
                    rx.foreach(
                        ProsData.pros_list_item_2,
                        pros_paragraph
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
            spacing="9",
            padding_top="15em",
            on_mount=ProsData.get_pros_data
            )


def pros_paragraph(featured:Purposes) -> rx.Component:
    return rx.flex(
                rx.heading(featured.title[0]),
                rx.heading(featured.title[1:]),
                rx.text(
                    featured.sumary
                ),
        width="20em",
        direction="column"
    )


def pros_backend() -> rx.Component:
    return rx.card(
        rx.flex(
                rx.flex(
                    rx.foreach(
                        ProsData.pros_list_item_1,
                        pros_paragraph
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
                    rx.foreach(
                        ProsData.pros_list_item_2,
                        pros_paragraph
                    ),

                direction="row",
                wrap="wrap",
                max_width="45em",
                width="100%",
                spacing="9",
                justify="center",
                align="center"
                ),

            update_pros_gui(button_text="Actualizar", pros_list_1=ProsData.pros_list_item_1, pros_list_2=ProsData.pros_list_item_2),

            padding="2em",
            max_width="50em",
            wrap="wrap",
            spacing="9",
            on_mount=ProsData.get_pros_data
        )
    )