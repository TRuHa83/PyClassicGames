import sqlite3


class ScoreGames:
    def __init__(self, path):
        db_name="score.db"
        self._db_path = path / db_name
        self._init_db()

    def _connection_db(self):
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        games = ["minesweeper", "knightstour", "wordle"]

        # Crea la tabla si no existe
        with self._connection_db() as conn:
            for game in games:
                sql_create_table = f"""
                CREATE TABLE IF NOT EXISTS {game} (
                    id     INTEGER    PRIMARY KEY AUTOINCREMENT,
                    date   TIMESTAMP  DEFAULT CURRENT_TIMESTAMP,
                    score  INTEGER    NOT NULL
                );
                """
                conn.execute(sql_create_table)

    def get_all_score(self, game):
        sql = f"SELECT * FROM {game} ORDER BY score DESC"
    
        with self._connection_db() as conn:
            result = conn.execute(sql).fetchall()
            return result

    def get_best_today(self, game):
        sql = f"SELECT MAX(score) FROM {game} WHERE date(date) = date('now')"

        with self._connection_db() as conn:
            result = conn.execute(sql).fetchone()
            return result[0] if result[0] is not None else 0

    def get_best_history(self, game):
        sql = f"SELECT MAX(score) FROM {game}"

        with self._connection_db() as conn:
            result = conn.execute(sql).fetchone()
            return result[0] if result[0] is not None else 0

    def set_score(self, game, score):
        sql = f"INSERT INTO {game} (score) VALUES (?)"

        with self._connection_db() as conn:
            conn.execute(sql, (score,))
