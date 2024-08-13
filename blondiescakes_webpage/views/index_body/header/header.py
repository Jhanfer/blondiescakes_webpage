import reflex as rx
from blondiescakes_webpage.styles import styles as st
from blondiescakes_webpage.components.body_badge.body_header_textimage.textimage import textimage_header
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion


def header() -> rx.Component:
    return rx.flex(
                    rx.hstack(
                            rx.spacer(),
                            motion(
                                    motion(
                                        rx.flex(
                                            rx.image(src="/header/back.svg",width="15em",height="auto"),
                                            rx.text("PASTELERÍA A LA CARTA",
                                                    color=st.ColorPalette.ENFASIS.value,
                                                    padding_left="1.7em",
                                                    padding_top="2em",
                                                    position="absolute"
                                            ),
                                            on_click=rx.redirect("/#productos")
                                        ),
                                        while_hover={"scale":1.1},
                                        while_tap={"scale":0.9},
                                        transition={"type": "spring", "stiffness":300,"damping":20}
                                    ),
                                initial={"opacity":0,"x":-50},
                                animate={"opacity":1,"x":0},
                                transition={"delay":0.1,"type":"keyframes","duration":1,"stiffness": 260, "damping": 0}
                            ),
                        padding_bottom="5em",
                        justify="between",
                        spacing="9",
                        display="flex",
                        position="relative",
                        z_index="5",
                        width="100%",
                        align="center",  
                    ),

            rx.hstack(     
                
                    rx.flex(
                        blondies_link("20em"),
                        display=["none", "none", "flex", "flex", "flex"],
                        z_index="101",
                        position="absolute",
                        top="20em",
                        #top="30em",
                        left="-2em",
                        #left="1em",
                        justify="center",
                        align_items="center",
                        spacing="4",
                        class_name="vertical-text",
                    ), 
                    rx.flex(
                        blondies_link("15em"),
                        display=["none", "flex", "none", "none", "none"],
                        z_index="101",
                        position="absolute",
                        top="15em",
                        #top="30em",
                        left="-2em",
                        #left="1em",
                        justify="center",
                        align_items="center",
                        spacing="4",
                        class_name="vertical-text",
                    ), 

                    textimage_header("header/123.jpg","Regala amor, regala dulce",size="9"),
                spacing="9",
                width="100%",
                align="center",
                display="flex",
                position="relative",
                justify="center",
                z_index="5"
            ),

        
        align="center",
        justify="between",
        #height="25em",
        padding_top="8em",
        width="100%",
        spacing="5",
        direction="column",
        #padding_bottom="10em",
        

    )


def blondies_link(top:str) -> rx.Component:
    return  rx.flex(
                motion(
                    motion(
                            rx.link(
                                    rx.text("@BLONDIES_CAKE",
                                        color=st.ColorPalette.ENFASIS.value,
                                        position="relative",
                                        size="3",
                                        align="center",
                                    ),
                                href="https://www.instagram.com/blondies_cake/"
                            ),
                            rx.icon(
                                tag="instagram",
                                position="relative",
                                width="1.09em",
                                height="1.09em",
                                color=st.ColorPalette.ENFASIS.value,
                                top="-1.39em",
                                left="10em"
                            ),
                        
                            while_hover={"scale":1.1},
                            while_tap={"scale":0.8},
                            transition={"type":"spring","stiffness":260,"damping":10}
                        ),
                        
                        rx.divider(background=st.ColorPalette.LINES.value,decorative=True, position="absolute",padding_left="20em", top="0.5em",left="12em",size="4",style={"height":"0.2em"}),
                        
                        initial={"opacity":0,"y":-50},
                        animate={"opacity":1,"y":0},
                        transition={"delay":0.1,"type":"keyframes","duration":1,"stiffness": 260, "damping": 0}
                    ),
            )