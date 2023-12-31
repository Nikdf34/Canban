import tkinter as tk
def create_task(event):
    task = entry.get()
    if task:
        to_do_list.insert(tk.END, task)
        entry.delete(0, tk.END)
def move_task(event, sourse_list, target_list):
    task = sourse_list.get(sourse_list.curselection())
    sourse_list.delete(sourse_list.curselection())
    target_list.insert(tk.END, task)
def clear_all(event):
    to_do_list.delete(0, tk.END)
    in_progress_list.delete(0, tk.END)
    done_list.delete(0, tk.END)
win = tk.Tk()
win.title('Canban board')
to_do_list = tk.Listbox(win, height = 20, width = 40)
in_progress_list = tk.Listbox(win, height = 20, width = 40)
done_list = tk.Listbox(win, height = 20, width = 40)
to_do = tk.Label(win, text = 'to do list', fg = 'red', font = 'Arial')
to_do.grid(row = 0, column = 0, padx = 20, pady = 20)
in_progress = tk.Label(win, text = 'in progress list', fg = 'orange', font = 'Arial')
in_progress.grid(row = 0, column = 1, padx = 20, pady = 20)
done = tk.Label(win, text = 'done list', fg = 'blue', font = 'Arial')
done.grid(row = 0, column = 2, padx = 20, pady = 20)
to_do_list.grid(row = 1, column = 0, padx = 20, pady = 20)
in_progress_list.grid(row = 1, column = 1, padx = 20, pady = 20)
done_list.grid(row = 1, column = 2, padx = 20, pady = 20)
label = tk.Label(win, text = 'add task:', font = 'Arial',)
label.grid(row = 2, column = 0, padx = 20, pady = 20)
entry = tk.Entry(win, width = 40)
entry.grid(row = 2, column = 1, padx = 20, pady = 20)
add_button = tk.Button(win, text = 'add', width = 10, bg = 'red')
add_button.grid(row = 2, column = 2, padx = 20, pady = 20)
deleter = tk.Button(win, text = 'clear', width = 10, bg = 'green')
deleter.grid(row = 3, column = 1, padx = 20, pady = 20)
add_button.bind('<Button-1>', create_task)
to_do_list.bind('<Double-Button-1>', lambda e: move_task(e, to_do_list, in_progress_list))
in_progress_list.bind('<Double-Button-1>', lambda e: move_task(e, in_progress_list, done_list))
deleter.bind('<Button-1>', clear_all)
win.mainloop()