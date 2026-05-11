import tkinter as tk
from tkinter import messagebox
import threading
import random
import time
import string

SYSTEM_USER = "Free Robux"
SYSTEM_PASS = "FreeRobux2026.Py"

BG = "black"
RED = "#ff2b2b"
WHITE = "#d9d9d9"

root = tk.Tk()
root.title("RBX REWARD TERMINAL")
root.geometry("1400x850")
root.configure(bg=BG)
root.resizable(False, False)

root.bind("<Escape>", lambda e: root.destroy())

# =========================================================
# LOGIN SCREEN
# =========================================================

login_frame = tk.Frame(root, bg=BG)
login_frame.pack(expand=True)

title = tk.Label(
    login_frame,
    text="RBX REWARD TERMINAL",
    fg=RED,
    bg=BG,
    font=("Consolas", 34, "bold")
)

title.pack(pady=30)

subtitle = tk.Label(
    login_frame,
    text="SECURE REWARD ACCESS SYSTEM",
    fg=WHITE,
    bg=BG,
    font=("Consolas", 14)
)

subtitle.pack()

user_label = tk.Label(
    login_frame,
    text="USERNAME",
    fg=RED,
    bg=BG,
    font=("Consolas", 13)
)

user_label.pack(pady=(40, 5))

user_entry = tk.Entry(
    login_frame,
    bg="#111111",
    fg=RED,
    insertbackground=RED,
    width=35,
    font=("Consolas", 14),
    relief="flat"
)

user_entry.pack(ipady=6)

pass_label = tk.Label(
    login_frame,
    text="PASSWORD",
    fg=RED,
    bg=BG,
    font=("Consolas", 13)
)

pass_label.pack(pady=(20, 5))

pass_entry = tk.Entry(
    login_frame,
    show="*",
    bg="#111111",
    fg=RED,
    insertbackground=RED,
    width=35,
    font=("Consolas", 14),
    relief="flat"
)

pass_entry.pack(ipady=6)

status_label = tk.Label(
    login_frame,
    text="",
    fg="white",
    bg=BG,
    font=("Consolas", 12)
)

status_label.pack(pady=15)

# =========================================================
# MAIN TERMINAL
# =========================================================

main_frame = tk.Frame(root, bg=BG)

header = tk.Label(
    main_frame,
    text="RBX REWARD GENERATOR",
    fg=RED,
    bg=BG,
    font=("Consolas", 28, "bold")
)

header.pack(pady=20)

menu = tk.Label(
    main_frame,
    text="""
[01] Reward Scanner
[02] Reward Generator
[03] Reward Injector
[04] Premium Unlock
[05] Server Connection
[06] Pending Reward Sync
""",
    fg=WHITE,
    bg=BG,
    justify="left",
    font=("Consolas", 15)
)

menu.pack()

terminal = tk.Text(
    main_frame,
    bg="#080808",
    fg=RED,
    insertbackground=RED,
    font=("Consolas", 11),
    borderwidth=0,
    highlightthickness=1,
    highlightbackground=RED
)

terminal.pack(fill="both", expand=True, padx=25, pady=25)

# =========================================================
# FUNCTIONS
# =========================================================

def write(text, delay=0.02):

    terminal.insert("end", text + "\n")
    terminal.see("end")

    root.update()

    time.sleep(delay)

def random_ip():

    return ".".join(str(random.randint(1, 255)) for _ in range(4))

def random_token(length=24):

    chars = string.ascii_uppercase + string.digits

    return "".join(random.choice(chars) for _ in range(length))

# =========================================================
# LOGS
# =========================================================

logs = [

    "CONNECTING TO REWARD SERVERS...",
    "VERIFYING ACCOUNT STATUS...",
    "SCANNING PENDING BALANCE...",
    "CONNECTING TO RBX API...",
    "VERIFYING USER SESSION...",
    "CHECKING BONUS ELIGIBILITY...",
    "LOADING REWARD DATABASE...",
    "SYNCING ACCOUNT DATA...",
    "VERIFYING TOKEN STRUCTURE...",
    "CONNECTING TO GLOBAL SERVERS...",
    "REQUESTING REWARD PACKAGE...",
    "FINALIZING REWARD DELIVERY..."
]

# =========================================================
# SIDE WINDOW
# =========================================================

def side_window():

    win = tk.Toplevel(root)

    win.title("LIVE DATA")
    win.geometry("400x250+20+20")
    win.configure(bg=BG)

    txt = tk.Text(
        win,
        bg=BG,
        fg=RED,
        font=("Consolas", 9),
        borderwidth=0
    )

    txt.pack(fill="both", expand=True)

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    while True:

        line = "".join(random.choice(chars) for _ in range(55))

        try:
            txt.insert("end", line + "\n")
            txt.see("end")
            win.update()
        except:
            break

        time.sleep(0.03)

# =========================================================
# TERMINAL SEQUENCE
# =========================================================

def run_terminal():

    threading.Thread(target=side_window, daemon=True).start()

    for i in range(100):

        if i < len(logs):
            write("[SYSTEM] " + logs[i])

        if i % 5 == 0:
            write("[IP] " + random_ip())

        if i % 7 == 0:
            write("[TOKEN] " + random_token())

        if i % 9 == 0:
            write("[SERVER] ONLINE")

        if i % 11 == 0:
            write("[CACHE] VERIFIED")

        time.sleep(0.08)

    write("")
    write("======================================")
    write("REWARD PACKAGE GENERATED")
    write("======================================")
    write("")

    time.sleep(2)

    messagebox.showinfo(
        "RBX REWARD TERMINAL",
        "😂 THIS WAS A PRANK\n\nFree Robux generators are fake."
    )

# =========================================================
# LOGIN FUNCTION
# =========================================================

def login():

    username = user_entry.get()
    password = pass_entry.get()

    if username == SYSTEM_USER and password == SYSTEM_PASS:

        login_frame.pack_forget()

        main_frame.pack(fill="both", expand=True)

        threading.Thread(target=run_terminal, daemon=True).start()

    else:

        status_label.config(text="ACCESS DENIED")

# =========================================================
# LOGIN BUTTON
# =========================================================

login_btn = tk.Button(
    login_frame,
    text="ACCESS SYSTEM",
    command=login,
    bg="#111111",
    fg=RED,
    activebackground="#222222",
    activeforeground=RED,
    relief="flat",
    font=("Consolas", 13, "bold"),
    padx=20,
    pady=10
)

login_btn.pack(pady=25)

# =========================================================
# RUN
# =========================================================

root.mainloop()