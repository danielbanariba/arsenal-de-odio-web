import reflex as rx
from arsenal_de_odio_web.styles.styles import Size, Color
import arsenal_de_odio_web.styles.styles as styles

def mercaderia() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.center(
                rx.text(
                "Mercaderia",    
                ),
                rx.image(
                    src="img/camisa_ejemplo.png",
                    width="10%",
                    height="auto",
                ),
                rx.image(
                    src="img/cd.png",
                    width="10%",
                    height="auto",
                ),
            ),
        ),
        bg_img="img/arsenal_blanc_negro.jpg",
        bg_position = "top",
        bg_repeat = "no-repeat",
        bg_attachment = "fixed",
        bg_size = "cover",
        width="100%",
    )