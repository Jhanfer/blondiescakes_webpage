import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import get_purposes, Purposes
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updater_components.update_purposes_gui import update_purposes_gui
class PurposesData(rx.State):
    purpose_list:list[Purposes]

    async def get_purpose_data(self):
        self.purpose_list = await get_purposes()

def purposes() -> rx.Component:
    return rx.flex(
            rx.foreach(
                PurposesData.purpose_list,
                component_purposes
            ),
        on_mount=PurposesData.get_purpose_data,
        direction="column"
    )


def component_purposes(featured:Purposes) -> rx.Component:
    return rx.flex(
                rx.heading(
                    featured.title,
                    style={"font-size":"clamp(1.8rem, 1.5vw + 1.8rem, 1.8rem)"}
                ),
                rx.text(
                    featured.sumary,
                    style={"font-size":"clamp(1em, 1.5vw + 0.5em, 1.3em)"}    
                ),
            direction="column",
            id=featured.type,
            padding_top="8em",
            width="auto",
            max_width="50em",
            wrap="wrap",
            spacing="3",
            padding_left="2em",
            padding_right="2em",
    )

def purposes_backend_component() -> rx.Component:
    return rx.card(
            rx.vstack(
                rx.flex(
                        rx.foreach(
                            PurposesData.purpose_list,
                            component_purposes
                        ),
                    on_mount=PurposesData.get_purpose_data,
                    direction="column"
                ),

                update_purposes_gui("Actualizar", PurposesData.purpose_list)
            ),
            on_mount=PurposesData.get_purpose_data,
    )