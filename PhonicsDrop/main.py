import tkinter
import tkinter.font
from tkinter import *
from winsound import *
from pygame import mixer
import random

mixer.init()

test_sound = mixer.Sound("gym.ogg")
insist_sound = mixer.Sound("audio/insist.ogg")
sat_sound = mixer.Sound("audio/sat.ogg")
sin_sound = mixer.Sound("audio/sin.ogg")

root = Tk()
root.geometry("1200x740")

FRAME_WIDTH = 1200
FRAME_HEIGHT = 740
answer_frames = []
page_state = "murder death kill"

alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

coordinate_list = [(10, 200), (220, 200), (430, 200), (640, 200), (850, 200), (1060, 200)]
answer = ""
alphabet_blocks = []
score = 0
question_counter = 0
text = Label(bg="red")

word_dictionary = {
    "satpin": {
        "bank": ["sat", "sin", 'nip', "nap", "tan", "tin", "spin", "pins", "tins", "past", "pants", "inapt", "insist",
                 "paints"],

        "words": {
            "sat": {"length": 3,
                    "letters": ["s", "a", "t"],
                    "audio": sat_sound
                    },
            "sin": {"length": 3,
                    "letters": ["s", "i", "n"],
                    "audio": sin_sound
                    },
            "nip": {"length": 3,
                    "letters": ["n", "i", "p"],
                    "audio": test_sound
                    },
            "nap": {"length": 3,
                    "letters": ["n", "a", "p"],
                    "audio": test_sound
                    },
            "tan": {"length": 3,
                    "letters": ["t", "a", "n"],
                    "audio": test_sound
                    },
            "tin": {"length": 3,
                    "letters": ["t", "i", "n"],
                    "audio": test_sound
                    },
            "spin": {"length": 4,
                     "letters": ["s", "p", "i", "n"],
                     "audio": test_sound
                     },
            "pins": {"length": 4,
                     "letters": ["p", "i", "n", "s"],
                     "audio": test_sound
                     },
            "tins": {"length": 4,
                     "letters": ["t", "i", "n", "s"],
                     "audio": test_sound
                     },
            "past": {"length": 4,
                     "letters": ["p", "a", "s", "t"],
                     "audio": test_sound
                     },
            "pants": {"length": 5,
                      "letters": ["p", "a", "n", "t", "s"],
                      "audio": test_sound
                      },
            "inapt": {"length": 5,
                      "letters": ["i", "n", "a", "p", "t"],
                      "audio": test_sound
                      },
            "paints": {"length": 6,
                       "letters": ["p", "a", "i", "n", "t", "s"],
                       "audio": test_sound
                       },
            "insist": {"length": 6,
                       "letters": ["i", "n", "s", "i", "s", "t"],
                       "audio": insist_sound
                       },
        }
    },
    "hmdeck": {
        "bank": ["ink", "man", "hit"],
        "words": {
            "ink": {"length": 3,
                    "letters": ["i", "n", "k"]
                    },
            "man": {"length": 3,
                    "letters": ["m", "a", "n"]
                    },
            "hit": {"length": 3,
                    "letters": ["h", "i", "t"]
                    }
        }
    },
    "lrgobf": {
        "bank": ["farms", "glam"],
        "words": {
            "farms": {"length": 5,
                      "letters": ["f", "a", "r", "m", "s"]
                      },
            "glam": {"length": 4,
                     "letters": ["g", "l", "a", "m"]
                     }
        }

    }
}


def play_audio():
    global answer
    global question_counter
    global page_state
    return mixer.Sound.play(word_dictionary[page_state]["words"][answer]["audio"])


def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)
    widget.bind("<ButtonRelease>", snap_function)


def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y


def on_drag_motion(event):
    widget = event.widget
    widget.tkraise()
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)


class DragDropMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.alphabet = ""
        self.position = 100
        self.locked = False
        make_draggable(self)


class DnDFrame(DragDropMixin, Label):
    pass


class AnswerFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filled = False
        self.alphabet = ""


def draw_menu():
    global score
    global question_counter
    global text
    text.option_add("*Font", "Times 20")
    question_counter = 0
    score = 0
    frame = Frame(root, width=FRAME_WIDTH, height=FRAME_HEIGHT, bg="green")
    frame.place(x=0, y=0)
    step_one_button = Button(frame, height=2, width=10, text="SATPIN", command=draw_page_1)
    step_one_button.place(x=550, y=100)
    step_two_button = Button(frame, height=2, width=10, text="HMDECK", command=draw_page_2)
    step_two_button.place(x=550, y=200)
    step_three_button = Button(frame, height=2, width=10, text="LRGOBF", command=draw_page_3)
    step_three_button.place(x=550, y=300)
    practice_button = Button(frame, height=2, width=10, text="Practice", command=draw_practice_page)
    practice_button.place(x=550, y=500)


def generate_question():
    global answer_frames
    global page_state
    global alphabet_blocks
    global answer
    global coordinate_list
    global question_counter
    global text
    text.option_add("*Font", "Times 76")

    random.shuffle(word_dictionary[page_state]["bank"])
    answer = word_dictionary[page_state]["bank"][question_counter]
    print(answer)
    question_length = word_dictionary[page_state]["words"][answer]["length"]
    # print(question_length)
    answer_frames = [AnswerFrame(root, bg="gray", width=146, height=146, relief="sunken", borderwidth=10) for x in
                     range(question_length)]
    if question_length == 3:
        for items in answer_frames:
            var = answer_frames.index(items)
            items.place(x=310 + (200 * int(var)), y=580)
            items.tkraise()
    elif question_length == 4:
        for items in answer_frames:
            var = answer_frames.index(items)
            items.place(x=210 + (200 * int(var)), y=580)
            items.tkraise()
    elif question_length == 5:
        for items in answer_frames:
            var = answer_frames.index(items)
            items.place(x=110 + (200 * int(var)), y=580)
            items.tkraise()
    elif question_length == 6:
        for items in answer_frames:
            var = answer_frames.index(items)
            items.place(x=10 + (200 * int(var)), y=580)
    # GENERATE ALPHABET BLOCKS
    random.shuffle(coordinate_list)
    alphabet_blocks = [DnDFrame(root, width=2, height=1, bd=4, bg="red", relief="raised", borderwidth=5) for x
                       in range(6)]
    for items in alphabet_blocks:
        var = alphabet_blocks.index(items)
        try:
            items.alphabet = word_dictionary[page_state]["words"][answer]["letters"][var]
        except IndexError:
            items.alphabet = random.choice(alphabet_list)
        items.configure(text=f"{items.alphabet.upper()}")
        items.place(x=coordinate_list[var][0], y=coordinate_list[var][1])


def draw_practice_page():
    global page_state
    page_state = "satpin"
    alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                     "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    frame = Frame(root, width=FRAME_WIDTH, height=FRAME_HEIGHT, bg="white")
    frame.place(x=0, y=0)
    button = Button(frame, height=2, width=10, text="Menu", command=draw_menu)
    button.place(x=100, y=620)
    text.option_add("*Font", "Times 76")
    alphabet_blocks = [DnDFrame(frame, width=2, height=1, bd=4, bg="red", relief="raised", borderwidth=5) for x
                       in range(26)]
    for blocks in alphabet_blocks:
        blocks.alphabet = alphabet_list[alphabet_blocks.index(blocks)]
        blocks.configure(text=f"{blocks.alphabet.upper()}")
        if alphabet_blocks.index(blocks) >= 24:
            blocks.place(x=620 + 200 * (alphabet_blocks.index(blocks) - 25), y=600)
        elif alphabet_blocks.index(blocks) >= 18:
            print(alphabet_blocks.index(blocks))
            blocks.place(x=20 + 200 * (alphabet_blocks.index(blocks) - 18), y=450)
        elif alphabet_blocks.index(blocks) >= 12:
            blocks.place(x=20 + 200 * (alphabet_blocks.index(blocks) - 12), y=300)
        elif alphabet_blocks.index(blocks) >= 6:
            blocks.place(x=20 + 200 * (alphabet_blocks.index(blocks) - 6), y=150)
        else:
            blocks.place(x=20 + 200 * (alphabet_blocks.index(blocks)), y=00)


def draw_page_1():
    global page_state
    page_state = "satpin"
    text.option_add("*Font", "Times 20")
    frame = Frame(root, width=FRAME_WIDTH, height=FRAME_HEIGHT, bg="white")
    frame.place(x=0, y=0)
    button = Button(frame, height=2, width=10, text="Menu", command=draw_menu)
    button.place(x=0, y=0)
    one_more_time_button = Button(frame, height=1, width=10, text="Listen", command=play_audio)
    one_more_time_button.place(x=520, y=500)
    generate_question()


def draw_page_2():
    global page_state
    page_state = "hmdeck"
    text.option_add("*Font", "Times 20")
    frame = Frame(root, width=FRAME_WIDTH, height=FRAME_HEIGHT, bg="white")
    frame.place(x=0, y=0)
    button = Button(frame, height=2, width=10, text="Menu", command=draw_menu)
    button.place(x=0, y=0)
    one_more_time_button = Button(frame, height=1, width=10, text="Listen", command=play_audio)
    one_more_time_button.place(x=520, y=500)
    generate_question()


def draw_page_3():
    global page_state
    page_state = "lrgobf"
    text.option_add("*Font", "Times 20")
    frame = Frame(root, width=FRAME_WIDTH, height=FRAME_HEIGHT, bg="purple")
    frame.place(x=0, y=0)
    button = Button(frame, height=2, width=10, text="Menu", command=draw_menu)
    button.place(x=0, y=0)
    one_more_time_button = Button(frame, height=1, width=10, text="Listen", command=play_audio)
    one_more_time_button.place(x=520, y=500)
    generate_question()


def snap_function(event):
    global alphabet_blocks
    global score
    global question_counter
    global page_state
    widget = event.widget
    if widget.winfo_x() < 0 or widget.winfo_x() > 1200 or widget.winfo_y() < 0 or widget.winfo_y() > 720:
        widget.place(x=540, y=300)
    for var in range(len(answer_frames)):
        if answer_frames[var].filled:
            if widget.position == var:
                if widget.winfo_x() == answer_frames[var].winfo_x() + 10 and \
                        widget.winfo_y() == answer_frames[var].winfo_y() + 10:
                    pass
                else:
                    answer_frames[var].filled = False
                    answer_frames[var].alphabet = ""
                    widget.position = 100
    for var in range(len(answer_frames)):
        if not answer_frames[var].filled:
            if -50 < widget.winfo_x() - answer_frames[var].winfo_x() < 50 and \
                    -50 < widget.winfo_y() - answer_frames[var].winfo_y() < 50:
                widget.place(x=10 + answer_frames[var].winfo_x(), y=10 + answer_frames[var].winfo_y())
                answer_frames[var].filled = True
                answer_frames[var].alphabet = widget.alphabet
                widget.position = var
    answer_check = [x.alphabet.lower() for x in answer_frames]
    if answer_check == word_dictionary[page_state]["words"][answer]["letters"]:
        score += 1
        question_counter += 1
        if question_counter > len(word_dictionary[page_state]["bank"]) - 1:
            draw_menu()
        elif page_state == "satpin":
            draw_page_1()
        elif page_state == "hmdeck":
            draw_page_2()
        elif page_state == "lrgobf":
            draw_page_3()
    # else:
    # print(f"Answer_check: {answer_check}")
    # print(f"word_dict: {word_dictionary['words'][answer]['letters']}")


draw_menu()
root.resizable(False, False)
root.mainloop()
