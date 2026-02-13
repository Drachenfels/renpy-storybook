import renpy

"""renpy
init -450 python:
"""


def illegible_word(word):
    """Generate illegible/glitchy text of approximately the same length"""
    # Try to use DDLC's glitchtext function if available
    length = renpy.random.randint(1, len(word) + 3)

    try:
        if "glitchtext" in dir(renpy.store):
            return glitchtext(length)
    except Exception:
        pass

    # Fallback to custom illegible text generation

    # 50/50 to generate psuedo-word or random glitched text
    if renpy.random.randint(0, 1):
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
    else:
        # Use ASCII-safe characters that will render in most fonts
        vowels = "#@%&*+=-~^"
        consonants = "#@%&*+=-~^"

    new_word = ""

    for _ in range(length):
        if renpy.random.randint(0, 1):
            new_word += renpy.random.choice(consonants)
        else:
            new_word += renpy.random.choice(vowels)

    return new_word


class Word:
    def __init__(self, text, replaced_text, glitched_text):
        self.original = text
        self.shuffled = replaced_text
        self.glitched = glitched_text
        self.picked = False

    @property
    def is_solved(self):
        return self.original == self.shuffled

    def swap(self, another_word):
        tmp = self.shuffled
        self.shuffled = another_word.shuffled
        another_word.shuffled = tmp


class Entry:
    def __init__(self, content):
        self.content = []

        shuffled_words = self.shuffle_words(content)

        for word in content.split():
            self.content.append(
                Word(
                    word,
                    shuffled_words.pop(0),
                    illegible_word(word),
                )
            )

    def shuffle_words(self, content):
        shuffled_words = content.split()
        words = content.split()
        punctuations = ',.!?;:"()[]{}<>'

        # guarantees that no single word will match the original
        attempts = 100

        while any(
            words[idx].strip(punctuations) == shuffled_words[idx].strip(punctuations)
            for idx in range(len(shuffled_words))
        ):
            renpy.random.shuffle(shuffled_words)

            attempts -= 1

            if attempts <= 0:
                break

        return shuffled_words

    def __repr__(self):
        return f"'{self.full_text}'"

    @property
    def full_text(self):
        return " ".join(word.original for word in self.content)

    @property
    def full_glitched(self):
        return " ".join(word.glitched for word in self.content)

    @property
    def is_solved(self):
        return all([word.is_solved for word in self.content])

    @property
    def picked_words(self):
        """
        Returns a list of currently picked words in the entry.
        """
        return [word for word in self.content if word.picked]

    def reset_picks(self):
        for word in self.picked_words:
            word.picked = False


class Page:
    def __init__(self, page_number, entries):
        self.page_number = page_number
        self.entries = entries

        self._solved_entries = []
        self._unsolved_entries = [Entry(content) for content in entries]

    @property
    def solved_entries(self):
        return self._solved_entries

    @property
    def current_entry(self):
        return self._unsolved_entries[0] if self._unsolved_entries else None

    def mark_current_entry_solved(self):
        self._solved_entries.append(self._unsolved_entries.pop(0))

    @property
    def unsolved_entries(self):
        return self._unsolved_entries[1:]

    def add_entry(self, content):
        self._unsolved_entries.append(Entry(content))


class ProgressiveScramble:
    def __init__(self, diary):
        self.diary = diary

        self._current_page = 1
        self.pages = []

        for idx, page_entries in enumerate(self.diary):
            self.pages.append(Page(idx + 1, page_entries))

    @property
    def total_pages(self):
        return len(self.diary)

    @property
    def current_page(self):
        return self.pages[self._current_page - 1]

    @property
    def is_current_page_solved(self):
        return False

    @property
    def is_solved(self):
        return (
            len(self.current_page.unsolved_entries) == 0
            and self.current_page.current_entry is None
        )

    def swap_words(self, word):
        if word.is_solved:
            return

        entry = self.current_page.current_entry

        picked_words = entry.picked_words

        if len(picked_words) >= 1:
            entry.reset_picks()

        if len(picked_words) == 1:
            word.swap(picked_words[0])
        else:
            word.picked = not word.picked

        if entry.is_solved:
            self.current_page.mark_current_entry_solved()

    def is_word_locked(self, index):
        """Check if word is in correct position (locked)"""
        return self.scrambled_words[index] == self.original_words[index]

    def next_page(self):
        self._current_page += 1 if self._current_page < self.total_pages else 0

    def prev_page(self):
        self._current_page -= 1 if self._current_page > 1 else 0
