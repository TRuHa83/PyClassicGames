import random

from PySide6.QtGui import QAction
from PySide6.QtCore import QObject, QTimer
from PySide6.QtWidgets import QPushButton, QLCDNumber, QMessageBox


class MinesWeeper(QObject):
    def __init__(self, ui_widget, score_games):
        super().__init__()
        self.ui_widget = ui_widget
        self.score_games = score_games

        self.mines = 20 # Cantidad de minas
        self.rows = 16  # Filas
        self.cols = 9   # Columnas


        self.timer = QTimer(self)

        self.grid_btns = [[]] # Matriz de botones

        self._set_variables()
        self._setup_connections()
        self._gen_matriz()

    def _set_variables(self):
        self.flags_remaining = self.mines
        self.real_mines = 0
        self.flags_good = 0
        self.flag = False

        self.seconds = 0

        self.matriz = []

        self.face = {
            -1: "🤯", 0: "😎", 1: "😃",
            2: "😄", 3: "😁", 4: "😆",
            5: "😅", 6: "😂", 7: "😉",
            8: "😍", 9: "🤩"
        }

        self.colors = {
            1: "blue",
            2: "green",
            3: "red",
            4: "darkblue",
            5: "darkred",
            6: "teal",
            7: "black",
            8: "gray"
        }

    def _setup_connections(self):
        # Configuramos el cronometro
        self.timer.timeout.connect(self._clock)

        # Buscamos los widgets en la interfaz
        self.face_btn = self.ui_widget.findChild(QPushButton, "face_btn")
        self.lcd_clock = self.ui_widget.findChild(QLCDNumber, "lcd_clock")
        self.lcd_lags = self.ui_widget.findChild(QLCDNumber, "lcd_lags")
        self.action_reset = self.ui_widget.window().findChild(QAction, "actionReset")

        # Configuramos el botón principal del tablero
        self.face_btn.setText(self.face[1])
        self.face_btn.clicked.connect(self._put_flag)

        # Configuramos los lcd de tiempo
        self.lcd_clock.display(self.seconds)
        self.lcd_clock.setStyleSheet("background-color: black; color: red; border: 1px solid gray;")

        # Configuramos los lcd de las banderas
        self.lcd_lags.display(self.flags_remaining)
        self.lcd_lags.setStyleSheet("background-color: black; color: red; border: 1px solid gray;")

        # Configuramos el botón de reset del menú
        self.action_reset.triggered.connect(self._reset_game)

        # Definimos las conexiones para todos los botones del tablero
        for r in range(self.rows):
            self.grid_btns.append([])

            for c in range(self.cols):
                btn = self.ui_widget.findChild(QPushButton, f"btn_mine_{r}_{c}")
                btn.clicked.connect(self._check_box)
                self.grid_btns[r].append(btn)

    def _reset_game(self):
        self._set_variables()

        for r in range(self.rows):
            for c in range(self.cols):
                btn = self.grid_btns[r][c]
                btn.setEnabled(True)
                btn.setFlat(False)
                btn.setText("")
                btn.setStyleSheet("")

        self.face_btn.setText(self.face[1])
        self.face_btn.setEnabled(True)

        self.lcd_lags.display(self.flags_remaining)
        self.lcd_clock.display(0)

        self._gen_matriz()

    def _clock(self):
        self.seconds += 1
        self.lcd_clock.display(self.seconds)

        if self.real_mines == self.mines:
            self.face_btn.setText("🤩")
            self.face_btn.setEnabled(False)

            for r in range(self.rows):
                for c in range(self.cols):
                    btn = self.grid_btns[r][c]
                    btn.setEnabled(False)
                    if self.matriz[r][c] == -1:
                        if btn.text() == "🚩":
                            btn.setStyleSheet("background-color: green")
                            self.flags_good += 1

            self.timer.stop()
            self._end_game(True)

    def _gen_matriz(self):
        pos_mines = []
        self.pos_negbr = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]

        # Agrega ceros en la matriz
        for r in range(self.rows):
            self.matriz.append([])
            for c in range(self.cols):
                self.matriz[r].append(0)

        # Agrega las minas en posición linear de forma aleatoria
        while self.flags_remaining > len(pos_mines):
            pos = random.randrange(0, 144)
            if pos not in pos_mines:
                pos_mines.append(pos)

        # Agrega las minas a la Matriz y
        # calcula la cantidad de minas vecinas
        for mine in pos_mines:
            row, col = divmod(mine, self.cols)
            self.matriz[row][col] = -1
            for pr, pc in self.pos_negbr:
                nr, nc = row + pr, col + pc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.matriz[nr][nc] != -1:
                        self.matriz[nr][nc] += 1

        self.timer.start(1000)

    def _put_flag(self):
        if not self.flag:
            self.face_btn.setText("🚩")
            self.flag = True
            return

        self.flag = False
        self.face_btn.setText(self.face[1])

    def _flag_mine(self, row, col):
        btn = self.grid_btns[row][col]

        if btn.text() == "🚩":
            btn.setText("")
            self.flags_remaining += 1
            if self.matriz[row][col] == -1:
                self.real_mines -= 1

        elif self.flags_remaining > 0:
            btn.setText("🚩")
            self.flags_remaining -= 1
            if self.matriz[row][col] == -1:
                self.real_mines += 1

        self.lcd_lags.display(self.flags_remaining)

    def _check_box(self):
        sender = self.sender()
        row = int(sender.property("row"))
        col = int(sender.property("col"))

        if self.flag:
            self._flag_mine(row, col)
            return

        if self.matriz[row][col] == 0:
            sender.setEnabled(False)
            sender.setFlat(True)
            self._uncover_zeros(row, col)
            self.face_btn.setText(self.face[0])

        elif self.matriz[row][col] > 0:
            num = self.matriz[row][col]
            self.face_btn.setText(self.face[num])
            sender.setEnabled(False)
            sender.setText(str(num))
            sender.setStyleSheet(f"color: {self.colors[num]}")

        else:
            sender.setEnabled(False)
            sender.setText("💣")
            sender.setStyleSheet("background-color: red")

            self.face_btn.setText(self.face[-1])
            self.face_btn.setEnabled(False)

            for r in range(self.rows):
                for c in range(self.cols):
                    btn = self.grid_btns[r][c]
                    btn.setEnabled(False)
                    if self.matriz[r][c] == -1:
                        if btn.text() == "🚩":
                            btn.setStyleSheet("background-color: green")
                            self.flags_good += 1

                        btn.setText("💣")

            self.timer.stop()
            self._end_game(False)

    def _uncover_zeros(self, row, col):
        queue = [(row, col)]

        while queue:
            r, c = queue.pop(0) # Obtenemos y eliminamos el primer elemento de la cola
            for dr, dc in self.pos_negbr:
                nr, nc = r + dr, c + dc # Obtenemos las posiciones de cada vecino
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.matriz[nr][nc] == 0:
                        btn = self.grid_btns[nr][nc]
                        if btn.isEnabled():
                            btn.setEnabled(False)
                            btn.setFlat(True)
                            queue.append((nr, nc))

                    elif self.matriz[nr][nc] > 0:
                        btn = self.grid_btns[nr][nc]
                        num = str(self.matriz[nr][nc])
                        btn.setText(num)
                        btn.setStyleSheet(f"color: {self.colors[int(num)]}")
                        btn.setEnabled(False)

    def _calculate_score(self):
        # Multiplicador
        multiplier = 10000

        # Uno como mínimo
        time = max(1, self.seconds)

        # Elevamos al cuadrado las banderas correctas
        square = self.flags_good ** 2

        # Calculamos las banderas incorrectas y balanceamos
        incorrect = self.mines - (self.flags_remaining + self.flags_good)
        balance = self.flags_good - incorrect

        # Calculo de la puntuación final
        score = (balance * square * multiplier) / time

        # Devolvemos el resultado redondeado y asegurando que no sea negativo
        return max(0, round(score))

    def _end_game(self, state):
        score = self._calculate_score()
        if score > 0:
            self.score_games.set_score("minesweeper", score)

        best_today = self.score_games.get_best_today("minesweeper")
        best_history = self.score_games.get_best_history("minesweeper")

        if state:
            title = "Felicidades"
            message = f"""
            <h3>¡¡ HAS GANADO !!</h3>
            
            <p>Puntuacion: <b>{str(score)}</b></p>

            <p>· Mejor puntuación del día: <b>{best_today}</b></p>
            <p>· Mejor puntuación historica: <b>{best_history}</b></p>
            """
            QMessageBox.information(self.ui_widget, title, message)

        else:
            title = "Fin del Juego"
            message = f"""
            <h3>¡¡ HAS PERDIDO !!</h3>
            
            <p>Puntuacion: <b>{str(score)}</b></p>

            <p>· Mejor puntuación del día: <b>{best_today}</b></p>
            <p>· Mejor puntuación histórica: <b>{best_history}</b></p>
            <br>
            """
            QMessageBox.critical(self.ui_widget, title, message)

    def exit_game(self):
        self.action_reset.triggered.disconnect(self._reset_game)
        self.timer.stop()
