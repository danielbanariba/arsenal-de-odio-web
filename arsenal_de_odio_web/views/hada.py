import reflex as rx
from arsenal_de_odio_web.styles.styles import MAX_WIDTH, Size, Color

def hada () -> rx.Component:
    return rx.box(
        rx.html(
        '''
            <head>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
                <style>
                    @keyframes shakeXY {
                        0% { transform: translate(0, 0) rotate(0); }
                        20% { transform: translate(-30px, 0) rotate(-8deg); }
                        40% { transform: translate(30px, 0) rotate(8deg); }
                        60% { transform: translate(-30px, 0) rotate(-8deg); }
                        80% { transform: translate(30px, 0) rotate(8deg); }
                        100% { transform: translate(0, 0) rotate(0); }
                    }

                    @keyframes heartBeat {
                        0% { transform: scale(1); }
                        14% { transform: scale(1.3); }
                        28% { transform: scale(1); }
                        42% { transform: scale(1.3); }
                        70% { transform: scale(1); }
                    }
                    
                    #myImageContainer {
                        overflow: hidden;
                    }

                    #myImage {
                        height: auto;
                        width: 100%;
                        animation: shakeXY 1.5s infinite;
                        overflow: hidden;
                    }
                    /*
                    #myImage:hover {
                        animation: shakeXY 2s infinite, heartBeat 1s infinite;
                    }
                    */
                </style>
            </head>
            <body>
                <div id="myImageContainer">
                    <img id="myImage" class="animate__animated animate__pulse animate__infinite" src="img/el_hada_de_las_birrias.png" alt="My Image">
                </div>
            </body>
        '''
        ),
        center_content=True,
    )
