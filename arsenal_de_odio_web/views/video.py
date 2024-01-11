import reflex as rx
from arsenal_de_odio_web.styles.styles import Size 

def video() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.html(#Oculta la barra horizontal de desplazamiento
                '''
                    <style>
                        body {
                            overflow-x: hidden;
                        }
                        #title-container {
                            position: relative;
                            width: 100vw;
                        }
                        #title-container h1 { 
                            font-size: 10vw;
                            text-align: center;
                            font-weight: 400;
                            color: white;      
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
                    </style>
                    <div id="title-container">
                        <video id="background-video" autoplay muted preload loop>
                            <source src="video/arsenal_video.mp4" type="video/mp4">
                        </video>
                        <h1>MUY PRONTO</h1>
                    </div>
                '''
            ),
            width="100%",
        ),
    )