import reflex as rx 
from arsenal_de_odio_web.styles.styles import MAX_WIDTH, Size, Color
import arsenal_de_odio_web.url as url
import arsenal_de_odio_web.styles.styles as styles
from arsenal_de_odio_web.components.icons import icon
import arsenal_de_odio_web.styles.const as view
from arsenal_de_odio_web.components.spotify import reproductor_spotify
from arsenal_de_odio_web.effects.background_noise import background_noise
from arsenal_de_odio_web.components.list_song import list_song

def header() -> rx.Component:
    return rx.vstack(
    rx.vstack(
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
            rx.vstack(
                rx.image(
                    src="img/portada.jpg",
                    alt="Arsenal de Odio - Muerte en el Mosh",
                    width="100%", #16em
                    heigh="100%",
                    box_shadow = "7px 7px 10px rgba(0, 0, 0, 0.9)"#sombra
                ),  
            ),
            rx.vstack(
                list_song(),
                rx.center(
                    rx.hstack(
                        icon(url.SPOTIFY, "spotify", Size.PLATAFORMAS.value, Color.SECONDARY.value, view.viewBox_0),
                        icon(url.YOUTUBE_MUSIC, "youtube_music", Size.PLATAFORMAS.value, Color.SECONDARY.value, view.viewBox),
                        icon(url.APPLE_MUSIC, "apple_music", Size.PLATAFORMAS.value, Color.SECONDARY.value, view.viewBox),
                        icon(url.DEEZER, "deezer", Size.PLATAFORMAS.value, Color.SECONDARY.value, view.viewBox),  
                    ),
                ),
            ),
            align_items="center",
            flex_direction=["column", "column", "column", "row", "row"], #Responsive
        ),
        padding_top=Size.VERY_SMALL.value,
        padding_x=Size.BIG.value,
        width="100%",
        max_width=MAX_WIDTH,                       
    ),
    rx.vstack(
        rx.text(
            "Escucha el disco!"
        ),
        reproductor_spotify(),  
        ),
    align_items="start",
    )