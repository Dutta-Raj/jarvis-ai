import customtkinter as ctk
import threading
from assistant import run_jarvis

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Jarvis AI Assistant")
app.geometry("500x400")

title = ctk.CTkLabel(app, text="JARVIS", font=("Arial", 32, "bold"))
title.pack(pady=20)

status = ctk.CTkLabel(app, text="Status: Idle", font=("Arial", 16))
status.pack(pady=10)

def start_jarvis():
    status.configure(text="Listening...")
    threading.Thread(target=run_jarvis).start()

start_btn = ctk.CTkButton(app, text="Start Jarvis", command=start_jarvis, height=50)
start_btn.pack(pady=30)

exit_btn = ctk.CTkButton(app, text="Exit", command=app.destroy, fg_color="red")
exit_btn.pack(pady=10)

app.mainloop()
