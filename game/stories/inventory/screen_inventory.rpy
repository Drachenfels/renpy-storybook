screen inventory():
    style_prefix "inventory"

    python:
        items = inventory.get_list_of_items(limit=25)

    frame:
        xsize 0.8
        xalign 0.1
        ypos 0.05

        vbox:
            frame:
                background Solid("#FF7F99")
                text "This is inventory screen, feel free to add or remove items, when you have enough, click 'Back' button to return to story picker."

            hbox:
                spacing 30
                textbutton ("Add Green Armour") action [Function(inventory.add_item, green_armour)]
                textbutton ("Add Brown Armour") action [Function(inventory.add_item, brown_armour)]
                textbutton ("Add Bronze Armour") action [Function(inventory.add_item, bronze_armour)]

            grid 5 5:
                spacing 4
                for idx, item in enumerate(items, 0):
                    frame:
                        padding (12, 12, 12, 12)
                        xsize 96
                        ysize 96

                        if item is not None:
                            imagebutton idle item.image action [Function(inventory.remove_item, idx)]:
                                xysize (100,100)
                                xfill True
                                yfill True

            frame:
                background Solid("#cfffdb")

                textbutton _("Back") action Return()
