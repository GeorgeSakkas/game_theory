import random 
import numpy as np

class game_theory:

    def __init__(self, payoff_matrix):
        self.payoff_matrix = payoff_matrix

    #Define all strategies in the competition
    def strategies(self,player1_history,player2_history,strategy,count,rounds):
        if strategy == 1:
            if not player1_history or not player2_history:
                return 'C'
            else:
                return player2_history[-1]
        elif strategy == 2:
            return 'D'
        elif strategy == 3:
            if count <= rounds/2:
                return 'C'
            else:
                return 'D'
        elif strategy == 4:
            return 'C'
        elif strategy == 5:
            return np.random.choice(['D','C'])
        elif strategy == 6:
            return np.random.choice(['C','D'], p=[0.7,0.3])
    
    #Play a round and return the payoff for each player 
    def play_round(self, player1_action, player2_action):
        return self.payoff_matrix[(player1_action,player2_action)]

        
    #Play the simulation 
    def play_game(self, rounds):
        size = 6  #input the number of strategies
        total_payoff_1_list = [[0] * size for _ in range(size)]
        total_payoff_2_list= [[0] * size for _ in range(size)]
  
        for j in range(size):
            for i in range(size):
                strategy_1=j+1
                strategy_2=i+1

                player1_history=[]
                player2_history=[]
                total_payoff_1=0
                total_payoff_2=0
                count=0

                for _ in range(rounds):

                    player1_action=self.strategies(player1_history,player2_history,strategy_1,count,rounds)
                    player2_action=self.strategies(player2_history,player1_history,strategy_2,count,rounds)

                    payoff_1, payoff_2 = self.play_round(player1_action,player2_action)

                    player1_history.append(player1_action)
                    player2_history.append(player2_action)

                    total_payoff_1+=payoff_1
                    total_payoff_2+=payoff_2
                    count+=1

                    total_payoff_1_list[strategy_1-1][strategy_2-1]=total_payoff_1
                    total_payoff_2_list[strategy_1-1][strategy_2-1]=total_payoff_2

                

        return(total_payoff_1_list,total_payoff_2_list)
            


#Define payoff_matrix for prisoner's dillema 
payoff_matrix = {
    ('C','C'):(3,3),
    ('C','D'):(0,5),
    ('D','C'):(5,0),
    ('D','D'):(1,1)
}

#Create an instance of the class
prisoners_dillema=game_theory(payoff_matrix)

#Get results of the simulation
rounds=200
print(prisoners_dillema.play_game(rounds))

#Get results for the first player
scores_of_player1=prisoners_dillema.play_game(rounds)[0]
print(scores_of_player1)

#Get results for the second player
scores_of_player2=prisoners_dillema.play_game(rounds)[1]
print(scores_of_player2)

#Consistency check, if we take the transpose of the total payoff matrix of the second player it should match the first.
print(prisoners_dillema.play_game(rounds)[0][0][2])
print(prisoners_dillema.play_game(rounds)[1][2][0])

#Get best strategy
best_strategies=[]
for i in range(6):
    best_strategies.append(sum(scores_of_player1[i])/6)

#print best strategies
print(best_strategies)