import psutil

from typing import Union

class Tasks:
    def is_running(executable_name: str) -> Union[str, bool]:
        try:
            for process in psutil.process_iter():
                if process.name() == executable_name and process.status() == "running":
                    return True
                else:
                    continue
                
        except Exception as error:
            return error