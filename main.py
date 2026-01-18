import sys
import version

from enum import Enum, auto

from modules.database  import ScoreGames

from ui.AboutUs        import Ui_AboutAs
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

        self._setup_connections()
        self._menu()

        self.window.show()

    def _setup_connections(self):
        self.ui.actionMenu.triggered.connect(self._menu)
        self.ui.actionScore.triggered.connect(self._score)

        self.ui.actionMine.triggered.connect(self._minesweeper)
        self.ui.actionHorse.triggered.connect(self._knightstour)
        self.ui.actionWordle.triggered.connect(self._wordle)

        self.ui.actionExit.triggered.connect(sys.exit)

        self.ui.actionAbout.triggered.connect(self._about)

        self.ui.btn_mine.clicked.connect(self._minesweeper)
        self.ui.btn_horse.clicked.connect(self._knightstour)
        self.ui.btn_wordle.clicked.connect(self._wordle)

    def _menu(self):
        self._exit_games()
        self.state = SelectGame.MENU
        self.ui.menuGame.setEnabled(False)
        self.window.setWindowTitle(version.__app_name__)
        self.ui.stackedWidget.setCurrentWidget(self.ui.menu)

    def _minesweeper(self):
        self._exit_games()
        self.state = SelectGame.MINE

        self.ui.menuGame.setEnabled(True)
        self.window.setWindowTitle("Buscaminas")
        self.ui.stackedWidget.setCurrentWidget(self.ui.mine)

        self.game_minesweeper = MinesWeeper(self.ui.mine, self.score_games)

    def _knightstour(self):
        self._exit_games()
        self.state = SelectGame.HORSE
        self.ui.menuGame.setEnabled(True)
        self.window.setWindowTitle("Salto del Caballo")
        self.ui.stackedWidget.setCurrentWidget(self.ui.horse)

        self.game_knightstour = KnightsTour(self.ui.horse, self.score_games)

    def _wordle(self):
        self._exit_games()
        self.state = SelectGame.WORDLE
        self.ui.menuGame.setEnabled(True)
        self.window.setWindowTitle("Wordle")
        self.ui.stackedWidget.setCurrentWidget(self.ui.wordle)

        self.game_wordle = Wordle(self.ui.wordle, self.score_games)

    def about(self):
        self.about_as.label_version.setText(version.__version__)
        self.about_as.label_author.setText(version.__author__)
        self.about_as.label_name.setText(version.__app_name__)

        self.dialog.exec()

    def _exit_games(self):
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