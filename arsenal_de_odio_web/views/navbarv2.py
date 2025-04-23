import reflex as rx 
from arsenal_de_odio_web.styles.styles import MAX_WIDTH, Size, Color
from arsenal_de_odio_web.components.link_icons import link, linkv2
import arsenal_de_odio_web.url as url
from arsenal_de_odio_web.components.icons import iconv2

class DrawerState(rx.State):
    is_open: bool = False

    def toggle_drawer(self):
        self.is_open = not self.is_open

def drawer_content():
    return rx.drawer.content(
        rx.flex(
            rx.drawer.close(
                iconv2(
                    "close",
                    Size.BIG.value,
                    Color.PRIMARY.value,
                    "0 0 512 512"
                )
            ),
            rx.vstack(
                linkv2(
                    url.MUSICA,
                    "MUSICA",
                    "right"
                ),
                link(
                    url.FACEBOOK,
                    "VIDEOS",
                    "right"  
                ),
                linkv2(
                    url.MERCADERIA,
                    "MERCADERIA",
                    "right"
                ),
                spacing=Size.DEFAULT_SPACING.value,
                width="100%",
                padding="1em",
            ),
            align_items="start",
            direction="column",
        ),
        height="100%",
        width="20em",
        padding="2em",
        background_color="rgba(0, 0, 0, 0.9)",
    )

def navbarv2() -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.link(
                iconv2(
                    "bars",
                    Size.BIG.value,
                    Color.PRIMARY.value,
                    "0 0 512 512"
                ),
                on_click=DrawerState.toggle_drawer,
            )
        ),
        rx.drawer.overlay(),
        rx.drawer.portal(drawer_content()),
        open=DrawerState.is_open,
        direction="right",
    )