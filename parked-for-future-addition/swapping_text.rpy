init python:
    import math
    import random

    class DispTextStyle():
        custom_tags = ["omega", "bt", "fi", "sc", "rotat", "chaos", "move"]
        accepted_tags = ["", "b", "s", "u", "i", "color", "alpha", "font",  "size", "outlinecolor", "plain", 'cps']
        custom_cancel_tags = ["/" + tag for tag in custom_tags]
        cancel_tags = ["/" + tag for tag in accepted_tags]
        def __init__(self):
            self.tags = {}

        # For setting style properties. Returns false if it accepted none of the tags
        def add_tags(self, char):
            tag, _, value = char.partition("=") # Separate the tag and its info
            # Add tag to dictionary if we accept it
            if tag in self.accepted_tags or tag in self.custom_tags:
                if value == "":
                    self.tags[tag] = True
                else:
                    self.tags[tag] = value
                return True
            # Remove mark tag as cleared if should no longer apply it
            if tag in self.cancel_tags or tag in self.custom_cancel_tags:
                tag = tag.replace("/", "")
                self.tags.pop(tag)
                return True
            return False # If we got any other tag, tell the function to let it pass

        # Applies all style properties to the string
        def apply_style(self, char):
            new_string = ""
            # Go through and apply all the tags
            new_string += self.start_tags()
            # Add the character in the middle
            new_string += char
            # Now close all the tags we opened
            new_string += self.end_tags()
            return new_string

        # Spits out start tags. Primarily used for SwapText
        def start_tags(self):
            new_string = ""
            # Go through the custom tags
            for tag in self.custom_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            # Go through the standard tags
            for tag in self.accepted_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            return new_string

        # Spits out ending tags. Primarily used for SwapText
        def end_tags(self):
            new_string = ""
            # The only tags we are required to end are any custom text tags.
            # And should also end them in the reverse order they were applied.
            reversed_cancels = [tag for tag in self.custom_cancel_tags]
            reversed_cancels.reverse()
            for tag in reversed_cancels:
                temp = tag.replace("/", "")
                if temp in self.tags:
                    new_string += "{" + tag + "}"
            return new_string

    class SwapText(renpy.Displayable):
        def __init__(self, start_tags, text1, text2, end_tags, **kwargs):
            super().__init__(**kwargs)

            self.start_tags = start_tags
            self.end_tags = end_tags

            self.child_t1 = Text(start_tags + text1 + end_tags)
            self.child_t2 = Text(start_tags + text2 + end_tags)

            self.child = self.child_t1
            self.bound_box = None
            self.width = 200
            self.height = 40

        def render(self, width, height, st, at):
            if self.bound_box is None:
                child_render1 = renpy.render(self.child_t1, width, height, st, at)
                child_render2 = renpy.render(self.child_t2, width, height, st, at)

                w1, h1 = child_render1.get_size()
                w2, h2 = child_render2.get_size()

                left_bound = (w1 if w1 >= w2 else w2) * -1
                bottom_bound = h1 if h1 >= h2 else h2

                self.bound_box = (
                    (left_bound, 0),
                    (0, bottom_bound),
                )

            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()

            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0, 0))
            render.fill((255, 0, 0, 125))
            renpy.redraw(self, 0)

            return render

        def event(self, ev, x, y, st):
            EVENT_MOUSE_UP = 1026

            if self.bound_box is None:
                return self.child.event(ev, x, y, st)

            if random.choice([0,1,2,3]) == 0:
                print("BOX", self.bound_box, "CUR. POS", x, y, ev.type)

            if x < self.bound_box[0][0] or x > self.bound_box[1][0]:
                return self.child.event(ev, x, y, st)

            if y < self.bound_box[0][1] or y > self.bound_box[1][1]:
                return self.child.event(ev, x, y, st)

            if ev.type == EVENT_MOUSE_UP:
                self.child = self.child_t2 if self.child is self.child_t1 else self.child_t1

                raise renpy.IgnoreEvent

            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]

    def fill_with_spaces(str1, str2):
        if len(str1) > len(str2):
            str2 = str2.ljust(len(str1) - 1)
        elif len(str2) > len(str1):
            str1 = str1.ljust(len(str2) - 1)
        return str1, str2

    def swap_tag(tag, argument, contents):
        new_content = []

        if argument == "":
            return contents

        alt_text = argument

        my_style = DispTextStyle()

        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:

                if len(text) != len(alt_text):
                    text, alt_text = fill_with_spaces(text, alt_text)

                text_to_display = SwapText(my_style.start_tags(), text, alt_text, my_style.end_tags())

                new_content.append((renpy.TEXT_DISPLAYABLE, text_to_display))

            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_content.append((kind, text))

            else:
                new_content.append((kind,text))

        return new_content

    config.custom_text_tags["swap"] = swap_tag


label start:
    """Hi there, I am {swap=johnanson}{u}JOHAMSOM{/u}{/swap}"""

    return
