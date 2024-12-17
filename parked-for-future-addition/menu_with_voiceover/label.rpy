label start_story_menu_with_voiceover:
    menu(voiceoverfile="voiceover.mp3"):
        "Pick your option"

        "Option 1":
            call start_story_menu_with_voiceover_option1

        "Option 2":
            call start_story_menu_with_voiceover_option2

        "Option 3":
            call start_story_menu_with_voiceover_option3

    "Good choice!"

    return


label start_story_menu_with_voiceover_option1:
    "Option 1"

    return


label start_story_menu_with_voiceover_option2:
    "Option 2"

    return


label start_story_menu_with_voiceover_option3:
    "Option 3"

    return
