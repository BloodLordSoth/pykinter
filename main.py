import customtkinter as ctk
import os, time

root = ctk.CTk()
root.title('Pykinter file creator')
root.geometry('500x300')
ctk.set_appearance_mode("dark")
root.configure(bg="#413e40")
root.resizable(width=False, height=False)


def write_shell():
    value: str = combo.get()
    data = ['#!/bin/sh', 'python3 -m venv venv', 'source venv/bin/activate', 'pip install ' + value]
    with open('kinter.sh', 'w') as file:
        for item in data:
            file.write(item + "\n")

def test():
    value_two: str = text_one.get()
    value_three: str = text_two.get()
    os.system('clear')
    time.sleep(0.5)
    print('Navigating...\n')
    time.sleep(0.5)
    os.chdir(os.path.expanduser('~'))
    time.sleep(1)
    if os.path.isdir(value_three):
        os.chdir(value_three)
    else:
        os.mkdir(value_three)
        os.chdir(value_three)
    time.sleep(1)
    print('Creating directory')
    os.mkdir(value_two)
    time.sleep(1)
    os.chdir(value_two)
    print('Initiating python build')
    os.system('touch main.py')
    write_shell()
    print('Completed')



bg_label = ctk.CTkLabel(root, width=300, height=400, bg_color="#3b3739", text="")
bg_label.place(relx=0.20, rely=0.26)
combo_label = ctk.CTkLabel(root, width=300, height=100, bg_color="#3b3739", text_color="white", font=("Arial",20), text="Select creation type:")
combo_label.place(relx=0.20, rely=-0.07)
newdir_label = ctk.CTkLabel(root, text="New Directory name:", bg_color="#3b3739", text_color="white")
newdir_label.place(relx=0.23, rely=0.40)
destdir_label = ctk.CTkLabel(root, text="Destination Directory:", bg_color="#3b3739", text_color="white")
destdir_label.place(relx=0.23, rely=0.62)
combo = ctk.CTkComboBox(root, width=200, height=25, values=["--Pick an option--", "customtkinter", "pygame"])
combo.place(relx=0.3, rely=0.21)
text_one = ctk.CTkEntry(root, placeholder_text="")
text_one.place(relx=0.49, rely=0.40)
text_two = ctk.CTkEntry(root, placeholder_text="")
text_two.place(relx=0.50, rely=0.62)
blue_label = ctk.CTkLabel(root, width=100, height=150, bg_color="dark blue", text="")
blue_label.place(relx=0, rely=0)
yellow_label = ctk.CTkLabel(root, width=100, height=150, bg_color="#c3bb0b", text="")
yellow_label.place(relx=0.80, rely=0.50)
name_label = ctk.CTkLabel(root, width=100, height=30, bg_color="#3b3739", font=("Arial", 13), text_color="black", text="A BloodLordSoth production")
name_label.place(relx=0.44, rely=0.92)
submit_btn = ctk.CTkButton(root, text="create", corner_radius=70, hover_color="#c3bb0b", bg_color="#3b3739", fg_color="dark blue", command=test)
submit_btn.place(relx=0.37, rely=0.8)


root.mainloop()
