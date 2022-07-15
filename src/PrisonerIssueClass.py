import numpy as np
import random
import time

class PrisonerIssue:
    def __init__(self) -> None:
        # self.prisoner_number_in_box = random.sample(range(1,101),100)
        self.prisoners = [x for x in range(1,101)]
    
    def perform_loop_search(self, starting_prisoner: int = None, print_process:bool = True) -> int:
        """method that allows to check how many iterations 

        Args:
            starting_prisoner (int, optional): Can specify which prisoner to use. Defaults to 1.
            print_process (bool, True): If True it will print the go through loop process. Defaults to True.

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
        i = 0
        
        while found_flag==False:
            i += 1
            current_number = self.prisoner_number_in_box[box_number_to_check]
            
            if print_process:
                print(f"{i:03d}:: Box {(box_number_to_check + 1):03d} - Prisonser {current_number:02d}")
            
            if current_number == starting_prisoner:
                found_flag = True
            else:
                box_number_to_check = current_number - 1
            
            # time.sleep(0.2)r
            if i > 100:
                raise Exception("whoah! Something gone wrong!")
        if print_process:
            print("\n")
        return i
    
    
    def single_run(self) -> bool:
        self.outcome = []
        for x in self.prisoners:
            self.outcome.append(PrisonerIssue.perform_loop_search(self, starting_prisoner = x, print_process=False))
        
        for x in self.outcome:
            if x > 50:
                return False
            else:
                return True
    
    def simulation(self, n):
        output = []
        for i in range(n):
            self.prisoner_number_in_box = random.sample(range(1,101),100)
            output.append(PrisonerIssue.single_run(self))
        
        return output
        
        
        
            
if __name__ == '__main__':
    issue = PrisonerIssue()
    n = 1000000
    otpt = issue.simulation(n)
    print(sum(otpt)/n)
    # issue.perform_loop_search(starting_prisoner = 1)
    # issue.perform_loop_search(starting_prisoner = 2)