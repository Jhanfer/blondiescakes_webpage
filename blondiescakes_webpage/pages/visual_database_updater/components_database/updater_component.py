import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.Updater import BackendUpdater
#from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_database import SupabaseAPI


def updater(button_text:str):
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(button_text,background_color="#75D516",color="#000000")),
        rx.dialog.content(
            rx.vstack(
                    rx.heading("Creación de artículo"),
                align="center",
                padding_bottom="3em"),
        

            rx.vstack(
                    rx.flex(
                        rx.text("Título del artículo"),
                        rx.input(placeholder="titulo del artículo",on_blur=BackendUpdater.set_title),
                        width="100%",
                        justify="between"),
                    
                    rx.flex(
                        rx.text("Descripción del articulo"),
                        rx.input(placeholder="descripción",on_blur=BackendUpdater.set_item_description),
                        width="100%",
                        justify="between"),

                    rx.flex(
                        rx.text("URL de la imagen(URL directa)"),
                        rx.input(placeholder="url de imagen",on_blur=BackendUpdater.set_image_url),
                        width="100%",
                        justify="between"),

                    rx.flex(
                        rx.text("Categoría"),
                        rx.select(["Pagina principal","Buttercream","Frios","Saludables","Tradicionales"],
                                placeholder="seleccione categoría",
                                on_change=BackendUpdater.set_categorie
                        ),
                        width="100%",
                        justify="between"),

                    rx.button("SUBIR",color_scheme="grass",on_click=lambda:[BackendUpdater.update_data,BackendUpdater.refresh_page]),
                align="start",
                spacing="5",
                justify="center",
                width="100%",
                padding_bottom="3em",
                on_mount=BackendUpdater.refresh_state_refresh),
                
                rx.vstack(
                        rx.dialog.close(
                            rx.button("cerrar",size="3",color_scheme="tomato",on_click=BackendUpdater.reset_data)),
                    align="center"),
                )
        )
