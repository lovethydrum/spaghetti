import json
from tkinter import *
from tkinter.filedialog import asksaveasfile

tk = Tk()
tk.geometry("1000x1000")
level = 1
sub_1 = 1
sub_2 = 0
sub_3 = 0
saved = False
page_state = "menu"
path = "./"


def writeToJSONFile(path, fileName, data):
    json.dump(data, path)


def level_up():
    global sub_1
    global sub_2
    global sub_3
    global level
    global page_state
    if page_state == "level 1":
        if sub_1 < 5:
            sub_1 += 1
            draw_level_1()
        elif sub_1 == 5:
            print("elif")
            if level < 2:
                level = 2
            draw_menu()
    elif page_state == "level 2":
        sub_2 += 1
        draw_menu()
    elif page_state == "level 3":
        sub_3 += 1
        draw_menu()
    save_file()


def level_down():
    global level
    level -= 1
    print(level)
    draw_menu()
    save_file()


def save_file():
    global saved
    global level
    global sub_1
    global sub_2
    global sub_3
    data = {
        'level': level,
        'sub 1': sub_1,
        'sub 2': sub_2,
        'sub 3': sub_3,
    }
    with open("test_file.json", "w") as f:
        json.dump(data, f)
    saved = True


def load_file():
    global level
    global sub_1
    global sub_2
    global sub_3
    with open("test_file.json", "r") as f:
        content = json.load(f)
    level = content["level"]
    sub_1 = content["sub 1"]
    sub_2 = content["sub 2"]
    sub_3 = content["sub 3"]


def reset_settings():
    global level
    global sub_1
    global sub_2
    global sub_3
    level = 1
    sub_1 = 1
    sub_2 = 0
    sub_3 = 0
    save_file()
    draw_menu()


def draw_menu():
    global page_state
    page_state = "menu"
    # frame = Frame(tk, width=1000, height=1000, bg="blue")
    # frame.place(x=0, y=0)
    main_menu_canvas = Canvas(tk, relief=GROOVE, width=1000, height=1000)
    world_map = PhotoImage(file="world_map.png")
    image = main_menu_canvas.create_image(50, 50, anchor=NE, image=world_map)
    reset_button = Button(main_menu_canvas, width=20, height=10, command=reset_settings)
    world_button_1 = Button(main_menu_canvas, width=10, height=5, command=draw_level_1)
    world_button_2 = Button(main_menu_canvas, width=10, height=5, command=draw_level_1)
    world_button_3 = Button(main_menu_canvas, width=10, height=5)
    world_button_4 = Button(main_menu_canvas, width=10, height=5)
    world_button_1.place(x=0, y=200)
    reset_button.place(x=500, y=600)
    if level > 1:
        world_button_2.place(x=100, y=200)
    # else:
    #     world_button_2.grid_forget()
    #     world_button_3.grid_forget()
    #     world_button_4.grid_forget()
    if level > 2:
        world_button_3.place(x=200, y=200)
    # else:
    #     world_button_3.grid_forget()
    #     world_button_4.grid_forget()
    if level > 3:
        world_button_4.place(x=300, y=200)
    # else:
    #     world_button_4.grid_forget()


def draw_level_1():
    global page_state
    page_state = "level 1"
    frame = Frame(tk, width=1000, height=1000, bg="red")
    frame.place(x=0, y=0)
    button = Button(frame, width=10, height=5, command=level_up)
    button2 = Button(frame, width=10, height=5, command=level_up)
    button3 = Button(frame, width=10, height=5, command=level_up)
    button4 = Button(frame, width=10, height=5, command=level_up)
    button5 = Button(frame, width=10, height=5, command=level_up)
    button.place(x=0, y=100)
    if sub_1 > 1:
        button2.place(x=100, y=100)
    # else:
    #     button2.grid_forget()
    #     button3.grid_forget()
    #     button4.grid_forget()
    #     button5.grid_forget()
    if sub_1 > 2:
        button3.place(x=200, y=100)
    # else:
    #     button3.grid_forget()
    #     button4.grid_forget()
    #     button5.grid_forget()
    if sub_1 > 3:
        button4.place(x=300, y=100)
    # else:
    #     button4.grid_forget()
    #     button5.grid_forget()
    if sub_1 > 4:
        button5.place(x=400, y=100)
    # else:
    #     button5.grid_forget()


try:
    load_file()
except FileNotFoundError:
    save_file()

draw_menu()
tk.mainloop()