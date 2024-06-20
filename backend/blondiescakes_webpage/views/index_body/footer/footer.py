import reflex as rx
from blondiescakes_webpage.styles import styles as st

def footer() -> rx.Component:
    return rx.hstack(

        rx.vstack(
            rx.image(src="/navbar/navbar.png",width="9em",height="5em"),
            rx.text("Página en construcción...",color=st.ColorPalette.ENFASIS.value,align="center"),
            rx.text("© BlondiesCake's - Todos los derechos reservados",color=st.ColorPalette.ENFASIS.value,align="center"),
            justify="center",
            align="center",
            width="100%",
            margin="1em"),

        bg=st.ColorPalette.MAIN.value,
        height="18em",
        position="relative",
        width="100%",
        z_index="9999",
        justify="center",
        align="center"
)