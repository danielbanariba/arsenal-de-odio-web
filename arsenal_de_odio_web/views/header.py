import reflex as rx 
from arsenal_de_odio_web.styles.styles import MAX_WIDTH, Size, Color
import arsenal_de_odio_web.url as url
import arsenal_de_odio_web.styles.styles as styles
from arsenal_de_odio_web.components.icons import icon
import arsenal_de_odio_web.styles.const as view
from arsenal_de_odio_web.components.spotify import reproductor_spotify
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
            padding_bottom=Size.ZERO_PX.value,
            padding_top=Size.VERY_SMALL.value,
        ),
        rx.flex(
            rx.vstack(
                rx.image(
                    src="img/portada.jpg",
                    alt="Arsenal de Odio - Muerte en el Mosh",
                    width="100%", #16em
                    heigh="100%",
                    box_shadow = "7px 7px 10px rgba(0, 0, 0, 0.9)",#sombra
                ),
                padding_bottom=Size.BIG.value,
                padding_x=Size.DEFAULT.value,
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
                padding_x=Size.VERY_BIG.value,
            ),
            align_items="center",
            flex_direction=["column", "column", "column", "row", "row"], #Responsive
        ),
        padding_top=Size.VERY_SMALL.value,
        width="100%",
        max_width=MAX_WIDTH,
    ),
    # rx.vstack(
    #     rx.spacer(),
    #     reproductor_spotify(),
    #     #rx.script(src="js/spotify.js"),
    # ),
    align_items="center",
    id="musica",
)