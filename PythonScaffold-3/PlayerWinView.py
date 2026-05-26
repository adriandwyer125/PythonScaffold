from tkinter import *
from tkinter import ttk
from TkUtils import TkUtils as ut

class PlayerWinView:
    def __init__(self, parent, winner, exit_callback):
        self.parent = parent
        self.winner = winner
        self.exit_callback = exit_callback
        self.parent.title("Game Over")
        self._build()
 
    # make ze window
    def _build(self):
        self.parent.configure(background=ut.off_white)
 
        # format: "<name> wins!"
        ut.label(self.parent, f"{self.winner.get_name()} wins!").pack(pady=(20, 15), padx=30)
 
        ttk.Separator(self.parent, orient="horizontal").pack(fill=X)
 
        # total health
        ut.text(self.parent, f"Total health: {self.winner.get_total_health()}").pack(pady=20, padx=30)
 
        ttk.Separator(self.parent, orient="horizontal").pack(fill=X)
 
        # close button
        ut.button(self.parent, "Close", self._close).pack(fill=X, pady=(0, 0))
 
    def _close(self):
        self.parent.destroy()
        self.exit_callback()