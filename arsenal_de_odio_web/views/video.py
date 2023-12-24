import reflex as rx
from arsenal_de_odio_web.styles.styles import Size 

def video() -> rx.Component:
    return rx.vstack(#TODO hacer que el video vaya de punta apunta en la pantalla
        rx.hstack(
                rx.html(#TODO investicar como verga hacer que solo salga el video
                    '''
                        <style>
                            #title-container {
                                position: relative;
                                width: 100%;
                            }
                            #background-video {
                                position: absolute;
                                top: 0;
                                left: 0;
                                width: 100%;
                                height: 100%;
                                object-fit: cover;
                                z-index: -1;
                            }
                            h1 { 
                                background-color: rgba(0, 0, 0, 1);  /* Añade transparencia al fondo del título */
                                font-size: 10vw;
                                text-align: center;
                                font-weight: 400;
                                mix-blend-mode: multiply;
                                padding-left: auto;
                                padding-right: auto;
                                width: 100%;
                                
                            }
                        </style>
                        <div id="title-container">
                            <video id="background-video" autoplay muted preload loop>
                                <source src="video/arsenal_video.mp4" type="video/mp4">
                            </video>
                            <h1>🍻MUY PRONTO🍺</h1>
                        </div>
                    '''
                ),
                margin_left = "auto",
                margin_right = "auto",
            ),
        )