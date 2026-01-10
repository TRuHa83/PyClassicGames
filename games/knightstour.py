from PySide6.QtGui import QAction
from PySide6.QtCore import QObject, QTimer
from PySide6.QtWidgets import QPushButton, QLCDNumber, QMessageBox


class KnightsTour(QObject):
    def __init__(self, ui_widget, score_games):
        super().__init__()
        self.ui_widget = ui_widget
        self.score_games = score_games

        self.rows = 8
        self.col = 8

        self.timer = QTimer(self)
        self.milis = 0

        self.count = 0
        self.last_pos = None
        self.moves = [
            (-2, -1), (-2, 1), # arriba
            (-1, -2), (-1, 2), # izquierda
            (1, -2), (1, 2),   # derecha
            (2, -1), (2, 1)    # abajo
        ]

        self.setup_connections()

    def setup_connections(self):
        # Configuramos el cronometro
        self.timer.timeout.connect(self.clock)

        # Configuramos el lcd de moviminetos
        self.lcd_score = self.ui_widget.findChild(QLCDNumber, "lcd_horse_score")
        self.lcd_score.display(self.count)

        # Configuramos el botón de reset del menú
        self.action_reset = self.ui_widget.window().findChild(QAction, "actionReset")
        self.action_reset.triggered.connect(self.reset_game)

        # Definimos las conexiones para todos los botones del tablero
        for r in range(self.rows):
            for c in range(self.col):
                btn = self.ui_widget.findChild(QPushButton, f"btn_horse_{r}_{c}")
                btn.clicked.connect(self.check_box)

    def reset_game(self):
        self.count = 0
        self.milis = 0
        self.last_pos = None

        self.lcd_score.display(self.count)

        for r in range(self.rows):
            for c in range(self.col):
                btn = self.ui_widget.findChild(QPushButton, f"btn_horse_{r}_{c}")
                btn.setEnabled(True)
                btn.setText("")

                style = btn.styleSheet()
                if "darkblue" in style:
                    btn.setStyleSheet(style.replace("darkblue", "grey"))

                elif "red" in style:
                    btn.setStyleSheet(style.replace("red", "grey"))

    def clock(self):
        self.milis += self.timer.interval()

    def check_box(self):
        sender = self.sender()
        row = int(sender.property("row"))
        col = int(sender.property("col"))

        if self.last_pos is None:
            self.timer.start(100)

        self.last_pos = (row, col)
        moves = self.change_states(self.last_pos)

        sender.setEnabled(False)
        sender.setText("🐴")

        style = sender.styleSheet()
        sender.setStyleSheet(style.replace("grey", "red"))

        self.count += 1
        self.lcd_score.display(self.count)

        if self.count == 64:
            self.end_game(True)
            return

        if moves == 0:
            self.end_game(False)

    def change_states(self, last_poss):
        for r in range(self.rows):
            for c in range(self.col):
                btn = self.ui_widget.findChild(QPushButton, f"btn_horse_{r}_{c}")
                btn.setEnabled(False)

                style = btn.styleSheet()
                if "darkblue" in style:
                    btn.setStyleSheet(style.replace("darkblue", "grey"))

                elif "red" in style:
                    btn.setStyleSheet(style.replace("red", "grey"))

        moves = []
        for dx, dy in self.moves:
            row = last_poss[0] + dx
            col = last_poss[1] + dy
            if 0 <= row < self.rows and 0 <= col < self.col:
                btn = self.ui_widget.findChild(QPushButton, f"btn_horse_{row}_{col}")
                if btn.text() == "":
                    moves.append((row, col))

        for move in moves:
            btn = self.ui_widget.findChild(QPushButton, f"btn_horse_{move[0]}_{move[1]}")
            btn.setEnabled(True)

            style = btn.styleSheet()
            btn.setStyleSheet(style.replace("grey", "darkblue"))

        return len(moves)

    def calculate_score(self):
        # Multiplicador
        multiplier = 100

        # Aplicamos un bonus extra a cada movimiento
        bonus = self.count ** 3

        # Realizamos el cálculo
        score = (multiplier * bonus) / self.milis
        return round(score)

    def end_game(self, state):
        self.timer.stop()

        score = self.calculate_score()
        self.score_games.set_score("knightstour", score)

        best_today = self.score_games.get_best_today("knightstour")
        best_history = self.score_games.get_best_history("knightstour")

        if state:
            title = "Felicidades"
            message = f"""
            <h3>¡¡ Has completado todas las casillas. !!</h3>

            <p>Puntuacion: <b>{str(score)}</b></p>

            <p>· Mejor puntuación del día: <b>{best_today}</b></p>
            <p>· Mejor puntuación histórica: <b>{best_history}</b></p>
            """
            QMessageBox.information(self.ui_widget, title, message)

        else:
            title = "Fin del Juego"
            message = f"""
            <h3>¡¡ No te quedan más movimientos !!</h3>

            <p>Puntuacion: <b>{str(score)}</b></p>

            <p>· Mejor puntuación del día: <b>{best_today}</b></p>
            <p>· Mejor puntuación histórica: <b>{best_history}</b></p>
            """
            QMessageBox.critical(self.ui_widget, title, message)

    def exit_game(self):
        self.action_reset.triggered.disconnect(self.reset_game)
        self.timer.stop()
        self.reset_game()
