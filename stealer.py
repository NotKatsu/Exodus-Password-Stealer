from typing import Union
from modules.tasks import Tasks

class Exodus_Password_Stealer:
    def check_if_running(executable_name: str) -> Union[str, bool]:
        is_running_result: any = Tasks.is_running(executable_name=executable_name)
        
        if is_running_result == True or is_running_result == False:
            return is_running_result
        else:
            return None