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

combined_style = {**styles.BASE_STYLE}

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                mercaderia(),
                integrantes(),
                footer(),
                width="100%",
                spacing=Size.BIG.value,
            )
        )
        
        # rx.center(
        #     rx.vstack(
        #         rx.video(
        #             url="https://www.youtube.com/watch?v=0ikIVI6oLNI",
        #             width="auto",
        #             height="auto",
        #         ),
        #         width="100%",
        #     ),  
        # ),
        #rx.html('<video autoplay muted loop> <source src="arsenal_video.mp4" type="video/mp4"> Your browser does not support the video tag.</video>')
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