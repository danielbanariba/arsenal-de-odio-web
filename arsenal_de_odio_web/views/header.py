import reflex as rx 
from arsenal_de_odio_web.styles.styles import Size, Color
#from arsenal_de_odio_web.components.link_icons import link_icon, link
import arsenal_de_odio_web.url as url
import arsenal_de_odio_web.styles.styles as styles

def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
                "MUERTE EN EL MOSH",
               size="lg",
               padding_bottom=Size.DEFAULT.value,
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
                rx.link(
                    "Escucha el disco!",
                    rx.image(
                        src="icons/spotify.svg",
                        alt="Logo de Spotify",
                        width=Size.DEFAULT.value,
                        height=Size.DEFAULT.value,
                    ),
                    href=url.SPOTIFY,
                     is_external=True
                ),
                align_items="start", # Hace todo el texto para la izquierda
            ),
            flex_direction=["column", "column", "column", "row", "row"], #Responsive
        ),
        padding_top=Size.VERY_BIG.value,
        style=styles.max_width_style,                              
    )