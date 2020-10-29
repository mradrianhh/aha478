import sys
import random

class ProbRandom():
    def __init__(self, dataset, prob_list):
        if len(dataset) != len(prob_list):
            print("Please provide valid inputs. Make sure the lists are of similar length.")
            sys.exit(1)
        
        total = 0
        for value in prob_list:
            total += value
        if total != 1:
            print("Please provide a valid prob_list. Make sure the sum of probabilites are equal to 1.0")
            sys.exit(1)

        self.dataset = dataset
        self.prob_list = prob_list

    def random_data(self):
        index = random.randint(0, len(self.dataset)-1)
        return self.dataset[index]

    def prob_random_data(self):
        return random.choices(self.dataset, self.prob_list)[0]