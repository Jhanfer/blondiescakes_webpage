import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.Updater import BackendUpdater
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_database import SupabaseAPI


def updater():
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("crear nuevo artículo",background_color="#75D516",color="#000000")),
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
                        rx.text("URL de la imagen(URL directa)"),
                        rx.input(placeholder="url de imagen",on_blur=BackendUpdater.set_image_url),
                        width="100%",
                        justify="between"),
                        
                    rx.flex(
                        rx.text("URL de whatsapp"),
                        rx.input(placeholder="url de compra",on_blur=BackendUpdater.set_url_purchase),
                        width="100%",
                        justify="between"),

                    rx.button("SUBIR",on_click=lambda:[BackendUpdater.update_data,BackendUpdater.refresh_page]),

                align="start",
                spacing="5",
                justify="center",
                width="100%",
                padding_bottom="3em",
                on_mount=BackendUpdater.refresh_state_refresh),
                
                rx.vstack(
                        rx.dialog.close(
                            rx.button("cerrar", size="3",on_click=BackendUpdater.reset_data)),
                    align="center"),
                )
        )

