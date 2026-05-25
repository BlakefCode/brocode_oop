class GameLogger:
    @staticmethod
    def log(message):
        print(f"[LOG]: {message}")

    @staticmethod
    def error(message):
        print(f"[ERROR]: {message}")