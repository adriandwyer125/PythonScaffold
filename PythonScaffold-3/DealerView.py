from tkinter import *
from tkinter import ttk
from TkUtils import TkUtils as ut
from PlayerView import PlayerView
from DeckView import DeckView
from PlayerWinView import PlayerWinView
from model.exception.empty_deck_exception import EmptyDeckException
from model.exception.round_not_ready_exception import RoundNotReadyException
from ErrorView import ErrorView
import sys

class DealerView:
    def __init__(self, parent, dealer, login_root):
        self.parent = parent
        self.dealer = dealer
        self.login_root = login_root
        self.player_views = []
        self._score_vars = []   # StringVar list for the 2x2 label grid
 
    def control(self):
        self.parent.title("Dealer")
        self.parent.configure(background=ut.off_white)

        # creates main dealer menu with a frame, labels, buttons, and score grids
        deck_frame = ut.frame(self.parent)
        try:
            main_img = ut.image(deck_frame, "image/deck.png", 220, 150)
            main_img.pack(side=LEFT, padx=20, pady=10)
            main_img.bind("<Button-1>",
                          lambda e: self._open_deck(self.dealer.get_main_deck(), "Main"))
        except Exception:
            Label(deck_frame, text="[Main Deck]", bg=ut.off_white, font="Arial 10").pack(side=LEFT, padx=20, pady=10)
        try:
            sec_img = ut.image(deck_frame, "image/deck.png", 220, 150)
            sec_img.pack(side=LEFT, padx=20, pady=10)
            sec_img.bind("<Button-1>",
                         lambda e: self._open_deck(self.dealer.get_secondary_deck(), "Secondary"))
        except Exception:
            Label(deck_frame, text="[Secondary Deck]", bg=ut.off_white, font="Arial 10").pack(side=LEFT, padx=20, pady=10)
        deck_frame.pack()
 
        ttk.Separator(self.parent, orient="horizontal").pack(fill=X, padx=0, pady=0)
 
        # score grid in 2x2 pattern with Label widgets in a grid. four slots are always shown with unused slots display n/a and a call button
        middle_frame = ut.frame(self.parent)
 
        grid_frame = ut.frame(middle_frame)
        self._score_vars = []
        players = self.dealer.get_players()
        for i in range(4):
            var = StringVar()
            self._score_vars.append(var)
            self._update_score_var(var, i, players)
            lbl = Label(grid_frame, textvariable=var, font="Helvetica 10", background=ut.off_white, anchor=W, width=16)
            lbl.grid(row=i // 2, column=i % 2, padx=10, pady=6, sticky=W)
        grid_frame.pack(side=LEFT, padx=10, pady=8)
 
        # call button that ends game
        call_btn = ut.button(middle_frame, "CALL", self._end_game)
        call_btn.pack(side=LEFT, padx=20, ipadx=18, ipady=10)
        middle_frame.pack()
 
        ttk.Separator(self.parent, orient="horizontal").pack(fill=X, padx=0, pady=0)
 
        # bottom buttons ofc
        btn_frame = ut.frame(self.parent)
        ut.button(btn_frame, "Deal", self._deal).pack(side=LEFT, expand=True, fill=X)
        ut.button(btn_frame, "Play Round", self._play_round).pack(side=LEFT, expand=True, fill=X)
        ut.button(btn_frame, "Exit", self._exit_app).pack(side=LEFT, expand=True, fill=X)
        btn_frame.pack(fill=X)
 
        self.parent.protocol("WM_DELETE_WINDOW", self._exit_app)
 
        # create playerview windows for each active player
        for player in self.dealer.get_players():
            pv = PlayerView(ut.top_level(player.get_name()), player,
                            self._refresh_scores)
            self.player_views.append(pv)
 
        self._refresh_scores()
 
    # ze helpers
    # set a score stringvar to 'player n: <health>' or 'player n: n/a'.
    def _update_score_var(self, var, index, players):
        if index < len(players):
            var.set(f"Player {index + 1}: {players[index].get_total_health()}")
        else:
            var.set(f"Player {index + 1}: N/A")
    # update all four score label vars from the current player list
    def _refresh_scores(self):
        players = self.dealer.get_players()
        for i, var in enumerate(self._score_vars):
            self._update_score_var(var, i, players)
 
    #title format of deck: "<deck type> Deck" eg "main deck" / "secondary deck"
    def _open_deck(self, deck, deck_type):
        # "
        DeckView(ut.top_level(f"{deck_type} Deck"), deck, f"{deck_type} Deck")
 
    def _deal(self):
        try:
            self.dealer.deal()
            for pv in self.player_views:
                pv.refresh()
            self._refresh_scores()
        except EmptyDeckException as e:
            ErrorView(ut.top_level("Error"), e)
 
    def _play_round(self):
        try:
            self.dealer.play()
            for p in self.dealer.get_players():
                p._Player__selected_card = None
            for pv in self.player_views:
                pv.refresh()
            self._refresh_scores()
        except RoundNotReadyException as e:
            ErrorView(ut.top_level("Error"), e)

    # triggered by call button which finds winner by highest health.
    def _end_game(self):
        players = self.dealer.get_players()
        if not players:
            return
        winner = max(players, key=lambda p: p.get_total_health())
        for pv in self.player_views:
            pv.parent.destroy()
        PlayerWinView(ut.top_level("Game Over"), winner, self._exit_app)
 
    def _exit_app(self):
        self.parent.destroy()
        self.login_root.destroy()
        sys.exit(0)