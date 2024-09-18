import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updaters_states.about_us_updater import AboutUsUpdater

## About Us Updater ##
def update_about_us(*,button_text:str, title:str, sub_title:str, sumary:str, image_url:str, second_text_title:str, second_text_sumary:str):
    return rx.dialog.root(
            rx.dialog.trigger(rx.button(button_text,background_color="#75D516",color="#000000")),
            rx.dialog.content(
                
                rx.vstack(
                        rx.heading("Edición del destacado"),
                    align="center",
                    padding_bottom="3em"),

                rx.vstack(
                        rx.flex(
                            rx.text("Titulo de página"),
                            rx.input(
                                placeholder="titulo",
                                on_blur=AboutUsUpdater.set_title,
                                on_change=AboutUsUpdater.set_title,
                                on_focus=AboutUsUpdater.set_title,
                                value=title
                            ),
                            width="100%",
                            justify="between"
                        ),

                        rx.flex(
                            rx.text("Subtítulo"),
                            rx.input(
                                placeholder="subtitulo",
                                on_blur=AboutUsUpdater.set_sub_title,
                                on_change=AboutUsUpdater.set_sub_title,
                                on_focus=AboutUsUpdater.set_sub_title,
                                value=sub_title
                            ),
                            width="100%",
                            justify="between"
                        ),
                        
                        rx.flex(
                            rx.text("Descripción del destacado"),
                            rx.text_area(
                                placeholder="descripción",
                                on_blur=AboutUsUpdater.set_sumary,
                                on_change=AboutUsUpdater.set_sumary,
                                on_focus=AboutUsUpdater.set_sumary,
                                value=sumary,
                                size="3"
                            ),
                            width="100%",
                            justify="between"
                        ),

                        rx.flex(
                            rx.text("URL de la imagen(URL directa)"),
                            rx.input(
                                placeholder="url de imagen",
                                on_blur=AboutUsUpdater.set_image,
                                on_change=AboutUsUpdater.set_image,
                                on_focus=AboutUsUpdater.set_image,
                                value=image_url,
                                
                            ),
                            width="100%",
                            justify="between",
                        ),

                        rx.flex(
                            rx.text("Preview de imagen"),
                            rx.image(
                                src=AboutUsUpdater.image_url,
                                width="10em"
                            ),
                            width="100%",
                            justify="between",
                        ),

                        rx.flex(
                            rx.text("Segundo titulo"),
                            rx.input(
                                placeholder="segundo titulo",
                                on_blur=AboutUsUpdater.set_second_title,
                                on_change=AboutUsUpdater.set_second_title,
                                on_focus=AboutUsUpdater.set_second_title,
                                value=second_text_title
                            ),
                            width="100%",
                            justify="between"
                        ),

                        rx.flex(
                            rx.text("Descripción del segundo titulo"),
                            rx.text_area(
                                placeholder="descripción del segundo titulo",
                                on_blur=AboutUsUpdater.set_second_sumary,
                                on_change=AboutUsUpdater.set_second_sumary,
                                on_focus=AboutUsUpdater.set_second_sumary,
                                value=second_text_sumary,
                                size="3"
                            ),
                            width="100%",
                            justify="between"
                        ),

                        rx.button("SUBIR",color_scheme="grass",on_click=AboutUsUpdater.update_data),
                    align="start",
                    spacing="5",
                    justify="center",
                    width="100%",
                    padding_bottom="3em",
                    ),
                    
                    rx.vstack(
                            rx.dialog.close(
                                rx.button("cerrar",size="3",color_scheme="tomato",on_click=AboutUsUpdater.set_none_data)),
                        align="center"
                    ),
            )
    )