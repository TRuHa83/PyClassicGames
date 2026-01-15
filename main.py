import sys
import version

from enum import Enum, auto

from modules.database  import ScoreGames

from ui.AboutAs        import Ui_AboutAs
from ui.MainWindow     import Ui_MainWindow

from games.wordle      import Wordle
from games.minesweeper import MinesWeeper
from games.knightstour import KnightsTour

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog
)


class SelectGame(Enum):
    MINE = auto()
    HORSE = auto()
    WORDLE = auto()
    MENU = auto()


class MainApp:
    def __init__(self):
        self.state = None
        self.score_games = ScoreGames()

        # Cargamos la interfaz
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        # Cargamos Acerca de..
        self.dialog = QDialog()
        self.about_as = Ui_AboutAs()
        self.about_as.setupUi(self.dialog)

        self.setup_connections()
        self.menu()

        self.window.show()

    def setup_connections(self):
        self.ui.actionMenu.triggered.connect(self.menu)

        self.ui.actionMine.triggered.connect(self.minesweeper)
        self.ui.actionHorse.triggered.connect(self.knightstour)
        self.ui.actionWordle.triggered.connect(self.wordle)

        self.ui.actionExit.triggered.connect(sys.exit)

        self.ui.actionAbout.triggered.connect(self.about)

        self.ui.btn_mine.clicked.connect(self.minesweeper)
        self.ui.btn_horse.clicked.connect(self.knightstour)
        self.ui.btn_wordle.clicked.connect(self.wordle)

    def menu(self):
        self.exit_games()
        self.state = SelectGame.MENU
        self.ui.menuGame.setEnabled(False)
        self.ui.stackedWidget.setCurrentWidget(self.ui.menu)

    def minesweeper(self):
        self.exit_games()
        self.state = SelectGame.MINE

        self.ui.menuGame.setEnabled(True)
        self.ui.stackedWidget.setCurrentWidget(self.ui.mine)

        self.game_minesweeper = MinesWeeper(self.ui.mine, self.score_games)

    def knightstour(self):
        self.exit_games()
        self.state = SelectGame.HORSE
        self.ui.menuGame.setEnabled(True)
        self.ui.stackedWidget.setCurrentWidget(self.ui.horse)

        self.game_knightstour = KnightsTour(self.ui.horse, self.score_games)

    def wordle(self):
        self.exit_games()
        self.state = SelectGame.WORDLE
        self.ui.menuGame.setEnabled(True)
        self.ui.stackedWidget.setCurrentWidget(self.ui.wordle)

        self.game_wordle = Wordle(self.ui.wordle, self.score_games)

    def about(self):
        self.about_as.label_version.setText(version.__version__)
        self.about_as.label_author.setText(version.__author__)
        self.about_as.label_name.setText(version.__app_name__)

        self.dialog.exec()

    def exit_games(self):
        if self.state == SelectGame.MINE:
            self.game_minesweeper.exit_game()

        elif self.state == SelectGame.HORSE:
            self.game_knightstour.exit_game()

        elif self.state == SelectGame.WORDLE:
            self.game_wordle.exit_game()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = MainApp()
    sys.exit(app.exec())