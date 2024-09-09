from reflex.components.component import Component
from typing import Any, Dict, List, Union, Callable, Literal
from reflex.vars import Var
import reflex as rx

literal_radius_vars = Literal["none","small","medium","large","full"]

class MaterialRatingStars(Component):
    library = "@smastrom/react-rating"
    tag = "Rating"

    value:Var[Union[int,str]]
    read_only:Var[bool]
    radius:Var[literal_radius_vars]

    def add_imports(self):
        return {"": ["@smastrom/react-rating/style.css"]}

rating_stars = MaterialRatingStars.create

