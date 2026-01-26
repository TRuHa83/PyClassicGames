import sys
import version

from enum import Enum, auto

from custom.launch     import GameButton

from modules.config    import Config
from modules.update    import Update
from modules.database  import ScoreGames

from ui.score          import Ui_Score
from ui.about_us       import Ui_AboutUs
from ui.main_window    import Ui_MainWindow

from games.datagame    import games
from games.wordle      import Wordle
from games.minesweeper import MinesWeeper
from games.knightstour import KnightsTour

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog,
    QTableWidgetItem, QHeaderView
)


class SelectGame(Enum):
    MINE = auto()
    HORSE = auto()
    WORDLE = auto()
    MENU = auto()


class MainApp:
    def __init__(self):
        self.state = None
        self.data_games = games

        # Cargamos la interfaz
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        # Cargamos las configuraciones
        self.config = Config(self.ui)
        self.setting = self.config.get_setting()
        self.state_update = self.setting.get("update")

        self.path = self.config.get_path()
        self.score_games = ScoreGames(self.path)

        # Agregamos elementos personalizados
        self._add_components()

        # Cargamos el sistema de actualizaciones
        self.update = Update(self.window)

        # Cargamos la puntuación
        self.score = QDialog()
        self.score_ui = Ui_Score()
        self.score_ui.setupUi(self.score)

        # Cargamos Acerca de..
        self.dialog = QDialog()
        self.about_as = Ui_AboutUs()
        self.about_as.setupUi(self.dialog)

        self._setup_connections()
        self._menu()

        self.window.show()

        if self.state_update:
            self.update.auto_check_update()

    def _add_components(self):
        for game in self.data_games.values():
            launch_button = GameButton(game["name"], game["description"], self.path / "assets" / game["icon"])
            self.ui.menu.layout().addWidget(launch_button)

    def _setup_connections(self):
        self.ui.actionMenu.triggered.connect(self._menu)
        self.ui.actionScore.triggered.connect(self._score)

        self.ui.actionMine.triggered.connect(self._minesweeper)
        self.ui.actionHorse.triggered.connect(self._knightstour)
        self.ui.actionWordle.triggered.connect(self._wordle)

        self.ui.actionExit.triggered.connect(sys.exit)

        self.ui.actionCheckRun.triggered.connect(self._update_setting)
        self.ui.actionCheckNow.triggered.connect(self.update.man_check_update)

        self.ui.actionAbout.triggered.connect(self._about)

        self.ui.menu.findChild(GameButton, "button_buscaminas").clicked.connect(self._minesweeper)
        self.ui.menu.findChild(GameButton, "button_salto_del_caballo").clicked.connect(self._knightstour)
        self.ui.menu.findChild(GameButton, "button_wordle").clicked.connect(self._wordle)

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

    def _score(self):
        # Las pestañas de puntuaciones en una lista
        score_tab = [
            self.score_ui.score_mines,
            self.score_ui.score_horse,
            self.score_ui.score_wordle
        ]

        # Puntuaciones de cada juego en una lista
        self.score_game = [
            self.score_games.get_all_score("minesweeper"),
            self.score_games.get_all_score("knightstour"),
            self.score_games.get_all_score("wordle")
        ]

        # Iteramos cada tab con su puntuación
        for sp, score in zip(score_tab, self.score_game):
            # Le damos el ancho maximo a la primera columna
            sp.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

            # Agregamos tantas filas como entradas hay
            sp.setRowCount(len(score))

            # Introducimos los valores en la tabla
            for i, s in enumerate(score):
                sp.setItem(i, 0, QTableWidgetItem(str(s["date"])))
                sp.setItem(i, 1, QTableWidgetItem(str(s["score"])))

        self.score.exec()

    def _about(self):
        self.about_as.label_version.setText(version.__version__)
        self.about_as.label_author.setText(version.__author__)
        self.about_as.label_name.setText(version.__app_name__)

        self.dialog.exec()

    def _update_setting(self):
        self.state_update = self.ui.actionCheckRun.isChecked()
        setting = self.config.get_setting()
        setting["update"] = self.state_update
        self.config.set_setting(setting)

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