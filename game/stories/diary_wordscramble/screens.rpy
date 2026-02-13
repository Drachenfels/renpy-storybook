screen progressive_diary_game():
    style_prefix "diary"

    add "bg wordscramblebook"

    frame:
        align (1.0, 1.0)
        offset (-10, -10)
        background Solid("#00000088") # Semi-transparent black
        padding (10, 5)

        hbox:
            textbutton "Prev":
                action Function(puzzle.prev_page)
                text_color "#0f0"

            text "Page [puzzle.current_page.page_number]/[puzzle.total_pages]":
                color "#0f0"

            textbutton "Next":
                action Function(puzzle.next_page)
                text_color "#0f0"

    frame:
        pos (230, 80)
        xsize 672
        ysize 964

        # background Solid("#cfcf0088")
        background None
        padding (10, 10)

        vbox:
            hbox:
                box_wrap True
                box_wrap_spacing 10
                spacing 8

                if puzzle.current_page.solved_entries:
                    for entry in puzzle.current_page.solved_entries:
                        text entry.full_text

                if puzzle.current_page.current_entry:
                    for word in puzzle.current_page.current_entry.content:
                        textbutton word.shuffled:
                            action Function(puzzle.swap_words, word)
                            if word.is_solved:
                                text_color "#000000"
                                text_outlines [(2, "#ffffff", 0, 0)]
                            elif word.picked:
                                text_color "#ffaa00"
                                text_outlines [(2, "#000000", 0, 0)]
                            else:
                                text_color "#808080"
                                text_outlines [(1, "#000000", 0, 0)]

                if puzzle.current_page.unsolved_entries:
                    for entry in puzzle.current_page.unsolved_entries:
                        text entry.full_glitched

                if puzzle.is_solved:
                    text "Page Complete!":
                        color "#00ff00"
                        at pop_in

transform pop_in:
    alpha 0.0 zoom 0.5    # Start invisible and small
    parallel:
        linear 0.6 alpha 1.0
    parallel:
        easein_back 1.5 zoom 1.0 # Bounces slightly larger then settles

    # Optional: Subtle breathing after it pops in
    block:
        linear 3.0 zoom 1.05
        linear 3.0 zoom 1.0
        repeat

style diary_text:
    # font "gui/font/Halogen.ttf"
    size 24
    color "#000000"
    outlines []
    text_align 0.0  # Left-aligned
    line_spacing 26  # Slight spacing between lines
    line_leading 10

style diary_illegible:
    # font "gui/font/Halogen.ttf"
    size 24
    color "#404040"  # Dark gray
    outlines []
    text_align 0.0
    line_spacing 15

style diary_button:
    background None
    padding (5, 5)

style diary_hbox:
    spacing 5

style diary_vbox:
    spacing 10
