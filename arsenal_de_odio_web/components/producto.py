import reflex as rx
from arsenal_de_odio_web.styles.styles import MAX_WIDTH, Size, Color, producto_style
import arsenal_de_odio_web.url as URL

# Tengo que actualizar el componente de la card para la nueva version de reflex
def producto (imagen: str, descripcion: str, precio: int) -> rx.Component:
    return rx.card(
        rx.image(#TODO poner el link del vendedor
            src=imagen, 
            _hover={
                "transform": "scale(1.1) rotate(10deg)",
                "transition": "transform 0.2s",
            },
        ),
        rx.text(
            descripcion, 
            color=Color.PRIMARY.value, 
            font_size=Size.BIG.value,
            align_items="center"
        ),
        rx.heading(precio, size="3"),
        align_items="center",
        bg="rgba(38, 35, 53, 0.7)",
        box_shadow = "7px 7px 10px rgba(0, 0, 0, 0.9)",
    )