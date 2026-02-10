import tkinter as tk
from tkinter import ttk
from tkinter import font

class TaskFlowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TaskFlow")
        self.root.geometry("600x400")
        
        self.current_frame = None
        self.tasks = [
            {"name": "Complete project proposal", "completed": False},
            {"name": "Review meeting notes", "completed": False},
            {"name": "Submit report", "completed": True},
            {"name": "Email client feedback", "completed": False},
            {"name": "Update documentation", "completed": False}
        ]
        self.show_start_page()
    
    def clear_frame(self):
        """Clear current frame"""
        if self.current_frame:
            self.current_frame.destroy()
    
    def toggle_task(self, index, var):
        """Update task completion status"""
        self.tasks[index]["completed"] = var.get()
    
    def add_task(self):
        """Open a dialog to add a new task and refresh the homepage"""
        popup = tk.Toplevel(self.root)
        popup.title("Add Task")
        popup.transient(self.root)
        popup.grab_set()
        popup.geometry("350x120")

        label = tk.Label(popup, text="Task Title:", font=("Arial", 11))
        label.pack(pady=(12,4), anchor=tk.W, padx=10)

        entry_var = tk.StringVar()
        entry = tk.Entry(popup, textvariable=entry_var, width=40)
        entry.pack(padx=10)
        entry.focus_set()

        def add_and_close(event=None):
            title = entry_var.get().strip()
            if title:
                self.tasks.append({"name": title, "completed": False})
                popup.destroy()
                self.show_homepage()

        def cancel():
            popup.destroy()

        btn_frame = tk.Frame(popup)
        btn_frame.pack(pady=10)

        add_btn = tk.Button(btn_frame, text="Add", command=add_and_close, width=10)
        add_btn.pack(side=tk.LEFT, padx=6)
        cancel_btn = tk.Button(btn_frame, text="Cancel", command=cancel, width=10)
        cancel_btn.pack(side=tk.LEFT, padx=6)

        entry.bind("<Return>", add_and_close)
        entry.bind("<Escape>", lambda e: cancel())
    
    def edit_task(self, index):
        """Open a dialog to edit an existing task"""
        popup = tk.Toplevel(self.root)
        popup.title("Edit Task")
        popup.transient(self.root)
        popup.grab_set()
        popup.geometry("350x150")

        label = tk.Label(popup, text="Task Title:", font=("Arial", 11))
        label.pack(pady=(12,4), anchor=tk.W, padx=10)

        entry_var = tk.StringVar(value=self.tasks[index]["name"])
        entry = tk.Entry(popup, textvariable=entry_var, width=40)
        entry.pack(padx=10)
        entry.focus_set()
        entry.select_range(0, tk.END)

        def save_and_close(event=None):
            title = entry_var.get().strip()
            if title:
                self.tasks[index]["name"] = title
                popup.destroy()
                self.show_homepage()

        def delete_task():
            confirm_popup = tk.Toplevel(popup)
            confirm_popup.title("Confirm Delete")
            confirm_popup.transient(popup)
            confirm_popup.grab_set()
            confirm_popup.geometry("500x100")

            msg_label = tk.Label(confirm_popup, text="Are you sure? Deleting this task cannot be undone.", font=("Arial", 12))
            msg_label.pack(pady=15)

            btn_frame = tk.Frame(confirm_popup)
            btn_frame.pack(pady=10)

            def confirm_delete():
                self.tasks.pop(index)
                confirm_popup.destroy()
                popup.destroy()
                self.show_homepage()

            def cancel_delete():
                confirm_popup.destroy()

            yes_btn = tk.Button(btn_frame, text="Yes", command=confirm_delete, width=10, fg="red")
            yes_btn.pack(side=tk.LEFT, padx=6)
            no_btn = tk.Button(btn_frame, text="No", command=cancel_delete, width=10)
            no_btn.pack(side=tk.LEFT, padx=6)

        def cancel():
            popup.destroy()

        btn_frame = tk.Frame(popup)
        btn_frame.pack(pady=10)

        save_btn = tk.Button(btn_frame, text="Save", command=save_and_close, width=8)
        save_btn.pack(side=tk.LEFT, padx=4)
        delete_btn = tk.Button(btn_frame, text="Delete", command=delete_task, width=8)
        delete_btn.pack(side=tk.LEFT, padx=4)
        cancel_btn = tk.Button(btn_frame, text="Cancel", command=cancel, width=8)
        cancel_btn.pack(side=tk.LEFT, padx=4)

        entry.bind("<Return>", save_and_close)
        entry.bind("<Escape>", lambda e: cancel())
    
    def show_start_page(self):
        """Display the start/welcome page"""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="#F4FFF8")
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            self.current_frame,
            text="TaskFlow",
            font=("Courier", 48, "bold"),
            bg="white"
        )
        title_label.pack(pady=80)
        
        # Subtitle
        subtitle_label = tk.Label(
            self.current_frame,
            text="Your Personal Productivity Assistant",
            font=("Arial", 14),
            bg="#F4FFF8",
            fg="gray"
        )
        subtitle_label.pack(pady=10)
        
        # Start button
        start_button = tk.Button(
            
            self.current_frame,
            bg="#8BAAAD",
            text="Get Started",
            font=("Arial", 12),
            command=self.show_homepage,
            padx=30,
            pady=10
        )
        start_button.pack(pady=40)
    
    def show_homepage(self):
        """Display the main homepage"""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="white")
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header_frame = tk.Frame(self.current_frame, bg="lightblue")
        header_frame.pack(fill=tk.X)
        
        header_label = tk.Label(
            header_frame,
            text="TaskFlow - Homepage",
            font=("Arial", 20, "bold"),
            bg="lightblue",
            fg="white"
        )
        header_label.pack(pady=15)
        
        # Content area
        content_frame = tk.Frame(self.current_frame, bg="white")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Task list section
        section1 = tk.Label(
            content_frame,
            text="📋 Your Tasks",
            font=("Arial", 14, "bold"),
            bg="white",
            justify=tk.LEFT
        )
        section1.pack(anchor=tk.W, pady=10)
        
        # Scrollable task frame
        task_container = tk.Frame(content_frame, bg="lightyellow", relief=tk.SUNKEN, bd=1)
        task_container.pack(anchor=tk.W, fill=tk.BOTH, expand=True, ipady=10, ipadx=10)
        
        # Create checkboxes for each task
        for i, task in enumerate(self.tasks):
            task_var = tk.BooleanVar(value=task["completed"])
            
            # Create a frame for each task to hold checkbox and edit button
            task_frame = tk.Frame(task_container, bg="lightyellow")
            task_frame.pack(anchor=tk.W, fill=tk.X, pady=5)
            
            checkbox = tk.Checkbutton(
                task_frame,
                text=task["name"],
                variable=task_var,
                font=("Arial", 11),
                bg="lightyellow",
                command=lambda idx=i, var=task_var: self.toggle_task(idx, var)
            )
            checkbox.pack(side=tk.LEFT, anchor=tk.W)
            
            edit_btn = tk.Button(
                task_frame,
                text="Edit",
                font=("Arial", 9),
                width=6,
                command=lambda idx=i: self.edit_task(idx)
            )
            edit_btn.pack(side=tk.RIGHT, padx=5)
        
        # Button bar at bottom
        button_frame = tk.Frame(self.current_frame, bg="white")
        button_frame.pack(fill=tk.X, padx=20, pady=10)
        
        add_task_btn = tk.Button(
            button_frame,
            text="+ Add Task",
            font=("Arial", 10),
            command=self.add_task
        )
        add_task_btn.pack(side=tk.LEFT, padx=5)
        
        back_btn = tk.Button(
            button_frame,
            text="← Back",
            font=("Arial", 10),
            command=self.show_start_page
        )
        back_btn.pack(side=tk.LEFT, padx=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskFlowApp(root)
    root.mainloop()
