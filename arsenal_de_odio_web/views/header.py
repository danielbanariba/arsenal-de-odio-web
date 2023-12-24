import reflex as rx 
from arsenal_de_odio_web.styles.styles import MAX_WIDTH, Size, Color
#from arsenal_de_odio_web.components.link_icons import link_icon, link
import arsenal_de_odio_web.url as url
import arsenal_de_odio_web.styles.styles as styles
from arsenal_de_odio_web.components.icons import icon

def header() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.text(
                "MUSICA",    
            ),
            font_size=Size.VERY_BIG.value,
            color = Color.SECONDARY.value,
            padding_bottom=Size.ZERO.value,
            padding_top=Size.VERY_SMALL.value,
        ),
        rx.flex(
            rx.image(
                src="img/portada.jpg",
                alt="Arsenal de Odio - Muerte en el Mosh",
                width="50%", #16em
                heigh="50%"
            ),
            rx.vstack(
                rx.span(
                    "Aqui va a ir una descripcion del album de la banda, y todo lo que se va a tratar del disco"
                ),
                rx.span(
                    "Mas detalles del disco como el año de lanzamiento, el genero, etc."
                ),
                rx.span(
                    "Y aqui va a ir la lista de canciones del disco"
                ),
                rx.box(#TODO no me da al poner el icono de spotify, mas grande  
                    icon(
                        url.SPOTIFY,
                        "spotify",
                    ),
                    _hover={"color": "#ffc435"},
                ),
                align_items="start",# Hace todo el texto para la izquierda
                margin_left=Size.DEFAULT.value,
            ),
            flex_direction=["column", "column", "column", "row", "row"], #Responsive
        ),
        padding_top=Size.VERY_SMALL.value,
        padding_x=Size.BIG.value,
        width="100%",
        max_width=MAX_WIDTH,                       
    )