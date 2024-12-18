screen story_picker():
    style_prefix "gallery"

    frame:
        xfill True
        yfill True

        vbox:
            xalign 0.5
            yalign 0.2
            textbutton _("Inventory System") action [Hide(), Call("start_story_inventory")]
            textbutton _("Game of Pong") action [Hide(), Call("start_story_pong")]

            textbutton _("MainMenu") action MainMenu(confirm=False, save=False)
