import os
from tkinter import filedialog
from tkinter.filedialog import askopenfile, askopenfilename
from PIL import Image
import customtkinter
from test_image import eval_image

FILE_PATH = ""
PLANT_NAME = ""
def open_file():
    file = filedialog.askopenfile(mode='r')
    if file is not None:
        filepath = os.path.abspath(file.name)
        print(filepath)
        global FILE_PATH
        FILE_PATH = filepath
        my_image = customtkinter.CTkImage(light_image=Image.open(filepath), size=(400, 400))
        label_image.configure(image= my_image)

def run_model():
    print(FILE_PATH)
    global PLANT_NAME
    PLANT_NAME = eval_image(FILE_PATH)
    label.configure(text=f"Prediction: {PLANT_NAME}")
    app.clipboard_clear()
    app.clipboard_append(PLANT_NAME)



customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk(fg_color="pink")  # create CTk window like you do with the Tk window
app.geometry("800x650")

# Use CTkButton instead of tkinter Button
fr=customtkinter.CTkFrame(master=app, fg_color="pink", height=600, width=800)
fr.grid(rowspan=3, columnspan=2, padx = 0, pady = 0)

button = customtkinter.CTkButton(master=fr, text="Load Image", command=open_file, fg_color="#AA336A", hover_color="#ff8e81", width=325)
button2 = customtkinter.CTkButton(master=fr, text="Run", command=run_model, fg_color="#AA336A", width=325, hover_color="#ff8e81")
button.grid(row=0, column=0, padx = 0, pady = 10)   # grid dynamically divides the space in a grid
button2.grid(row=0, column=1, padx = 0, pady = 10)

bottom_frame = customtkinter.CTkFrame(master=fr, fg_color="pink", height=600, width=800)
bottom_frame.grid(row=1, columnspan =2, padx = 0, pady = 0)
label_image = customtkinter.CTkLabel(master=bottom_frame, width=760, height=500, fg_color='pink', text='')

label = customtkinter.CTkLabel(master=bottom_frame, text=f"Prediction: {PLANT_NAME}", fg_color="transparent", font=("Lato", 25))

label_image.grid(column=0, row=0, padx = 20, pady = 5)
label.grid(column=0, row=1, padx = 20, pady = 10)


app.mainloop()