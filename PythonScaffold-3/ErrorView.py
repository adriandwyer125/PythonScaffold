from tkinter import *
from TkUtils import TkUtils as ut

class ErrorView:
    def __init__(self, parent, error):
        self.parent = parent
        if isinstance(error, Exception):
            self.exc_name = type(error).__name__
            self.message = str(error)
        else:
            self.exc_name = None
            self.message = str(error)
        self._build()
 
    def _build(self):
        self.parent.title("Error")
        self.parent.configure(background=ut.off_white)
 
        try:
            ut.image(self.parent, "image/error.png", 120, 120).pack(pady=(15, 5))
        except Exception:
            pass
 
        # exception class that makes error label is monolabel red
        if self.exc_name:
            ut.error_label(self.parent, self.exc_name).pack(pady=(10, 2), padx=20)
 
        # makes some readable text at the bottom describing error
        ut.text(self.parent, self.message).pack(pady=(2, 10), padx=20)
 
        ut.button(self.parent, "Close", self.close).pack(fill=X, pady=(5, 0))
 
        self.parent.grab_set()
        self.parent.protocol("WM_DELETE_WINDOW", self.close)
 
    def close(self):
        self.parent.destroy()