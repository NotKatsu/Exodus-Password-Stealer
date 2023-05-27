import pygetwindow

class Current_Window:
    def fetch_one() -> str:
        return pygetwindow.getActiveWindow()
        