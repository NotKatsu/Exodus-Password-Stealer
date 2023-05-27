import pygetwindow

class Current_Window:
    def fetch_one() -> dict[str]:
        current_active_window: object = pygetwindow.getActiveWindow()
        
        return {"title": current_active_window.title, "width": current_active_window.width, "height": current_active_window.height}
        