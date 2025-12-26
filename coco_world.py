from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# --- CONSTANTS ---

IMAGE_PATH = "coco_photos/"
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 500

# --- MAIN WINDOW ---

window = Tk()
window.title("Coco Game")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.resizable(False, False)

# --- CANVAS FOR BACKGROUND ---

canvas = Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, highlightthickness=0)
canvas.pack()

menu_buttons = []

# --- BUTTON STYLES ---

style = ttk.Style()
style.configure("TButton", font=("Comic Sans MS", 15), padding=9)

# --- HELPER FUNCTION TO DISPLAY SCREEN ---

def display_scene(image_file, message_text):
    global current_image, menu_buttons

    image = Image.open(IMAGE_PATH + image_file)
    image = image.resize((WINDOW_WIDTH, WINDOW_HEIGHT))
    current_image = ImageTk.PhotoImage(image)
    
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=current_image)
    canvas.create_text(WINDOW_WIDTH // 2, 80, text=message_text, 
                       font=("Comic Sans MS", 26, "bold"), fill="black", anchor="center", justify="center")

    for button in menu_buttons:
        button.place_forget()
    menu_buttons.clear()

# --- MENU SCENE FUNCTION ---

def home_scene():
    display_scene("coco_chillz.jpeg", "COCO'S WORLD")

    start_button = ttk.Button(window, text="Start", command=intro_scene)
    exit_button = ttk.Button(window, text="Exit", command=window.destroy)

    start_button.place(relx=0.5, rely=0.75, anchor="center")
    exit_button.place(relx=0.5, rely=0.88, anchor="center")

    menu_buttons.extend([start_button, exit_button])

# --- ACTION SCENE FUNCTIONS ---

def intro_scene():
    display_scene("coco_chillz.jpeg", "Good Morning!\nWhat should Coco do today?")

    feed_button = ttk.Button(window, text="Feed", command=feed_scene)
    silly_button = ttk.Button(window, text="Silly", command=silly_scene)
    leave_button = ttk.Button(window, text="Leave", command=home_scene)

    feed_button.place(relx=0.35, rely=0.85, anchor="center")
    silly_button.place(relx=0.65, rely=0.85, anchor="center")
    leave_button.place(x=10, y=10)

    menu_buttons.extend([feed_button, silly_button, leave_button])

def feed_scene():
    display_scene("coco_eating.jpeg", "Coco is enjoying a treat!")

    curious_button = ttk.Button(window, text="Query", command=curious_scene)
    smile_button = ttk.Button(window, text="Playful", command=smiling_scene)
    leave_button = ttk.Button(window, text="Leave", command=home_scene)

    curious_button.place(relx=0.35, rely=0.85, anchor="center")
    smile_button.place(relx=0.65, rely=0.85, anchor="center")
    leave_button.place(x=10, y=10)

    menu_buttons.extend([curious_button, smile_button, leave_button])

def silly_scene():
    display_scene("coco_silly.jpeg", "Coco is being silly!")

    smile_button = ttk.Button(window, text="Playful", command=smiling_scene)
    feed_button = ttk.Button(window, text="Feed", command=feed_scene)
    leave_button = ttk.Button(window, text="Leave", command=home_scene)

    smile_button.place(relx=0.35, rely=0.85, anchor="center")
    feed_button.place(relx=0.65, rely=0.85, anchor="center")
    leave_button.place(x=10, y=10)

    menu_buttons.extend([smile_button, feed_button, leave_button])

def curious_scene():
    display_scene("coco_questioning.jpeg", "")

    feed_button = ttk.Button(window, text="Feed", command=feed_scene)
    stun_button = ttk.Button(window, text="BOO!", command=stunning_scene)
    leave_button = ttk.Button(window, text="Leave", command=home_scene)

    feed_button.place(relx=0.35, rely=0.85, anchor="center")
    stun_button.place(relx=0.65, rely=0.85, anchor="center")
    leave_button.place(x=10, y=10)

    menu_buttons.extend([feed_button, stun_button, leave_button])

def stunning_scene():
    display_scene("coco_stunning.jpeg", "")

    curious_button = ttk.Button(window, text="Query", command=curious_scene)
    sleep_button = ttk.Button(window, text="Nap Time", command=napping_scene)
    leave_button = ttk.Button(window, text="Leave", command=home_scene)

    curious_button.place(relx=0.35, rely=0.85, anchor="center")
    sleep_button.place(relx=0.65, rely=0.85, anchor="center")
    leave_button.place(x=10, y=10)

    menu_buttons.extend([curious_button, sleep_button, leave_button])

def napping_scene():
    display_scene("coco_sleeping.jpeg", "Coco is taking a nap...")

    wakeup_button = ttk.Button(window, text="Wake Up", command=intro_scene)
    bye_button = ttk.Button(window, text="Bye Bye", command=home_scene)
    leave_button = ttk.Button(window, text="Leave", command=home_scene)

    wakeup_button.place(relx=0.35, rely=0.85, anchor="center")
    bye_button.place(relx=0.65, rely=0.85, anchor="center")
    leave_button.place(x=10, y=10)

    menu_buttons.extend([wakeup_button, bye_button, leave_button])

def smiling_scene():
    display_scene("coco_smiling.jpeg", "Coco is smilling at you! <3")

    silly_button = ttk.Button(window, text="Silly", command=silly_scene)
    stun_button = ttk.Button(window, text="BOO!", command=stunning_scene)
    leave_button = ttk.Button(window, text="Leave", command=home_scene)

    silly_button.place(relx=0.35, rely=0.85, anchor="center")
    stun_button.place(relx=0.65, rely=0.85, anchor="center")
    leave_button.place(x=10, y=10)

    menu_buttons.extend([silly_button, stun_button, leave_button])

# --- END OF PROGRAMME ---

home_scene()
window.mainloop()