from tkinter import *
from tkinter import ttk
from TkUtils import TkUtils as ut
from CardView import CardView

class DeckView:
    def __init__(self, parent, deck, title):
        self.parent = parent
        self.deck = deck
        self.parent.title(title)
        self.tree = None
        self._build()
 
    def _build(self):
        self.parent.configure(background=ut.off_white)
 
        # card column that shows the cards in ze deck
        self.tree = ut.treeview(self.parent, ("Card",), multi=False, width=400)
        self.tree.pack(pady=10, padx=10)
 
        self._refresh()
 
        # all the buttons
        btn_frame = ut.frame(self.parent)
        ut.button(btn_frame, "Show Card", self._show_card).pack(
            side=LEFT, expand=True, fill=X)
        ut.button(btn_frame, "Close", self.parent.destroy).pack(
            side=LEFT, expand=True, fill=X)
        btn_frame.pack(fill=X)
 
    def _refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        # insert card name into column
        for card in self.deck.get_cards():
            self.tree.insert("", "end", values=(card.get_name(),))
 
    def _show_card(self):
        selected = self.tree.selection()
        if not selected:
            return
        card_name = self.tree.item(selected[0])['values'][0 ]
        for c in self.deck.get_cards():
            if c.get_name() == card_name:
                CardView(ut.top_level(c.get_name()), c)
                break