import reflex as rx 
import arsenal_de_odio_web.styles.styles as styles
from arsenal_de_odio_web.styles.styles import FONDO_BACKGROUND_PRIMARIO
from arsenal_de_odio_web.views.mercaderia import mercaderia
from arsenal_de_odio_web.views.navbar import navbar
from arsenal_de_odio_web.styles.styles import Size
from arsenal_de_odio_web.views.video import video
from arsenal_de_odio_web.views.header import header
from arsenal_de_odio_web.views.footer import footer
from arsenal_de_odio_web.views.integrantes import integrantes
from arsenal_de_odio_web.views.inicio import inicio
from arsenal_de_odio_web.effects.background_noise import background_noise

combined_style = {**styles.BASE_STYLE}

def index() -> rx.Component:
    return rx.vstack(
                navbar(),
                # rx.vstack(
                #     background_noise(),    
                # ),
                rx.center(
                    rx.vstack(
                        inicio(),
                        header(),
                        max_width=styles.MAX_WIDTH,
                    ),
                ),
                mercaderia(),
                video(),
                integrantes(),
                footer(),
                width="100%",
                spacing=Size.BIG.value,
            )
        

app = rx.App(
    stylesheets=styles.STYLESHEETS, # Carga las hojas de estilos
    style=combined_style,
)

app.add_page(
    index,
    title="Arsenal de Odio",
    description="Arsenal de Odio es una banda de trash metal de la ciudad de tegucigalpa, Honduras.",
)

app.compile()