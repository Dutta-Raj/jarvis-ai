import pyautogui
import os

def type_text(text):
    pyautogui.write(text)

def shutdown_pc():
    os.system("shutdown /s /t 1")

def restart_pc():
    os.system("shutdown /r /t 1")

def open_notepad():
    os.system("start notepad")

def open_chrome():
    os.system("start chrome")

def open_vscode():
    os.system("code")
