import customtkinter as ctk
from utils import summarize_prompt
from backend import query_deepseek  

class PromptArea:
    def __init__(self, parent, chat_area, sidebar):
        self.parent = parent
        self.chat_area = chat_area
        self.sidebar = sidebar

        self.prompt_frame = ctk.CTkFrame(parent, fg_color="#1A1A1A", width=1000)
        self.prompt_frame.pack(side="bottom", fill="x", padx=15, pady=15)

        self.prompt_text = ctk.CTkTextbox(
            self.prompt_frame,
            height=60,
            font=("Arial", 16),
            wrap="word",
            corner_radius=10,
        )
        self.prompt_text.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.placeholder_text = "Inquire"
        self.prompt_text.insert("1.0", self.placeholder_text)
        self.prompt_text.configure(text_color="gray")

        self.prompt_text.bind("<FocusIn>", self.handle_focus_in)
        self.prompt_text.bind("<FocusOut>", self.handle_focus_out)

        self.send_button = ctk.CTkButton(
            self.prompt_frame,
            text="Send",
            command=self.send_prompt,
            width=10, 
            fg_color="#10101a",
            hover_color="#1A1A2A",
            corner_radius=20,
        )
        self.send_button.pack(side="right", padx=(4, 0))

    def handle_focus_in(self, event):
        current_text = self.prompt_text.get("1.0", "end").strip()
        if current_text == self.placeholder_text:
            self.prompt_text.delete("1.0", "end")
        self.prompt_text.configure(text_color="white")

    def handle_focus_out(self, event):
        current_text = self.prompt_text.get("1.0", "end").strip()
        if not current_text:
            self.prompt_text.insert("1.0", self.placeholder_text)
            self.prompt_text.configure(text_color="gray")

    def send_prompt(self):
        prompt = self.prompt_text.get("1.0", "end").strip()
        if prompt and prompt != self.placeholder_text:
            #user message in the chat area
            user_message = ctk.CTkLabel(
                master=self.chat_area.chat_frame,
                text=prompt,
                fg_color="#333333",
                text_color="lightblue",
                corner_radius=10,
                anchor="e",
                wraplength=400,
                justify="right",
            )
            user_message.pack(pady=10, padx=10, anchor="e")

            # Clear the prompt text area
            self.prompt_text.delete("1.0", "end")
            if not self.prompt_text.get("1.0", "end").strip():
                self.prompt_text.insert("1.0", self.placeholder_text)
                self.prompt_text.configure(text_color="gray")

            # summarized prompt
            summarized_prompt = summarize_prompt(prompt)
            self.sidebar.add_history_item(summarized_prompt)

            # Querying the AI model from backend
            ai_response_text = query_deepseek(prompt)

            # Displaying AI response 
            ai_response = ctk.CTkTextbox(
                master=self.chat_area.chat_frame,
                height=100,
                font=("Arial", 14),
                wrap="word",
                fg_color="#1A1A2A",
                text_color="white",
                corner_radius=10,
                state="normal",
            )
            ai_response.insert("1.0", f"{ai_response_text}")
            ai_response.configure(width=600)
            ai_response.pack(pady=10, padx=10, anchor="w")
