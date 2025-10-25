import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("To-Do List Application")
window.geometry("1000x1000")

_TaskListbox = []
_CompletedTasks = []
_CategoryTypeList = []


def add_task():
    global _TaskListbox 
    _TaskListbox.append(_AddTaskET.get())
    _AddTaskET.delete(0, tk.END)

def add_category():
    global _CategoryTypeList
    _CategoryTypeList.append(_AddCategoryTypeET.get())
    _AddCategoryTypeET.delete(0, tk.END)


def open_tasks():
    _AddedTasksWindow = tk.Toplevel(window)
    _AddedTasksWindow.title("Your Tasks")
    _TaskListboxLB = tk.Listbox(_AddedTasksWindow)
    tasks = _TaskListbox
    for task in tasks:
        _TaskListboxLB.insert(tk.END, task)   
    _TaskListboxLB.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    _TaskListboxSB = tk.Scrollbar(_AddedTasksWindow)
    _TaskListboxSB.pack(side=tk.RIGHT, fill=tk.BOTH)
    _TaskListboxLB.config(yscrollcommand=_TaskListboxSB.set)
    _TaskListboxSB.config(command=_TaskListboxLB.yview)
    _deleteTaskBT = ttk.Button(_AddedTasksWindow, text="Delete Task", command=lambda: delete_task(_TaskListboxLB))
    _deleteTaskBT.pack()
    _CompletedTasksBT = ttk.Button(_AddedTasksWindow, text="Task Completed", command=lambda: mark_task_completed(_TaskListboxLB))
    _CompletedTasksBT.pack()

def mark_task_completed(listbox):
    selected_Task = listbox.curselection()
    for index in reversed(selected_Task):
        global _CompletedTasks
        _CompletedTasks.append(_TaskListbox[index])
        listbox.delete(index)
        del _TaskListbox[index]

def delete_task(listbox):
    selected_Task = listbox.curselection()
    for index in reversed(selected_Task):
        listbox.delete(index)
        del _TaskListbox[index]

def open_completed_tasks():
    _CompletedTasksWindow = tk.Toplevel(window)
    _CompletedTasksWindow.title("Completed Tasks")
    _CompletedTasksLB = tk.Listbox(_CompletedTasksWindow)
    for task in _CompletedTasks:
        _CompletedTasksLB.insert(tk.END, task)
    _CompletedTasksLB.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    _CompletedTasksSB = tk.Scrollbar(_CompletedTasksWindow)
    _CompletedTasksSB.pack(side=tk.RIGHT, fill=tk.BOTH)
    _CompletedTasksLB.config(yscrollcommand=_CompletedTasksSB.set)
    _CompletedTasksSB.config(command=_CompletedTasksLB.yview)

def open_category_types():
    _CategoryTypesWindow = tk.Toplevel(window)
    _CategoryTypesWindow.title("Category Types")
    _CategoryTypesLB = tk.Listbox(_CategoryTypesWindow)
    for category in _CategoryTypeList:
        _CategoryTypesLB.insert(tk.END, category)
    _CategoryTypesLB.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    _CategoryTypesSB = tk.Scrollbar(_CategoryTypesWindow)
    _CategoryTypesSB.pack(side=tk.RIGHT, fill=tk.BOTH)
    _CategoryTypesLB.config(yscrollcommand=_CategoryTypesSB.set)
    _CategoryTypesSB.config(command=_CategoryTypesLB.yview)

_AddTaskLB = ttk.Label(window, text="Add a task")
_AddTaskLB.pack(side=tk.LEFT)
_AddTaskET = ttk.Entry()
_AddTaskET.pack(side=tk.LEFT)
_AddTaskBT = ttk.Button(window, text="Add Task", command=add_task)
_AddTaskBT.pack(side=tk.LEFT)
_OpenTaskBT = ttk.Button(window, text="Open Tasks", command=open_tasks)
_OpenTaskBT.pack(side=tk.RIGHT)
_OpenCompletedTasksBT = ttk.Button(window, text="View Completed Tasks", command=open_completed_tasks)
_OpenCompletedTasksBT.pack(side=tk.RIGHT)
_AddCategoryTypeLB = ttk.Label(window, text="Add a Category")
_AddCategoryTypeLB.pack(side=tk.BOTTOM)
_AddCategoryTypeET = ttk.Entry()
_AddCategoryTypeET.pack(side=tk.BOTTOM)
_AddCategoryTypeBT = ttk.Button(window, text="Add Category", command=add_category)
_AddCategoryTypeBT.pack(side=tk.BOTTOM)
_OpenCategoryTypeBT = ttk.Button(window, text="View Category Types", command=open_category_types)
_OpenCategoryTypeBT.pack(side=tk.BOTTOM)


window.mainloop()