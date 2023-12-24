import reflex as rx
from arsenal_de_odio_web.styles.styles import Size, Color
import arsenal_de_odio_web.styles.styles as styles

def inicio() -> rx.Component:
    return rx.vstack(#TODO estoy en duda si poner el inicio, es que no se xd 
        rx.hstack(
            rx.link(
                rx.audio(
                url="https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3",
                width="400px",
                height="auto",
            ),    
            ),
            
        ),
        bg_img="img/arsenal_portada.jpg",
        bg_position = "top",
        bg_repeat = "no-repeat",
        bg_attachment = "scroll",  # Cambia esto #TODO estoy indeciso si dejarlo asi o poner el fixed 
        bg_size = "cover",
        width="100%",
    )