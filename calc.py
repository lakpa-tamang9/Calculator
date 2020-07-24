import tkinter as tk
# New comment below

HEIGHT = 600
WIDTH = 300
root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = 'gray', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.7, relheight = 0.1, anchor='n')

entry = tk.Entry(frame, font=('Helvetica', 20))
entry.place(relwidth=1, relheight=1)

lower_frame = tk.Frame(root, bg='gray', bd=5)
lower_frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.5, anchor='n')

button = tk.Button(lower_frame, text = "7", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=0, column=0)

button = tk.Button(lower_frame, text = "8", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=0, column=1)

button = tk.Button(lower_frame, text = "9", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=0, column=2)

button = tk.Button(lower_frame, text = "/", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=0, column=3)

button = tk.Button(lower_frame, text = "4", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=1, column=0)

button = tk.Button(lower_frame, text = "5", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=1, column=1)

button = tk.Button(lower_frame, text = "6", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=1, column=2)

button = tk.Button(lower_frame, text = "x", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=1, column=3)

button = tk.Button(lower_frame, text = "1", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=2, column=0)

button = tk.Button(lower_frame, text = "2", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=2, column=1)

button = tk.Button(lower_frame, text = "3", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=2, column=2)

button = tk.Button(lower_frame, text = "-", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=2, column=3)

button = tk.Button(lower_frame, text = "0", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=3, column=0)

button = tk.Button(lower_frame, text = ".", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=3, column=1)

button = tk.Button(lower_frame, text = "+", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=3, column=2)

button = tk.Button(lower_frame, text = "=", font=('Arial', 18), height=2, width=3, anchor = 'n') #placing buttons inside the frame
button.grid(row=3, column=3)

root.mainloop()