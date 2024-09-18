import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updaters_states.purposes_updater import PurposesUpdater
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import Purposes

## Purposes Updater ##
def update_purposes_gui(button_text:str, purposes_list:list[Purposes]):
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(button_text,background_color="#75D516",color="#000000")),
        rx.dialog.content(
            
            rx.vstack(
                    rx.heading("Edición del destacado"),
                align="center",
                padding_bottom="3em"),

            rx.vstack(
                    rx.heading("Visión"),
                    rx.flex(
                        rx.text("Titulo visión"),
                        rx.input(
                            placeholder="titulo",
                            on_blur=PurposesUpdater.set_vision_title,
                            on_change=PurposesUpdater.set_vision_title,
                            on_focus=PurposesUpdater.set_vision_title,
                            value=purposes_list[0].title
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("Descripción de visión"),
                        rx.text_area(
                            placeholder="descripción",
                            on_blur=PurposesUpdater.set_vision_sumary,
                            on_change=PurposesUpdater.set_vision_sumary,
                            on_focus=PurposesUpdater.set_vision_sumary,
                            size="3",
                            value=purposes_list[0].sumary,
                            resize="vertical"
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.heading("Misión"),
                    rx.flex(
                        rx.text("Titulo misión"),
                        rx.input(
                            placeholder="titulo",
                            on_blur=PurposesUpdater.set_mision_title,
                            on_change=PurposesUpdater.set_mision_title,
                            on_focus=PurposesUpdater.set_mision_title,
                            value=purposes_list[1].title
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("Descripción de misión"),
                        rx.text_area(
                            placeholder="descripción",
                            on_blur=PurposesUpdater.set_mision_sumary,
                            on_change=PurposesUpdater.set_mision_sumary,
                            on_focus=PurposesUpdater.set_mision_sumary,
                            size="3",
                            value=purposes_list[1].sumary,
                            resize="vertical"
                        ),
                        width="100%",
                        justify="between"
                    ),


                    rx.button("SUBIR",color_scheme="grass",on_click=PurposesUpdater.update_data),
                align="start",
                spacing="5",
                justify="center",
                width="100%",
                padding_bottom="3em",
                ),
                
                rx.vstack(
                        rx.dialog.close(
                            rx.button("cerrar",size="3",color_scheme="tomato",on_click=PurposesUpdater.set_none_data)),
                    align="center"),
                )
        )