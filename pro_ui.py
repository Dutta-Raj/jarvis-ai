import customtkinter as ctk
from PIL import Image
import threading
from assistant import run_jarvis

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("JARVIS AI")
app.geometry("600x500")
app.resizable(False, False)

# ---------- BACKGROUND ----------

bg = ctk.CTkImage(Image.open("assets/bg.png"), size=(600, 500))
bg_label = ctk.CTkLabel(app, image=bg, text="")
bg_label.place(x=0, y=0)

# ---------- LOGO ----------

logo = ctk.CTkImage(Image.open("assets/jervis.png"), size=(120, 120))
logo_label = ctk.CTkLabel(app, image=logo, text="")
logo_label.pack(pady=15)

# ---------- TITLE ----------

title = ctk.CTkLabel(app, text="JARVIS", font=("Arial", 30, "bold"))
title.pack()

# ---------- STATUS ----------

status = ctk.CTkLabel(app, text="System Ready", font=("Arial", 14))
status.pack(pady=5)

# ---------- MIC BUTTON ----------

mic_img = ctk.CTkImage(Image.open("assets/mic.png"), size=(70, 70))
mic_btn = ctk.CTkButton(app, image=mic_img, text="", width=90, height=90)
mic_btn.pack(pady=25)

# ---------- EXIT ----------

exit_btn = ctk.CTkButton(app, text="Exit", command=app.destroy)
exit_btn.pack(pady=10)

# ---------- ANIMATION ----------

size = 70

def animate():
    global size
    size += 2

    if size > 85:
        size = 70

    new_img = ctk.CTkImage(Image.open("assets/mic.png"), size=(size, size))
    mic_btn.configure(image=new_img)

    app.after(120, animate)

if size > 85:
    size = 70

new_img = ctk.CTkImage(Image.open("assets/mic.png"), size=(size, size))
mic_btn.configure(image=new_img)

app.after(120, animate)
animate()

# ---------- LISTEN ----------

def start_listening():
    status.configure(text="Listening...")
    threading.Thread(target=run_jarvis, daemon=True).start()

mic_btn.configure(command=start_listening)

app.mainloop()
