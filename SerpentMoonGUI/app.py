import os
import pathlib
import tkinter
from datetime import datetime
from tkinter import ttk

from SerpentMoonGUI.calculator import calculate_needed_points, calculate_percentage_done

root_directory = pathlib.Path(__file__).parent.resolve()
image_path = "art\\hunt_logo.ico"
background_image = "art\\bg.png"
f1 = os.path.join(root_directory, image_path)
f2 = os.path.join(root_directory, background_image)


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Serpent Moon Calculator")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.iconbitmap(default=f1)

        self.canvas = tkinter.Canvas(self)
        self.canvas.pack(fill="both", expand=True)

        self.canvas.image = tkinter.PhotoImage(file=f2)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor="nw")

        # Title
        self.canvas.create_text(640, 75,
                                anchor="center",
                                text="Hunt: Showdown - Serpent Moon Calculator",
                                fill="white",
                                font="Helvetica 42 bold")

        # Remaining Time
        day_style = ttk.Style().configure("TLabel",
                                          font="Helvetica 30 bold",
                                          background="black",
                                          foreground="white")
        self.time_remaining = ttk.Label(self.canvas,
                                        text="60:00:00:00",
                                        font="Helvetica 35 bold",
                                        style=day_style)
        self.canvas.create_window(640, 175,
                                  window=self.time_remaining,
                                  anchor="center")

        # Level
        self.canvas.create_text(200, 250,
                                anchor="nw",
                                text="Enter your current event level:",
                                font="Helvetica 22 bold",
                                fill="white")
        self.level_entry = ttk.Entry(self.canvas,
                                     font="Helvetica 25 bold",
                                     width=10,
                                     justify="center")
        self.canvas.create_window(825, 250,
                                  window=self.level_entry,
                                  anchor="nw")

        # Event Points
        self.canvas.create_text(200, 400,
                                anchor="nw",
                                text="Enter your current event points:",
                                font="Helvetica 22 bold",
                                fill="white")
        self.points_entry = ttk.Entry(self.canvas,
                                      font="Helvetica 25 bold",
                                      width=10,
                                      justify="center")
        self.canvas.create_window(825, 400,
                                  window=self.points_entry,
                                  anchor="nw")

        # Button
        button_style = ttk.Style().configure("TButton",
                                             font="Helvetica 20 bold",
                                             width=12)
        self.button = ttk.Button(self.canvas,
                                 text="Submit",
                                 style=button_style,
                                 command=self.on_button_press)
        self.canvas.create_window(825, 475,
                                  window=self.button,
                                  anchor="nw")

        # Answer Label
        self.canvas.create_text(640, 575,
                                anchor="center",
                                text="To finish the event in time you need",
                                font="Helvetica 22 bold",
                                fill="white")
        label_style = ttk.Style().configure("TLabel",
                                            font="Helvetica 20 bold",
                                            background="black",
                                            foreground="white")
        self.answer_label = ttk.Label(self.canvas,
                                      text="411.67 points/day",
                                      style=label_style)
        self.canvas.create_window(640, 625,
                                  window=self.answer_label,
                                  anchor="center")

        # Progress Bar
        self.progress = ttk.Progressbar(self.canvas, orient="horizontal", length=1200, mode="determinate")
        self.canvas.create_window(640, 680, anchor="center", window=self.progress)
        self.countdown()

    def on_button_press(self):
        if not self.level_entry.get().isnumeric() or not self.points_entry.get().isnumeric():
            self.level_entry.delete(0, 200)
            self.points_entry.delete(0, 200)
            return

        level = int(self.level_entry.get())
        points = int(self.points_entry.get())

        self.level_entry.delete(0, 200)
        self.points_entry.delete(0, 200)

        points_needed = calculate_needed_points(level, points)
        if points_needed < 0:
            return
        self.answer_label.configure(text=f"{points_needed} points/day")
        percentage_done = calculate_percentage_done(level, points)
        self.progress["value"] = percentage_done

    def countdown(self):
        remaining_time = datetime(2022, 9, 26, 16, 0, 0) - datetime.now()
        remaining_days = remaining_time.days
        remaining_hours = int(remaining_time.seconds / 3600)
        remaining_minutes = int((remaining_time.seconds % 3600) / 60)
        remaining_seconds = int(remaining_time.seconds % 60)
        self.time_remaining.configure(
            text=f"{remaining_days:02d}:{remaining_hours:02d}:{remaining_minutes:02d}:{remaining_seconds:02d}")
        self.after(1000, self.countdown)
