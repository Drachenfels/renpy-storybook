label start_story_pong:
    # Hide the window and quick menu while in pong
    window hide

    $ quick_menu = False

    call screen pong

    $ quick_menu = True

    window show

    show pong_player vhappy

    if _return == "pong_player":
        pong_player "I win!"

    else:
        pong_player "You won! Congratulations."
