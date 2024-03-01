import customtkinter as ctk

class textarea():
    def __init__(self, parent_frame, screen_width, rf, screen_height):
        self.parent_frame = parent_frame
        self.screen_width = screen_width
        self.rf = rf
        self.text_area = ctk.CTkTextbox(parent_frame, height= screen_height, width = rf, activate_scrollbars = True, wrap = 'none')
        self.text_area.grid(row = 0, column = 1, sticky = 'nsew')
        self.text_area.configure(padx = 10, pady = 10,takefocus = True)
    