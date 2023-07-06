from tkinter.filedialog import askopenfile, askopenfilename
from PIL import Image
import customtkinter

def open_file():
    file = askopenfilename()
    if file is not None:
        print(file)
        my_image = customtkinter.CTkImage(light_image=Image.open(file), size=(400, 400))
        label_image.configure(image= my_image)

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk(fg_color="pink")  # create CTk window like you do with the Tk window
app.geometry("800x650")

# Use CTkButton instead of tkinter Button
fr=customtkinter.CTkFrame(master=app, fg_color="pink", height=600, width=800)
fr.grid(rowspan=3, columnspan=2, padx = 0, pady = 0)

button = customtkinter.CTkButton(master=fr, text="Load Image", command=open_file, fg_color="#AA336A", hover_color="#ff8e81", width=325)
button2 = customtkinter.CTkButton(master=fr, text="Run", command=open_file, fg_color="#AA336A", width=325, hover_color="#ff8e81")
button.grid(row=0, column=0, padx = 0, pady = 10)   # grid dynamically divides the space in a grid
button2.grid(row=0, column=1, padx = 0, pady = 10)

bottom_frame = customtkinter.CTkFrame(master=fr, fg_color="pink", height=600, width=800)
bottom_frame.grid(row=1, columnspan =2, padx = 0, pady = 0)
label_image = customtkinter.CTkLabel(master=bottom_frame, width=760, height=500, fg_color='pink', text='')

label = customtkinter.CTkLabel(master=bottom_frame, text="Prediction: ", fg_color="transparent", font=("Lato", 25))

label_image.grid(column=0, row=0, padx = 20, pady = 5)
label.grid(column=0, row=1, padx = 20, pady = 10)


app.mainloop()