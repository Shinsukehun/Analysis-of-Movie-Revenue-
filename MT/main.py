import customtkinter as ctk
from sidebar import Sidebar
from chat_area import ChatArea
from prompt_area import PromptArea

class App:
    def __init__(self):
        self.app = ctk.CTk(fg_color="#1A1A1A")
        self.app.title("MaxTac")
        self.app.geometry("900x600")

        # Initialize components
        self.sidebar = Sidebar(self.app, self)
        self.chat_area = ChatArea(self.app)
        self.prompt_area = PromptArea(self.app, self.chat_area, self.sidebar)
        self.app.mainloop()

if __name__ == "__main__":
    App()