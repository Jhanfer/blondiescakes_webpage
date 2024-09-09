import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.updaters_states.index_windows_updater import IndexWindowsUpdater

## Windows Updater Component ##
def updater_windows(*,button_text:str,published_title:str,published_description:str, all_data:list):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(button_text,background_color="#75D516",color="#000000"),
            ),
        rx.dialog.content(

            rx.vstack(
                    rx.heading("Edición de las Ventanas"),
                align="center",
                padding_bottom="3em"
            ),

            rx.vstack(
                    rx.cond(IndexWindowsUpdater.windows_image_url,
                        rx.flex(
                            rx.text("Imagen posteada"),
                            rx.image(
                                src=IndexWindowsUpdater.windows_image_url,
                                width="10em",
                                height="auto"
                            ),
                            align="center",
                            justify="center",
                            direction="column"
                        )
                    ),

                    rx.select(["Ventana 1","Ventana 2","Ventana 3","Ventana 4"],
                            placeholder="seleccione categoría",
                            on_change=[IndexWindowsUpdater.set_categorie],
                            on_mount=[IndexWindowsUpdater.get_all_data(all_data)]
                    ),

                    rx.cond(IndexWindowsUpdater.windows_id_1_cond,
                        rx.flex(
                            rx.text("Titulo del destacado"),
                            rx.input(
                                placeholder="titulo",
                                on_blur=IndexWindowsUpdater.set_title,
                                on_change=IndexWindowsUpdater.set_title,
                                on_focus=IndexWindowsUpdater.set_title,
                                value=published_title
                            ),
                            width="100%",
                            justify="between"
                        )
                    ),
                    
                    rx.cond(IndexWindowsUpdater.windows_id_1_cond,
                        rx.flex(
                            rx.text("Descripción del destacado"),
                            rx.text_area(
                                placeholder="descripción",
                                on_blur=IndexWindowsUpdater.set_description,
                                on_change=IndexWindowsUpdater.set_description,
                                on_focus=IndexWindowsUpdater.set_description,
                                value=published_description,
                                size="3"
                            ),
                            width="100%",
                            justify="between"
                        )
                    ),

                    rx.flex(
                        rx.text("Texto de imagen"),
                        rx.input(
                            placeholder="Texto",
                            on_blur=IndexWindowsUpdater.set_text,
                            on_change=IndexWindowsUpdater.set_text,
                            on_focus=IndexWindowsUpdater.set_text,
                            value=IndexWindowsUpdater.windows_text,
                            
                        ),
                            width="100%",
                            justify="between"
                    ),

                    rx.flex(
                        rx.text("URL de la imagen(URL directa)"),
                        rx.input(
                            placeholder="url de imagen",
                            on_blur=IndexWindowsUpdater.set_image_url,
                            on_change=IndexWindowsUpdater.set_image_url,
                            on_focus=IndexWindowsUpdater.set_image_url,
                            value=IndexWindowsUpdater.windows_image_url,
                            
                        ),
                        width="100%",
                        justify="between",
                        on_mount=[IndexWindowsUpdater.set_all(published_title, IndexWindowsUpdater.windows_image_url,published_description,IndexWindowsUpdater.windows_text)]
                    ),



                    rx.button("SUBIR",color_scheme="grass",on_click=lambda:[IndexWindowsUpdater.update_data]),
                align="start",
                spacing="6",
                justify="center",
                width="100%",
                padding_bottom="3em",
                
                ),
                
                rx.vstack(
                        rx.dialog.close(
                            rx.button("cerrar",size="3",color_scheme="tomato",on_click=IndexWindowsUpdater.reset_data)),
                    align="center"
                    ),

                )
        )
