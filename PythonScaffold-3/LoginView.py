from tkinter import *
from TkUtils import TkUtils as ut
from model.player import Player
from model.dealer import Dealer
from DealerView import DealerView
from model.login_model import LoginModel
from ErrorView import ErrorView

#Note that this class is not done!
#This will only add 2 players to the game.

#This structure is following the method shown in the study modules
#You are welcome to change this however you want


class LoginView:

    def __init__(self, root, model):
        self.model = model
        self.root = root
        self.entries = []
        self.avatar_refs = []
    
    def control(self):
        self.root.title("Login")

        # creates a frame to hold the four player columns
        players_frame = ut.frame(self.root)
        players_frame.pack(pady=(20, 20))

        self.entries.clear()
        self.avatar_refs.clear()

        for i in range(4):
            # each player requires an avatar above entry, grouped in its little invisible frame
            player_frame = ut.frame(players_frame)
            player_frame.pack(side=LEFT, padx=15)

            # calls for avatar image with a fallback to a colored box if missing ofc
            try:
                img_label = ut.image(player_frame, "image/avatar.png", 80, 80, background=ut.off_white)
            except Exception:
                img_label = Label(player_frame, text="A", font="Arial 20", width=4, height=2, bg="#cccccc")
            img_label.pack(pady=(0, 10))
            self.avatar_refs.append(img_label)

            # the entry fields, with the first two having default names
            entry = ut.entry(player_frame, f"Player {i+1}" if i < 2 else "")
            entry.pack()
            self.entries.append(entry)

        # zis is for the bottom bbutton bar
        button_frame = ut.frame(self.root)
        start_btn = ut.button(button_frame, "Start Game", self.start)
        start_btn.pack(expand=True, fill=X)
        button_frame.pack(side=BOTTOM, fill=X)

    def start(self):
        players = []
        for entry in self.entries:
            name = entry.get().strip()
            if name:
                players.append(Player(name))
        if len(players) < 2:
            ErrorView(ut.top_level("Error"), "Need at least 2 players to start the game.")
            return

        for p in players:
            self.model.add_to_game(p)

        dealer = Dealer(self.model.get_players())
        self.root.withdraw()
        dealer_tl = ut.top_level("Dealer")
        DealerView(dealer_tl, dealer, self.root).control()

if __name__ == "__main__":
    root = ut.root()
    root.title("Login")   # title for ui is login yues
    LoginView(root, LoginModel()).control()
    root.mainloop()