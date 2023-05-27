import psutil

from typing import Union

class Tasks:
    def is_running(executable_name: str) -> Union[str, bool]:
        found_exodus: bool = False 
        
        try:
            for process in psutil.process_iter():
                if process.name() == executable_name and process.status() == "running":
                    found_exodus: bool = True; return True
                else:
                    continue
                
            return False
                
        except Exception as error:
            return error