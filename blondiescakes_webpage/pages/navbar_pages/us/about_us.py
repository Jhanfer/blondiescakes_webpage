import reflex as rx
from blondiescakes_webpage.components.navbar.navbar import navbar


class Test(rx.State):
    path:str

    def generar_zigzag(self, amplitud, frecuencia, longitud, offset_x=700):
        path = f'M {offset_x},0'
        for i in range(1, longitud + 1):
            x = (i % 2) * frecuencia + offset_x
            y = i * amplitud
            path += f' L {x},{y}'
        #print(path)
        self.path = path



@rx.page(
    route="/nosotros"
)

def us() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(    
            class_name="container",
            width="100%",
            height="112em",
            top="5em",
            on_mount=Test.generar_zigzag(100,200,30),
            style={"clip-path": f"path('{Test.path}')",

            }
        ),
    )
