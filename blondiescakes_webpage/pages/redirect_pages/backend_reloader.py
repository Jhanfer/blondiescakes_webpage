import reflex as rx

@rx.page(
    route="/database_updater/redirect",
    title="Database",
    on_load=rx.redirect("/database_updater/")
)

def redirect():
    return rx.flex()