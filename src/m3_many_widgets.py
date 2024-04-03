import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (4 pts)
#
#   Now, we are going to practice all of our widgets.
#
#   First, create two different frames.
#
#   Next, place widgets in both frames. Your frames should have these widgets
#   in them:
#
#       - Frame 1
#           - Label
#           - Button
#           - Single Line Text Entry
#       - Frame 2
#           - Label
#           - Multi Line Text Entry
#
#   You choose what text to have in the labels and button.
#
#   Make sure you call the pack method on all your widgets and that each widget
#   is in the proper frame.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()

frame_1 = tk.Frame(
    master = window,
    bg = "green",
    borderwidth = 25
)
frame_1.pack()

label_1 = tk.Label(
    master = frame_1,
    text = "I am first!"
)
label_1.pack()

button_1 = tk.Button(
    master = frame_1,
    text = "Button 1"
)
button_1.pack()

entry = tk.Entry(
    master = frame_1
)
entry.pack()

frame_2 = tk.Frame(
    master = window
)
frame_2.pack()

label_2 = tk.Label(
    master = frame_2,
    text = "I am second!"
)
label_2.pack()

text = tk.Text(
    master = frame_2
)
text.pack()

window.mainloop()