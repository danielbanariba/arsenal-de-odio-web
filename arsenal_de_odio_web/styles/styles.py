from enum import Enum
import reflex as rx
from .colors import TextColor, Color
from .fonts import Font, FontWeight

# Ancho maximo de la pagina web
MAX_WIDTH = "1000px"


class Size(Enum): # Tamanno de las imagenes
    # Para propiedades spacing en componentes HStack/VStack (valores de 0-9)
    ZERO = "0"
    SMALL_SPACING = "1"
    MEDIUM_SPACING = "2"
    DEFAULT_SPACING = "3"
    LARGE_SPACING = "4"
    BIG_SPACING = "5"
    
    # Para propiedades CSS que necesitan valores con unidades
    ZERO_PX = "0px !important"
    VERY_SMALL = "0.2em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    PEQUENIO = "1.2em"
    LARGE = "1.5em"
    GRANDELOGO = "1.7em"
    BIG = "1.9em"
    MUY_BIG = "2.5em"
    PLATAFORMAS = "3em"
    VERY_BIG = "4em"
    GIGANTE = "8em"

#Hojas de estilos
STYLESHEETS = [
    # "fonts/fonts.css", # Ir al archvivo fonts.py para ver las fuentes
    # TODO hacer una animacion con la imagen del hada de las birrias, Link de la pagina: https://animejs.com/documentation/#functionBasedPropVal 
    # TODO Y las funciones que mas me gustaron fueron: FUNCTION BASED VALUES
    "styles/grain.css",
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": "bold",
    "color": TextColor.PRIMARY.value,
    "background_color": Color.PRIMARY.value,
    # No permite que se repita la imagen
    rx.heading: {# ? rx.<propiedad> Nos permite modificar cada propiedad en nuestro componente
        "font_family": Font.DEFAULT.value,
        "color": TextColor.PRIMARY.value,
    },
    rx.link: {# Desaparece el subrayado de los links
        "text_decoration": "none",
        "_hover": {
            "color": TextColor.SECONDARY.value,
        },
    }
}

FONDO_BACKGROUND_PRIMARIO = {
    "background_image": 'url("img/arsenal_portada.jpg")',
    "background_position": "top",
    "background_repeat": "no-repeat",
    "background_attachment": "fixed",
    "background_size": "cover",
}

FONDO_BACKGROUND_SECUNDARIO = {
    "background_image": 'url("img/arsenal_blanc_negro.jpg")',
    "background_position": "top",
    "background_repeat": "no-repeat",
    "background_attachment": "fixed",
    "background_size": "cover",
}

logo_canal = dict(
    font_family=Font.LOGO_CANAL.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.GRANDELOGO.value,
)

max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH,
)

producto_style = dict(
    _hover={
        "transform": "scale(1.1) rotate(10deg)",
        "transition": "transform 0.2s",
    },
),