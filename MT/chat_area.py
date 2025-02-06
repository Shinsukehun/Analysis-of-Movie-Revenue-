import customtkinter as ctk

class ChatArea:
    def __init__(self, parent):
        self.parent = parent
        self.chat_frame = ctk.CTkScrollableFrame(parent, fg_color="#1A1A1A", corner_radius=30)
        self.chat_frame.pack(side="top", fill="both", expand=True, padx=30, pady=10)

        # Welcome message
        self.welcome_message = ctk.CTkLabel(
            master=self.chat_frame,
            text="Hi, User!",
            fg_color="#1A1A2A",
            text_color="white",
            corner_radius=10,
            anchor="center",
            wraplength=300,
            justify="center",
            font=("Arial", 16)
        )
        self.welcome_message.pack(pady=2, padx=5, anchor="center")

    def new_chat(self):
        for widget in self.chat_frame.winfo_children():
            widget.destroy()
        self.welcome_message.pack(pady=2, padx=5, anchor="center")