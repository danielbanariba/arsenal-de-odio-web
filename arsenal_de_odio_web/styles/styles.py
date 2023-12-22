from enum import Enum
import reflex as rx
from .fonts import Font
from .colors import TextColor, Color

# Yo no quiero que pases el tamanno mas de lo que esta escrito
MAX_WIDTH = "1000px"


class Size(Enum): # Tamanno de las imagenes
    SMALL = "0.5em"
    DEFAULT = "1em"
    BIG = "1.9em"
    MUY_BIG = "2.5em"
    VERY_BIG = "4em"

#Hojas de estilos
STYLESHEETS = [
    "fonts/fonts.css", # Ir al archvivo fonts.py para ver las fuentes
    # TODO hacer una animacion con la imagen del hada de las birrias, Link de la pagina: https://animejs.com/documentation/#functionBasedPropVal 
    # TODO Y las funciones que mas me gustaron fueron: FUNCTION BASED VALUES
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": "bold",
    "color": TextColor.PRIMARY.value,
    "background_color": Color.PRIMARY.value,
    "background_image": 'url("img/arsenal_portada.jpg")',
    "background_repeat": "no-repeat", # No permite que se repita la imagen
    rx.Link: {# Desaparece el subrayado de los links
        "text_decoration": "none",
        "_hover": {
            "color": TextColor.AMARILLO.value,
        },
    }
}

max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH,
)