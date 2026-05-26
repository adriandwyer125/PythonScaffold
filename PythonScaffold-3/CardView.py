from tkinter import *
from TkUtils import TkUtils as ut

class CardView:
    def __init__(self, parent, card):
        self.parent = parent
        self.card = card
        self._build()
 
    def _build(self):
        self.parent.title(self.card.get_name())
        self.parent.configure(background=ut.off_white)
 
        img_path = f"image/cards/{self.card.get_name().replace(' ', '').lower()}.png"
 
        # create image of ^ at 300x300
        try:
            self.img_label = ut.image(self.parent, img_path, 300, 300)
            self.img_label.pack(pady=(15, 10), padx=15)
        except Exception:
            # if card no exist I cri and just put stats
            ut.label(self.parent, self.card.get_name()).pack(pady=(15, 5))
            ut.text(self.parent, f"Attack: {self.card.get_attack()}").pack()
            ut.text(self.parent, f"Style: {self.card.get_style()}").pack()
            ut.text(self.parent, f"Health: {self.card.get_health()}").pack(pady=(0, 10))
 
        # this for button at bottom ofc
        ut.button(self.parent, "Close", self.parent.destroy).pack(fill=X, pady=(5, 0))