## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing 10

        textbutton _("Start") action Start()

        textbutton _("Preferences") action ShowMenu("preferences")

        textbutton _("Quit") action Quit(confirm=not main_menu)

    vbox:
        style "main_menu_vbox"

        text "[config.name!t]":
            style "main_menu_title"

        text "[config.version]":
            style "main_menu_version"


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


