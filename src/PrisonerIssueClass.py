import numpy as np
import random
import time

class PrisonerIssue:
    def __init__(self) -> None:
        self.prisoner_number_in_box = random.sample(range(1,101),100)
        self.prisoner_number = 1
    
    def perform_loop_search(self, starting_prisoner: int = None) -> int:
        """method that allows to check how many iterations 

        Args:
            starting_prisoner (int, optional): Can specify which prisoner to use. Defaults to 1.

        Raises:
            Exception: When something gone wrong and there is an endless loop

        Returns:
            int: Iteration when prisoner found his number
        """
        if starting_prisoner:
            box_number_to_check = starting_prisoner - 1
        else:
            box_number_to_check = 0
            
        found_flag: bool = False
        i = 1
        
        while found_flag==False:
            current_number = self.prisoner_number_in_box[box_number_to_check]
            print(f"{i}: Box {box_number_to_check + 1} - Number inside {current_number}")
            if current_number == self.prisoner_number:
                found_flag = True
            else:
                box_number_to_check = current_number - 1
            i += 1
            # time.sleep(0.2)r
            if i > 100:
                raise Exception("whoah! Something gone wrong!")
        return i
        
if __name__ == '__main__':
    issue = PrisonerIssue()
    issue.perform_loop_search()
    