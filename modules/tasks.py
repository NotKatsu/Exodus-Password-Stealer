import psutil

from typing import Union

class Tasks:
    def is_running(executable_name: str) -> Union[str, bool]:
        """Check if an executable is running by its name.

        Args:
            executable_name (str): Name of the executable you are looking for.

        Returns:
            Union[str, bool]: Return str which would be an error else return True or False.
        """
        found_exodus: bool = False 
        try:
            for process in psutil.process_iter():
                if executable_name.endswith(".exe") == True:
                    if process.name() == f"{executable_name}" and process.status() == "running":
                        found_exodus: bool = True; return True
                    else:
                        continue
                else:
                    if process.name() == f"{executable_name}.exe" and process.status() == "running":
                        found_exodus: bool = True; return True
                    else:
                        continue
                
            if found_exodus == False:
                return False
                
        except Exception as error:
            return error