import random

from PySide6.QtGui import QAction
from PySide6.QtCore import QObject, Qt, QEvent, QTimer
from PySide6.QtWidgets import QPushButton, QMessageBox, QLabel


def secret_word():
    index = random.randint(0, 484)
    with open("data/words.txt", 'r', encoding='utf-8') as f:
        for i, linea in enumerate(f):
            if i == index:
                word = linea.strip().lower()
                return word


class Wordle(QObject):
    def __init__(self, ui_widget, score_games):
        super().__init__()
        self.ui_widget = ui_widget
        self.score_games = score_games

        self.rows = 5
        self.cols = 4

        self.timer = QTimer(self)

        # ESTILOS
        self.neutro = """
        color: rgb(0, 0, 0);
        background-color: rgb(255, 255, 255);
        """
        self.verde = """
        background-color: rgb(51, 209, 122);
        color: rgb(255, 255, 255);
        """
        self.orange = """
        color: rgb(255, 255, 255);
        background-color: rgb(255, 190, 111);
        """
        self.grey = """
        color: rgb(255, 255, 255);
        background-color: rgb(154, 153, 150);
        """

        self.grid_btns = [[]]
        for r in range(6):
            self.grid_btns.append([])
            for c in range(5):
                btn = self.ui_widget.findChild(QPushButton, f"btn_wordle_{r}_{c}")
                self.grid_btns[r].append(btn)

        self.load_words()
        self.set_variables()
        self.setup_connections()

    def set_variables(self):
        self.clean_board()
        self.word = secret_word()
        self.score = 5000

        self.turn = 0
        self.user_word = []
        self.finished = False

    def clean_board(self):
        for r in range(6):
            for c in range(5):
                btn = self.grid_btns[r][c]
                btn.setText("")
                btn.setStyleSheet(self.neutro)

    def setup_connections(self):
        # Configuramos el cronometro
        self.timer.timeout.connect(self.clock)

        # Configuramos el botón de reset del menú
        self.action_reset = self.ui_widget.window().findChild(QAction, "actionReset")
        self.label_score = self.ui_widget.findChild(QLabel, "label_score")

        self.action_reset.triggered.connect(self.reset_game)
        self.update_score()

        # Activamos los eventos externos
        self.ui_widget.installEventFilter(self)

    def eventFilter(self, source, event):
        if not self.finished:
            # Cualquier pulsación de teclado
            if event.type() == QEvent.KeyPress:
                key = event.key()
                # Teclas de la A a la Z y la Ñ
                if Qt.Key_A <= key <= Qt.Key_Z or key == Qt.Key_Ntilde:
                    if len(self.user_word) < 5:
                        letter = event.text()
                        self.user_word.append(letter.lower())
                        self.write_letter(letter.upper())
                    return True

                # Tecla de RETROCESO
                elif key == Qt.Key_Backspace:
                    if len(self.user_word) > 0:
                        self.user_word.pop()
                        self.remove_letter()
                    return True

                # Tecla SUPRIMIR
                elif key == Qt.Key_Delete:
                    self.user_word = []
                    self.erase_word()
                    return True

                # Teclas ENTER y RETURN
                elif key == Qt.Key_Enter or key == Qt.Key_Return:
                    if len(self.user_word) == 5:
                        self.send_word()
                    return True

        return super().eventFilter(source, event)

    def clock(self):
        self.score -= 1
        self.update_score()

    def reset_game(self):
        self.timer.stop()
        self.set_variables()

        self.label_score.setText(str(self.score))

    def load_words(self):
        self.valid_words = []
        with open("data/valid_words.txt", 'r', encoding='utf-8') as f:
            for linea in f:
                self.valid_words.append(linea.strip().lower())

    def erase_word(self):
        for n in range(5):
            btn = self.grid_btns[self.turn][n]
            btn.setText("")

    def write_letter(self, letter):
        btn = self.grid_btns[self.turn][len(self.user_word) - 1]
        btn.setText(letter)

    def remove_letter(self):
        btn = self.grid_btns[self.turn][len(self.user_word)]
        btn.setText("")

    def send_word(self):
        # Unimos todas las letras en una única palabra
        word = "".join(self.user_word)

        # Por defecto la palabra es verdadera a menos que se demuestre lo contrario
        self.valid = True
        if word in self.valid_words:
            # Evaluamos las letras de la palabra introducida
            for n, letter in enumerate(self.user_word):
                if letter == self.word[n]:
                    btn = self.grid_btns[self.turn][n]
                    btn.setStyleSheet(self.verde)

                elif letter in self.word:
                    btn = self.grid_btns[self.turn][n]
                    btn.setStyleSheet(self.orange)
                    self.score -= 50
                    self.valid = False

                else:
                    btn = self.grid_btns[self.turn][n]
                    btn.setStyleSheet(self.grey)
                    self.score -= 100
                    self.valid = False

            # Actualizamos la puntuación mostrada
            self.update_score()

            # Evaluamos si ha terminado el juego
            if self.is_finish():
                return

            # Siguiente turno
            self.turn += 1
            self.score -= 200

            if self.turn == 1:
                self.timer.start(1000)

        else:
            self.erase_word()

        self.user_word = []

    def update_score(self):
        self.label_score.setText(str(self.score))

    def is_finish(self):
        if self.valid or self.turn == 5:
            self.timer.stop()

            self.score_games.set_score("wordle", self.score)

            best_today = self.score_games.get_best_today("wordle")
            best_history = self.score_games.get_best_history("wordle")

            self.finished = True
            if self.valid:
                title = "Felicidades"
                message = f"""
                <h3>¡¡ HAS AVERIGUADO LA PALABRA SECRETA !!</h3>

                <p>Puntuación: <b>{str(self.score)}</b></p>

                <p>· Mejor puntuación del día: <b>{best_today}</b></p>
                <p>· Mejor puntuación historica: <b>{best_history}</b></p>
                """
                QMessageBox.information(self.ui_widget, title, message)

            else:
                title = "Fin del Juego"
                message = f"""
                <h3>¡¡ HAS PERDIDO, PARTIDA TERMINADA !!</h3>
                <p> La palabra secreta era <b>{self.word.upper()}</b></p> 

                <p>Puntuación: <b>{str(self.score)}</b></p>

                <p>· Mejor puntuación del día: <b>{best_today}</b></p>
                <p>· Mejor puntuación histórica: <b>{best_history}</b></p>
                """
                QMessageBox.critical(self.ui_widget, title, message)

        return self.finished

    def exit_game(self):
        self.action_reset.triggered.disconnect(self.reset_game)
        self.ui_widget.removeEventFilter(self)
        self.timer.stop()
