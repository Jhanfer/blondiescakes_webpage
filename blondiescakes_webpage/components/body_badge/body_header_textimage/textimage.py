import reflex as rx
from blondiescakes_webpage.styles import styles as st
from typing import Optional
from blondiescakes_webpage.components.wrapping_react.framer_motion import motion


def textimage(image:str,text:str,color:Optional[str]=st.ColorPalette.ENFASIS.value,size:Optional[str]="6") -> rx.Component:
        return rx.box(
                rx.text(text,
                        size=size,
                        color=color,
                        align="center",
                        justify="center",
                        position="absolute"),

                rx.image(
                        src=image,
                        width="18em",
                        height="auto",
                        position="relative",
                        object_fit="cover"),
                align="center",
                justify="center"
        )


def textimage_header(image:str,text:str,color:Optional[str]=st.ColorPalette.ENFASIS.value,size:Optional[str]="6") -> rx.Component:
        return rx.vstack(
                rx.vstack(
                        motion(        
                                        rx.flex(
                                                rx.text("Regala",
                                                        size=size,
                                                        color=color,
                                                        position="relative",
                                                ),
                                        ),
                                initial={"opacity":0.5,"x":100},
                                animate={"opacity":1,"x":0},
                                tansition={"delay":10,"type":"spring","duration":3,"stiffness": 260, "damping": 0,"ease":"linear"}
                        ),
                        
                        motion(
                                        rx.flex(
                                                rx.text("Amor,",
                                                        size=size,
                                                        color=color,
                                                ),
                                        ),
                                initial={"opacity":0.5,"x":100},
                                animate={"opacity":1,"x":0},
                                tansition={"delay":0.3,"type":"keyframes","duration":1,"stiffness": 260, "damping": 0}
                        ),

                        motion(
                                        rx.flex(
                                                rx.text("Regala",
                                                        size=size,
                                                        color=color,
                                                ),
                                        ),
                                initial={"opacity":0.5,"x":100},
                                animate={"opacity":1,"x":0},
                                tansition={"delay":0.3,"type":"keyframes","duration":1,"stiffness": 260, "damping": 0}
                        ),

                        motion(
                                        rx.flex(
                                                rx.text("Dulce.",
                                                        size=size,
                                                        color=color,
                                                ),
                                        ),
                                initial={"opacity":0.5,"x":100},
                                animate={"opacity":1,"x":0},
                                tansition={"delay":1,"type":"keyframes","duration":1,"stiffness": 260, "damping": 0}
                        ),
                align="center",
                justify="center",
                position="absolute",
                z_index="100",
                top="-5em"
                ),

                motion(
                                rx.flex(
                                        rx.image(
                                                src=image,
                                                width="22em",
                                                max_width="28em",
                                                height="auto",
                                                position="relative",
                                                border_radius="15px 50px",
                                                object_fit="cover",
                                                top="3em",
                                                style={"opacity":"0.7"}
                                        ),
                                ),
                        initial={"opacity":0,"y":100},
                        animate={"opacity":1,"y":0},
                        transition={"delay":0.1,"type":"keyframes","duration":1,"stiffness": 260, "damping": 0}
                ),
                align="center",
                justify="center"
        )



