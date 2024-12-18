screen pong():
    add "bg pong field"

    add pong

    text "Player":
        xpos 240
        xanchor 0.5
        ypos 25
        size 40

    text "Eileen":
        xpos (1280 - 240)
        xanchor 0.5
        ypos 25
        size 40

    if pong.stuck:
        text "Click to Begin":
            xalign 0.5
            ypos 50
            size 40
