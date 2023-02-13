from tkinter import *

window = Tk()
window.title("Drag Tester")
window.geometry("1200x720")

alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


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
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)


def snap_function(event):
    widget = event.widget
    for boxes in answer_boxes:
        if -50 < widget.winfo_x() - boxes.winfo_x() < 50 and -50 < widget.winfo_y() - boxes.winfo_y() < 50:
            widget.place(x=10 + boxes.winfo_x(), y=10 + boxes.winfo_y())
            boxes.filled = True
            boxes.alphabet = widget.alphabet


class DragDropMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.alphabet = ""
        self.locked = False
        make_draggable(self)


class DnDFrame(DragDropMixin, Frame):
    pass


class AnswerFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filled = False
        self.alphabet = ""


def select_mode():
    global game_state
    # game_button.pack_forget()
    game_state = "Game"


# game_button = Button(window, width=100, height=100, bg="blue", text="PLAY", command=select_mode)
answer_boxes = [AnswerFrame(window, bg="gray", width=140, height=140, relief="sunken", borderwidth=10) for x in
                range(6)]

alphabet_blocks = [DnDFrame(window, width=120, height=120, bd=4, bg="red", relief="raised", borderwidth=5) for x
                   in range(25)]

running = True
game_state = "Game"

while running:
    if game_state == "Menu":
        # game_button.place(x=10, y=10)
        window.mainloop()
    if game_state == "Game":
        for items in alphabet_blocks:
            var = alphabet_blocks.index(items)
            items.alphabet = alphabet_list[var]
            text = Label(items, bg="red", text=f"{items.alphabet}", anchor=CENTER)
            text.place(x=50 + items.winfo_x(), y=50 + items.winfo_y())
            if 17 < var <= 25:
                items.place(x=10 + (200 * int(var - 18)), y=430)
            if 11 < var <= 17:
                items.place(x=10 + (200 * int(var - 12)), y=290)
            if 5 < var <= 11:
                items.place(x=10 + (200 * int(var - 6)), y=150)
            if var <= 5:
                items.place(x=10 + (200 * int(var)), y=10)
            items.tkraise()

        for items in answer_boxes:
            var = answer_boxes.index(items)
            items.place(x=10 + (200 * int(var)), y=580)
            items.lower()
        window.mainloop()

    # if -30 < widget.winfo_x() - answer_boxes[0].winfo_x() < 30 and -30 < widget.winfo_y() - answer_boxes[0].winfo_y() < 30:
    #     widget.place(x=20, y=590)
    #     answer_boxes[0].filled = True
    # elif -30 < widget.winfo_x() - answer_boxes[1].winfo_x() < 30 and -30 < widget.winfo_y() - answer_boxes[1].winfo_y() < 30:
    #     widget.place(x=220, y=590)
    #     answer_boxes[1].filled = True
    # elif -30 < widget.winfo_x() - answer_boxes[2].winfo_x() < 30 and -30 < widget.winfo_y() - answer_boxes[2].winfo_y() < 30:
    #     widget.place(x=420, y=590)
    #     answer_boxes[2].filled = True
    # elif -30 < widget.winfo_x() - answer_boxes[3].winfo_x() < 30 and -30 < widget.winfo_y() - answer_boxes[3].winfo_y() < 30:
    #     widget.place(x=620, y=590)
    #     answer_boxes[3].filled = True
    # elif -30 < widget.winfo_x() - answer_boxes[4].winfo_x() < 30 and -30 < widget.winfo_y() - answer_boxes[4].winfo_y() < 30:
    #     widget.place(x=820, y=590)
    #     answer_boxes[4].filled = True
    # elif -30 < widget.winfo_x() - answer_boxes[5].winfo_x() < 30 and -30 < widget.winfo_y() - answer_boxes[5].winfo_y() < 30:
    #     widget.place(x=1020, y=590)
    #     answer_boxes[5].filled = True
    # else:
    #     x = widget.winfo_x() - widget._drag_start_x + event.x
    #     y = widget.winfo_y() - widget._drag_start_y + event.y
    #     widget.place(x=x, y=y)
