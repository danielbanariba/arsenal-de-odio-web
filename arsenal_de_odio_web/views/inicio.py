import reflex as rx
from arsenal_de_odio_web.styles.styles import Size, Color
import arsenal_de_odio_web.styles.styles as styles

def inicio() -> rx.Component:
    return rx.vstack(#TODO estoy en duda si poner el inicio, es que no se xd 
        rx.hstack(
            rx.html(#La imagen no se pueda ni hacer zoom ni moverse
                '''
                    <style>
                        #image-container {
                            position: relative;
                            width: 100vw;
                            height: 100vh;
                        }
                        #background-image {
                            position: absolute;
                            top: 0;
                            left: 0;
                            width: 100%;
                            height: 100%;
                            object-fit: cover;
                            z-index: -1;
                        }
                    </style>
                    <div id="image-container">
                        <img id="background-image" src="img/arsenal_portada.jpg" alt="Background Image">
                    </div>
                ''')
        ),
    )