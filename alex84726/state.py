import random

class State:
    def __init__(self, player_value_sum=0, dealer_value_sum=0, reward=0):
        self.player_value_sum = player_value_sum
        self.dealer_value_sum = dealer_value_sum
        self.reward = reward
        self.policy = { 'hit' :0.5,'stick':0.5}
        
    def getaction(self):
        if player_value_sum < dealer_value_sum:
            return 'hit'
        elif random.random() < self.policy['hit']:
            return 'hit'
        else:
            return 'stick'
    
    def getplayer_value(self):
        return self.player_value_sum

    def getdealer_value(self):
        return self.dealer_value_sum
