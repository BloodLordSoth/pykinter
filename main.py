import customtkinter as ctk
import os, time

root = ctk.CTk()
root.title('Pykinter file creator')
root.geometry('500x300')
ctk.set_appearance_mode("dark")
root.configure(bg="#413e40")

def test():
    os.system('clear')
    value = combo.get()
    value_two = text_one.get()
    time.sleep(0.5)
    print('Navigating...\n')
    time.sleep(0.5)
    os.system('cd ~')
    time.sleep(1)
    os.mkdir('pykinter')
    time.sleep(1)
    os.system('cd pykinter')
    os.mkdir(value_two)
    time.sleep(1)
    os.system(f'touch {value}.py')
    time.sleep(1)
    os.system(f'cd {value_two}')
    time.sleep(2)
    print('Completed.')



bg_label = ctk.CTkLabel(root, width=300, height=400, bg_color="#3b3739", text="")
bg_label.place(relx=0.20, rely=0.26)
combo_label = ctk.CTkLabel(root, width=300, height=100, bg_color="#3b3739", text_color="white", font=("Arial",20), text="Select creation type:")
combo_label.place(relx=0.20, rely=-0.07)
dir_label = ctk.CTkLabel(root, text="Directory name:", bg_color="#3b3739", text_color="white")
dir_label.place(relx=0.23, rely=0.32)
combo = ctk.CTkComboBox(root, width=200, height=25, values=["--Pick an option--", "CustomTkinter", "Pygame"])
combo.place(relx=0.3, rely=0.16)
text_one = ctk.CTkEntry(root, placeholder_text="")
text_one.place(relx=0.44, rely=0.31)
submit_btn = ctk.CTkButton(root, text="create", command=test)
submit_btn.place(relx=0.37, rely=0.8)


root.mainloop()
