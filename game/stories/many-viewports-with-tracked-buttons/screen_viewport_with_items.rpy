screen viewport_with_items(items, pick_store):
    style_prefix "choice"

    default yadj = ui.adjustment()
    default hoveredrect = (1, 2, 3, 100)
    default hoveredy = 56

    key "K_UP" action ScrollViewport(yadj, 'up', hoveredy)
    key "K_DOWN" action ScrollViewport(yadj, 'down', hoveredy)
    key "pad_righty_neg" action ScrollViewport(yadj, 'up', hoveredy)
    key "pad_dpup_press" action ScrollViewport(yadj, 'up', hoveredy)
    key "pad_dpdown_press" action ScrollViewport(yadj, 'down', hoveredy)
    key "pad_righty_pos" action ScrollViewport(yadj, 'down', hoveredy)

    python:
        print(pick_store)
        print("PICKED COLOUR", picked_colour)
        print("PICKED SHAPE", picked_shape)

    vbox:
        label "Picked item: [getattr(store, pick_store)]"
        viewport yadjustment yadj:
            draggable True
            mousewheel True
            scrollbars "vertical"
            xpos 0
            ypos 0
            xsize 400
            ysize 300

            window:
                background Solid("#7f7f7f")
                ysize 100 + 80 * len(items)
                vbox:
                    for idx, item in enumerate(items):
                        textbutton item.caption:
                            xsize 380
                            action SetVariable(pick_store, item.id)
                            selected getattr(store, pick_store) == item.id

        textbutton _("Back") action Return()
