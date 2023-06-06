# Markov decision process
# First write the Markov chain
# Then think of the agent

#keep on playing or not as a user input
#then present the probs and outcomes to user

import numpy as np

def Markov(correct):
    #correct: probability to answer correctly
    result = np.random.binomial(1,correct)
    if result == 1:
        return 1
    else:
        return 0

class LasVegas:
    def __init__(self):
        self.prizes = [100, 1000, 10000, 50000, 61100] 
        self.probs = [9/10, 3/4, 1/2, 1/10]

    def process(self, prob):
        outcome = Markov(prob)
        if outcome == 1:
            return "win"
        else:
            return "lose"
        
    def game(self): #You can't stop once you've started
        for i in range(len(self.prizes)):
            print("Your current prize is " + str(self.prizes[i]) + ". The probability to win the next bet is " + str(self.probs[i]) + " and the next prize is " + str(self.prizes[i+1]) + ". Wanna keep playing?")
            answer = input()
            if answer == "no":
                break
            else:
                outcome = self.process(self.probs[i])
                print("You " + str(outcome))
                if outcome == "lose":
                    #print("You've lost :(")
                    break
                else:
                    continue
    
# minimal version for the agent

class MiniGame:
    def __init__(self):
        self.prizes = [100, 1000, 10000, 50000, 61100]
        self.probs = [9/10, 3/4, 1/2, 1/10]
        self.outcomes = []
        self.a_prize = [] #accumulated prizes
    
    def play(self):
        for i in range(len(self.prizes)):
            self.a_prize.append[self.prizes[i]]


play = LasVegas()
play.game()

#next step: compute the expectation value of every step (after many samples) to model the agent

# def Markov(prob):
#     #correct: probability to answer correctly
#     result = np.random.binomial(1, prob)
#     if result == 1:
#         return 1
#     else:
#         return 0

# # one loop for playing, one loop for quitting 

# # 1 = play, 0 = quit
# def game(action):
#     for i in range(len(prizes)):
#         if action == 0:
#             break
#         else:
#             outcome = Markov(probs[i])
#             if outcome == 0:
#                 break
#             else:
#                 continue
