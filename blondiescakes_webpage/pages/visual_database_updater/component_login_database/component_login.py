import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_state.LoginState import LoginState



def login_component() -> rx.Component:
    return rx.card(
            rx.vstack(
                rx.center(
                    rx.heading(
                        "Ingresa con usuario",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "DIRECCIÓN EMAIL",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        placeholder="user@email.com",
                        type="email",
                        size="3",
                        width="100%",
                        on_blur=LoginState.get_username,
                        on_focus=LoginState.get_username,
                        on_change=LoginState.get_username
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "contraseña",
                            size="3",
                            weight="medium",
                        ),
                        justify="between",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        placeholder="ponga su contraseña",
                        type="password",
                        size="3",
                        width="100%",
                        on_blur=LoginState.get_password,
                        on_focus=LoginState.get_password,
                        on_change=LoginState.get_password
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.button("Sign in", size="3", width="100%",on_click=[LoginState.auth_user]),
                
                spacing="6",
                width="100%",
            ),
            max_width="28em",
            size="4",
            width="100%",
        )