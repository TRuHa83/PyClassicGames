import sys
import version

from pathlib import Path
from enum    import Enum, auto

from modules.database  import ScoreGames

from games.wordle      import Wordle
from games.minesweeper import MinesWeeper
from games.knightstour import KnightsTour

from PySide6.QtGui     import QAction
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore    import QFile, QIODevice

from PySide6.QtWidgets import (
    QApplication, QStackedWidget, QWidget,
    QPushButton, QMenu, QMessageBox
)


class SelectGame(Enum):
    MINE = auto()
    HORSE = auto()
    WORDLE = auto()
    MENU = auto()


class MainApp:
    def __init__(self):
        # Inicializamos el cargador de UI
        self.state = None
        loader = QUiLoader()
        self.score_games = ScoreGames()

        # Construimos la ruta al archivo .ui relativa a este script
        self.path = Path(__file__).parent.absolute()
        ui_path = self.path / "ui/MainWindow.ui"
        ui_file = QFile(ui_path)

        # Intentamos abrir el archivo
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"No se pudo abrir el archivo UI: {ui_path}")
            sys.exit(-1)

        # Cargamos la interfaz y cerramos el archivo
        self.window = loader.load(ui_file)
        ui_file.close()

        # Si la carga falla, salimos
        if not self.window:
            print(loader.errorString())
            sys.exit(-1)

        self.elements()
        self.setup_connections()
        self.menu()

        self.window.show()

    def elements(self):
        # Elementos del menu
        self.menu_game = self.window.findChild(QMenu, "menuGame")

        # Acciones de menu
        self.action_menu = self.window.findChild(QAction, "actionMenu")
        self.action_horse = self.window.findChild(QAction, "actionHorse")
        self.action_mine = self.window.findChild(QAction, "actionMine")
        self.action_wordle = self.window.findChild(QAction, "actionWordle")
        self.action_about = self.window.findChild(QAction, "actionAbout")
        self.action_exit = self.window.findChild(QAction, "actionExit")

        # Paginas
        self.stacked_widget = self.window.findChild(QStackedWidget, "stackedWidget")
        self.menu_page = self.window.findChild(QWidget, "menu")
        self.horse_page = self.window.findChild(QWidget, "horse")
        self.mine_page = self.window.findChild(QWidget, "mine")
        self.wordle_page = self.window.findChild(QWidget, "wordle")

        # Botones
        self.btn_mine = self.window.findChild(QPushButton, "btn_mine")
        self.btn_horse = self.window.findChild(QPushButton, "btn_horse")
        self.btn_wordle = self.window.findChild(QPushButton, "btn_wordle")

    def setup_connections(self):
        self.action_menu.triggered.connect(self.menu)

        self.action_mine.triggered.connect(self.minesweeper)
        self.action_horse.triggered.connect(self.knightstour)
        self.action_wordle.triggered.connect(self.wordle)

        self.action_exit.triggered.connect(sys.exit)

        self.action_about.triggered.connect(self.about)

        self.btn_mine.clicked.connect(self.minesweeper)
        self.btn_horse.clicked.connect(self.knightstour)
        self.btn_wordle.clicked.connect(self.wordle)

    def menu(self):
        self.exit_games()
        self.state = SelectGame.MENU
        self.menu_game.setEnabled(False)
        self.stacked_widget.setCurrentWidget(self.menu_page)

    def minesweeper(self):
        self.exit_games()
        self.state = SelectGame.MINE

        self.menu_game.setEnabled(True)
        self.stacked_widget.setCurrentWidget(self.mine_page)

        self.game_minesweeper = MinesWeeper(self.mine_page, self.score_games)

    def knightstour(self):
        self.exit_games()
        self.state = SelectGame.HORSE
        self.menu_game.setEnabled(True)
        self.stacked_widget.setCurrentWidget(self.horse_page)

        self.game_knightstour = KnightsTour(self.horse_page, self.score_games)

    def wordle(self):
        self.exit_games()
        self.state = SelectGame.WORDLE
        self.menu_game.setEnabled(True)
        self.stacked_widget.setCurrentWidget(self.wordle_page)

        self.game_wordle = Wordle(self.wordle_page, self.score_games)

    def about(self):
        img_path = self.path / "assets" / "logo_128.png"
        img_path = img_path.as_posix()

        title = "Acerca de..."
        message = f"""
        <h2>{version.__app_name__}</h2>

        <br>
        <img src="{img_path}" alt="logo">

        <p><b>Versión:</b> {version.__version__}</p>
        <p><b>Desarrollado por:</b> {version.__author__}</p>
        <p><b>Licencia:</b> MIT License</p>
        
        <p>Aplicación de escritorio que integra juegos clásicos de estrategia y lógica, 
        desarrollada como Ejercicio Final para la asignatura de Desarrollo de Interfaces.</p>
        
        <p><b>Tecnologías:</b><br>
        Python 3.10+ • PySide6 • SQLite • uv</p>
        
        <p><b>Repositorio:</b><br>
        <a href='{version.__github_url__}'>Ver proyecto en GitHub</a></p>

        <br>
        <p>Copyright © {version.__year__}. Todos los derechos reservados.</p>
        """
        QMessageBox.information(self.window, title, message)

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