import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updaters_states.pros_updater import ProsUpdater
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import Purposes

## Pros Updater ##
def update_pros_gui(*,button_text:str, pros_list_1:list[Purposes], pros_list_2:list[Purposes]):
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(button_text,background_color="#75D516",color="#000000")),
        rx.dialog.content(
            
            rx.vstack(
                    rx.heading("Edición del destacado"),
                align="center",
                padding_bottom="3em"),

            rx.vstack(
                    rx.flex(
                        rx.text("Titulo item 1"),
                        rx.input(
                            placeholder="titulo",
                            on_blur=ProsUpdater.set_title_1,
                            on_change=ProsUpdater.set_title_1,
                            on_focus=ProsUpdater.set_title_1,
                            value=pros_list_1[0].title
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("Descripción item 1"),
                        rx.text_area(
                            placeholder="descripción",
                            on_blur=ProsUpdater.set_sumary_1,
                            on_change=ProsUpdater.set_sumary_1,
                            on_focus=ProsUpdater.set_sumary_1,
                            size="3",
                            value=pros_list_1[0].sumary,
                            resize="vertical"
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("Titulo item 2"),
                        rx.input(
                            placeholder="titulo",
                            on_blur=ProsUpdater.set_title_2,
                            on_change=ProsUpdater.set_title_2,
                            on_focus=ProsUpdater.set_title_2,
                            value=pros_list_1[1].title
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("Descripción item 2"),
                        rx.text_area(
                            placeholder="descripción",
                            on_blur=ProsUpdater.set_sumary_2,
                            on_change=ProsUpdater.set_sumary_2,
                            on_focus=ProsUpdater.set_sumary_2,
                            size="3",
                            value=pros_list_1[1].sumary,
                            resize="vertical"
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("Titulo item 3"),
                        rx.input(
                            placeholder="titulo",
                            on_blur=ProsUpdater.set_title_3,
                            on_change=ProsUpdater.set_title_3,
                            on_focus=ProsUpdater.set_title_3,
                            value=pros_list_2[0].title
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("Descripción item 3"),
                        rx.text_area(
                            placeholder="descripción",
                            on_blur=ProsUpdater.set_sumary_3,
                            on_change=ProsUpdater.set_sumary_3,
                            on_focus=ProsUpdater.set_sumary_3,
                            size="3",
                            value=pros_list_2[0].sumary,
                            resize="vertical"
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("Titulo item 4"),
                        rx.input(
                            placeholder="titulo",
                            on_blur=ProsUpdater.set_title_4,
                            on_change=ProsUpdater.set_title_4,
                            on_focus=ProsUpdater.set_title_4,
                            value=pros_list_2[1].title
                        ),
                        width="100%",
                        justify="between"
                    ),

                    rx.flex(
                        rx.text("Descripción item 4"),
                        rx.text_area(
                            placeholder="descripción",
                            on_blur=ProsUpdater.set_sumary_4,
                            on_change=ProsUpdater.set_sumary_4,
                            on_focus=ProsUpdater.set_sumary_4,
                            size="3",
                            value=pros_list_2[1].sumary,
                            resize="vertical"
                        ),
                        width="100%",
                        justify="between"
                    ),


                    rx.button("SUBIR",color_scheme="grass",on_click=ProsUpdater.update_data),
                align="start",
                spacing="5",
                justify="center",
                width="100%",
                padding_bottom="3em",
                ),
                
                rx.vstack(
                        rx.dialog.close(
                            rx.button("cerrar",size="3",color_scheme="tomato",on_click=ProsUpdater.set_none_data)),
                    align="center"),
                )
        )