import reflex as rx
from arsenal_de_odio_web.styles.styles import Size 

def background_noise() -> rx.Component:
    return rx.html(
                '''
                    <style>
                        .bg-color-noise {
                            background-color: #111111;
                            margin: 0;
                            overflow-x: hidden;
                        }
                        .noise {
                            position: fixed;
                            top: -50%;
                            left: -50%;
                            right: -50%;
                            bottom: -50%;
                            width: 200%;
                            height: 200vh;
                            background: transparent url('http://assets.iceable.com/img/noise-transparent.png') repeat 0 0;
                            background-repeat: repeat;
                            animation: bg-animation .2s infinite;
                            opacity: .9;
                            visibility: visible;
                        }
                        @keyframes noise-animation {
                            0% { transform: translate(0,0) }
                            10% { transform: translate(-5%,-5%) }
                            20% { transform: translate(-10%,5%) }
                            30% { transform: translate(5%,-10%) }
                            40% { transform: translate(-5%,15%) }
                            50% { transform: translate(-10%,5%) }
                            60% { transform: translate(15%,0) }
                            70% { transform: translate(0,10%) }
                            80% { transform: translate(-15%,0) }
                            90% { transform: translate(10%,5%) }
                            100% { transform: translate(5%,0) }
                        }
                    </style>
                    <div>
                        <div class="bg-color-noise">
                            <div class="noise"></div>
                        </div>
                    </div>
                '''
            ),