from tkinter import *
from TkUtils import TkUtils as ut
from model.exception.full_hand_exception import FullHandException
from ErrorView import ErrorView
from CardView import CardView
from PIL import Image, ImageTk

class PlayerView:
    def __init__(self, parent, player, refresh_callback):
        self.parent = parent
        self.player = player
        self.refresh_callback = refresh_callback
        self.parent.title(player.get_name())
        self.hand_tree = None       # left: permanent hand
        self.dealt_tree = None      # middle: temp/dealt hand
        self.image_label = None     # right: card preview
        self._build()
        self._refresh()
 
    def _build(self):
        self.parent.configure(background=ut.off_white)
 
        # this creates a three columns with nested frames
        outer = ut.frame(self.parent)
        outer.pack(padx=10, pady=10)
 
        # Left column with the permanent hand
        left = ut.frame(outer)
        left.pack(side=LEFT, padx=(0, 5))
 
        self.hand_tree = ut.treeview(
            left, ("Name", "Attack", "Style", "Health"), multi=False, width=320)
        self.hand_tree.pack()
 
        # select button that is full width fill x
        ut.button(left, "Select", self._select_card).pack(fill=X)
 
        # middle column that deals with temporary cards
        mid = ut.frame(outer)
        mid.pack(side=LEFT, padx=(0, 5))
 
        self.dealt_tree = ut.treeview(mid, ("Card",), multi=False, width=200)
        self.dealt_tree.column("Card", width=200, minwidth=200, stretch=False)
        self.dealt_tree.pack()
 
        # ze place button that also fills x
        ut.button(mid, "Place", self._place_card).pack(fill=X)
 
        # last column of the outer frame that deals with card image
        # bordered frame with fixed size acts as placeholder; replaced
        # by actual card image when a card is selected via _select_card.
        right = ut.frame(outer)
        right.pack(side=LEFT)
 
        # Border frame 1px solid border
        border = Frame(right, bg="black", bd=1, relief=SOLID)
        border.pack()
 
        # pixel container
        IMG_W, IMG_H = 160, 220
        container = Frame(border, width=IMG_W, height=IMG_H, bg=ut.off_white)
        container.pack_propagate(False)
        container.pack(padx=1, pady=1)
 
        self.image_label = Label(container, background=ut.off_white)
        self.image_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self._img_size = (IMG_W, IMG_H)

    # ze helpers again
    # delete all existing rows and reinsert into the model
    def _refresh(self):
        # in the permanent hand
        for row in self.hand_tree.get_children():
            self.hand_tree.delete(row)
        for card in self.player.get_hand():
            self.hand_tree.insert("", "end", values=(card.get_name(), card.get_attack(), str(card.get_style()), card.get_health()))
 
        # in the dealt column
        for row in self.dealt_tree.get_children():
            self.dealt_tree.delete(row)
        for card in self.player.get_temp_hand():
            self.dealt_tree.insert("", "end", values=(card.get_name(),))
 
        if self.refresh_callback:
            self.refresh_callback()
 
    # move temporary dealt card into the player's permanent hand.
    def _place_card(self):
        selected = self.dealt_tree.selection()
        if not selected:
            return
        card_name = self.dealt_tree.item(selected[0])['values'][0]
        card = next((c for c in self.player.get_temp_hand() if c.get_name() == card_name), None)
        if card:
            try:
                self.player.place(card)
                self._refresh()
            except FullHandException as e:
                ErrorView(ut.top_level("Error"), e)
 
    # mark the selected hand card as the one to play and show its image.
    def _select_card(self):
        selected = self.hand_tree.selection()
        if not selected:
            return
        card_name = self.hand_tree.item(selected[0])['values'][0]
        for c in self.player.get_hand():
            if c.get_name() == card_name:
                self.player.select(c)
                # Update card image preview
                img_path = f"image/cards/{card_name.replace(' ', '').lower()}.png"
                try:
                    pil_img = Image.open(img_path).resize((116, 156))
                    photo = ImageTk.PhotoImage(pil_img)
                    self.image_label.config(image=photo, text="", width=116, height=156)
                    self.image_label.image = photo
                except Exception:
                    self.image_label.config(image="", text="No preview", width=120, height=160)
                break
 
    def refresh(self):
        self._refresh()