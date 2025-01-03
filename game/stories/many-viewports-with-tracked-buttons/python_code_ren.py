import renpy
from renpy.ui import Action

"""renpy
init -100 python:
"""


class ScrollViewport(Action):
    def __init__(self, yadj, scroll_dir, step=50):
        # def __init__(self, yadj, scroll_dir, step):
        self.yadj = yadj
        self.scroll_dir = scroll_dir
        self.step = step

    def __call__(self):
        # yadj = renpy.focus_coordinates()[1]
        # Don't confuse dir with the other use case for "up" which
        # refers to the state of the key (pressed/released)
        if self.scroll_dir == "up":
            self.yadj.change(self.yadj.value - self.step)

            renpy.display.behavior.queue_event("focus_up", up=False)
        else:
            self.yadj.change(self.yadj.value + self.step)

            renpy.display.behavior.queue_event("focus_down", up=False)
        renpy.restart_interaction


class ChoiceItem:
    def __init__(self, caption):
        self.caption = caption
        self.id = caption.lower()
