# each entry is set of lines (lines are only to visualy split entry per line)
define entry_1 = "Today the literature club met to discuss Gothic poetry and symbolism"
define entry_2 = "Natsuki brought strawberry cupcakes and they were delicious as always"
define entry_3 = "But I cannot remember eating them or even being at the meeting"

define entry_4 = "I found this notebook in my bag this morning"
define entry_5 = "The handwriting looks exactly like mine but feels completely unfamiliar"
define entry_6 = "Someone named Yuri wrote these entries but I do not know who that is"

# each page consist of entries
define page_1 = (
    entry_1,
    entry_2,
    entry_3,
)

define page_2 = (
    entry_4,
    entry_5,
    entry_6,
)

# diary consists of pages
define diary = (
    page_1,
    page_2,
)

default puzzle = ProgressiveScramble(diary)


label start_story_diary_wordscramble:
    call screen progressive_diary_game()

    return
