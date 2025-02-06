import customtkinter as ctk
import random

class Sidebar:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.sidebar_frame = ctk.CTkFrame(master=parent, fg_color="#10101a", width=200)
        self.sidebar_frame.pack(side="left", fill="y")

        # List to store history items
        self.history_items = []

        self.create_new_chat_button()
        self.create_prompt_history_section()
        self.create_user_label()

    def create_new_chat_button(self):
        self.new_chat_button = ctk.CTkButton(
            master=self.sidebar_frame,
            text="New Chat +",
            command=lambda: self.app.chat_area.new_chat(),
            fg_color="transparent",
            hover_color="#1A1A2A",
            width=170,
            height=35,
            corner_radius=10,
            font=("Arial", 14),
        )
        self.new_chat_button.pack(pady=(15, 15), padx=15, anchor="n")

        # Hover effects
        self.new_chat_button.bind("<Enter>", self.on_hover_enter_new_chat)
        self.new_chat_button.bind("<Leave>", self.on_hover_leave_new_chat)

    def on_hover_enter_new_chat(self, event):
        self.new_chat_button.configure(fg_color="#1A1A2A", text_color="lightblue")

    def on_hover_leave_new_chat(self, event):
        self.new_chat_button.configure(fg_color="transparent", text_color="white")

    def create_prompt_history_section(self):
        prompt_history_label = ctk.CTkLabel(
            self.sidebar_frame, text="Session History", font=("Arial", 14, "bold")
        )
        prompt_history_label.pack(pady=(20, 10), padx=10)

        # Hover effects for the label
        prompt_history_label.bind("<Enter>", self.on_hover_enter_label)
        prompt_history_label.bind("<Leave>", self.on_hover_leave_label)

        self.prompt_history_frame = ctk.CTkFrame(
            master=self.sidebar_frame, fg_color="transparent", corner_radius=10, width=200
        )
        self.prompt_history_frame.pack(fill="x", padx=10, pady=(0, 10))

    def on_hover_enter_label(self, event):
        event.widget.configure(text_color="lightblue")

    def on_hover_leave_label(self, event):
        event.widget.configure(text_color="white")

    def create_user_label(self):
        random_colors = ["#FF5733", "#33FF57", "#5733FF", "#FF33A6", "#FFC300"]
        self.original_color = random.choice(random_colors)

        self.user_frame = ctk.CTkFrame(
            self.sidebar_frame,
            width=30,
            height=30,
            corner_radius=15,
            fg_color=self.original_color,
        )

        self.user_frame.pack(side="bottom", anchor="w", pady=(30, 30), padx=(15, 5))

        self.user_label = ctk.CTkLabel(
            self.user_frame, text="U", font=("Arial", 14, "bold"), text_color="white"
        )
        self.user_label.place(relx=0.5, rely=0.5, anchor="center")

        # Hover and click effects
        self.user_frame.bind("<Enter>", self.on_hover_enter_user)
        self.user_frame.bind("<Leave>", self.on_hover_leave_user)
        self.user_frame.bind("<Button-1>", self.on_click_user)

    def on_hover_enter_user(self, event):
        light_color = self.lighten_color(self.original_color, 20)
        self.user_frame.configure(fg_color=light_color)
        self.user_label.configure(text_color="lightblue")
        self.user_frame.configure(width=32, height=32, corner_radius=16)

    def on_hover_leave_user(self, event):
        self.user_frame.configure(fg_color=self.original_color)
        self.user_label.configure(text_color="white")
        self.user_frame.configure(width=30, height=30, corner_radius=15)

    def on_click_user(self, event):
        self.user_label.configure(font=("Arial", 18, "bold"))
        self.user_frame.configure(fg_color="blue")
        self.parent.after(300, self.revert_user_label)

    def revert_user_label(self):
        self.user_label.configure(font=("Arial", 14, "bold"))
        self.user_frame.configure(fg_color=self.original_color)

    def lighten_color(self, color, factor):
        color = color.lstrip('#')
        rgb = [int(color[i:i+2], 16) for i in (0, 2, 4)]
        rgb = [min(255, int(c + factor)) for c in rgb]
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

    def add_history_item(self, item):
        # Store the history item
        self.history_items.append(item)

        # New history item added to the sidebar
        history_label = ctk.CTkLabel(
            master=self.prompt_history_frame,
            text=item,
            fg_color="transparent", 
            text_color="white",
            font=("Arial", 12),
            anchor="w",  
            width=180,  
        )
        history_label.pack(pady=(5, 5), padx=10, anchor="w", fill="x") 

        # Bind hover events
        history_label.bind("<Enter>", lambda e, label=history_label: self.on_hover_enter_history_item(label))
        history_label.bind("<Leave>", lambda e, label=history_label: self.on_hover_leave_history_item(label))

    def on_hover_enter_history_item(self, label):
        label.configure(text_color="lightblue", fg_color="#2A2A3A", corner_radius=10)  

    def on_hover_leave_history_item(self, label):
        label.configure(text_color="white", fg_color="transparent") 