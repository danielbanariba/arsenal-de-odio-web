import reflex as rx 
import arsenal_de_odio_web.styles.styles as styles
from arsenal_de_odio_web.styles.styles import FONDO_BACKGROUND_PRIMARIO
from arsenal_de_odio_web.styles.styles import Size
from arsenal_de_odio_web.views.mercaderia import mercaderia
from arsenal_de_odio_web.views.navbar import navbar
#from arsenal_de_odio_web.views.navbarv2 import navbarv2
from arsenal_de_odio_web.views.video import video
from arsenal_de_odio_web.views.header import header
from arsenal_de_odio_web.views.footer import footer
from arsenal_de_odio_web.views.integrantes import integrantes
from arsenal_de_odio_web.views.inicio import inicio
from arsenal_de_odio_web.views.grain import grain
from arsenal_de_odio_web.views.hada import hada
from arsenal_de_odio_web.views.hada_moved import hada_moved
from arsenal_de_odio_web.components.spotify import reproductor_spotify

combined_style = {**styles.BASE_STYLE}

def index() -> rx.Component:
    return rx.vstack(
                rx.script("document.documentElement.lang='es'"),
                #hada_moved(),
                navbar(),
                rx.center(
                    rx.vstack(
                        inicio(),
                        header(),
                        reproductor_spotify(),
                        max_width=styles.MAX_WIDTH,
                    ),
                ),
                hada(),
                mercaderia(),
                video(),
                integrantes(),
                footer(),
                grain(),
                spacing=Size.BIG.value,
            )
        

app = rx.App(
    stylesheets=styles.STYLESHEETS, # Carga las hojas de estilos
    style=combined_style,
    head_components=[
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-3YGHT3XJFS"),
        rx.script(
            """
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-3YGHT3XJFS');
            """
        ),
    ],
)

app.add_page(
    index,
    title="Arsenal de Odio",
    description="Arsenal de Odio es una banda de Trash Metal de la ciudad de Tegucigalpa, Honduras.",
)

app.compile()