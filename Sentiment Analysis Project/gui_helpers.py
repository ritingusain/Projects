import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

def create_gui():
    gui = ThemedTk(theme="arc")
    gui.title("Sentiment Analyzer")
    gui.geometry("900x600")
    return gui

def create_widgets(gui, detect_sentiment_func, clear_func):
    style = ttk.Style()
    style.configure('Custom.TButton', font=('Arial', 10))
    style.configure('Custom.TLabel', font=('Arial', 10))
    style.configure('Custom.TEntry', font=('Arial', 10))

    main_frame = ttk.Frame(gui, padding=20)
    main_frame.grid(row=0, column=0, sticky="nsew")
    gui.grid_rowconfigure(0, weight=1)
    gui.grid_columnconfigure(0, weight=1)

    left_frame = ttk.Frame(main_frame)
    left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    main_frame.grid_columnconfigure(0, weight=2)

    ttk.Label(left_frame, text="Enter Your Text:", style='Custom.TLabel').grid(row=0, column=0, sticky="w", pady=(0, 5))
    
    text_area = tk.Text(left_frame, height=5, width=50, font=("Arial", 10))
    text_area.grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky="ew")

    ttk.Button(left_frame, text="Check Sentiment", command=detect_sentiment_func, style='Custom.TButton').grid(row=2, column=0, columnspan=2, pady=(0, 20), sticky="ew")

    ttk.Label(left_frame, text="Results:", style='Custom.TLabel').grid(row=3, column=0, sticky="w", pady=(0, 5))



    results_frame = ttk.Frame(left_frame)
    results_frame.grid(row=4, column=0, columnspan=2, sticky="ew")

    labels = ["Negative:", "Neutral:", "Positive:", "Overall:", "Emotion:"]
    fields = []

    for i, label in enumerate(labels):
        ttk.Label(results_frame, text=label, style='Custom.TLabel').grid(row=i, column=0, sticky="w", pady=2)
        entry = ttk.Entry(results_frame, width=30, style='Custom.TEntry')
        entry.grid(row=i, column=1, sticky="ew", padx=(10, 0), pady=2)
        fields.append(entry)

    button_frame = ttk.Frame(left_frame)
    button_frame.grid(row=5, column=0, columnspan=2, pady=(20, 0), sticky="ew")

    ttk.Button(button_frame, text="Clear", command=clear_func, style='Custom.TButton').pack(side="left", expand=True, fill="x", padx=(0, 5))
    ttk.Button(button_frame, text="Exit", command=gui.quit, style='Custom.TButton').pack(side="right", expand=True, fill="x", padx=(5, 0))

    right_frame = ttk.Frame(main_frame)
    right_frame.grid(row=0, column=1, sticky="nsew", padx=(20, 0))
    main_frame.grid_columnconfigure(1, weight=1)

    ttk.Label(right_frame, text="Sentiment Distribution:", style='Custom.TLabel').grid(row=0, column=0, sticky="w", pady=(0, 5))

    pie_chart_label = ttk.Label(right_frame)
    pie_chart_label.grid(row=1, column=0, pady=(0, 10))

    return text_area, *fields, pie_chart_label

def add_file_button(gui, command):
    ttk.Button(gui, text="Analyze File", command=command, style='Custom.TButton').grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

def add_youtube_button(gui, command):
    ttk.Button(gui, text="Analyze YouTube Comments", command=command, style='Custom.TButton').grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew")
