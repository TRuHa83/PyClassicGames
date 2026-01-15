import os
import sys
import sqlite3

from pathlib import Path


class ScoreGames:
    def __init__(self, db_name="score.db"):
        # Comprobar OS y ruta del usuario
        if sys.platform == "win32":
            base_path = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))

        else:
            base_path = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))

        # Crear carpeta el juego
        data_dir = base_path / "PyClassicGames"
        data_dir.mkdir(parents=True, exist_ok=True)

        self.db_path = data_dir / db_name
        self.init_db()

    def connection_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        games = ["minesweeper", "knightstour", "wordle"]

        # Crea la tabla si no existe
        with self.connection_db() as conn:
            for game in games:
                sql_create_table = f"""
                CREATE TABLE IF NOT EXISTS {game} (
                    id     INTEGER PRIMARY KEY AUTOINCREMENT,
                    date   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    score  INTEGER NOT NULL
                );
                """
                conn.execute(sql_create_table)

    def get_best_today(self, game):
        sql = f"SELECT MAX(score) FROM {game} WHERE date(date) = date('now')"

        with self.connection_db() as conn:
            result = conn.execute(sql).fetchone()
            return result[0] if result[0] is not None else 0

    def get_best_history(self, game):
        sql = f"SELECT MAX(score) FROM {game}"

        with self.connection_db() as conn:
            result = conn.execute(sql).fetchone()
            return result[0] if result[0] is not None else 0

    def set_score(self, game, score):
        sql = f"INSERT INTO {game} (score) VALUES (?)"

        with self.connection_db() as conn:
            conn.execute(sql, (score,))
