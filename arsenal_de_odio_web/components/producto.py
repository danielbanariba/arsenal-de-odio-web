import reflex as rx
from arsenal_de_odio_web.styles.styles import Size, producto_style, Color
import arsenal_de_odio_web.url as URL

def producto (imagen: str, descripcion: str, precio: str) -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.link(
                rx.image(
                    src=imagen,
                    style=producto_style
                ),
                href=URL.WHATSAPP,
                is_external=True,   
            ),
        ),
        rx.center(
            rx.text(
                descripcion,
                font_size=Size.VERY_BIG.value,
            ),
        ),
        rx.center(
            rx.text(
                precio,
                font_size=Size.LARGE.value,
            ),
        ),
        color = Color.SECONDARY.value,
    )
        
        