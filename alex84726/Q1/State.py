import random

class State:
    reward = 0
    def __init__(self, player_value_sum=0, dealer_value_sum=0,process='processing'):
        self.player_value_sum = player_value_sum
        self.dealer_value_sum = dealer_value_sum
        self.process = process
        self.policy = { 'hit' :0.5,'stick':0.5}
        
    def getAction(self):
        if random.random() < self.policy['hit']:
            return 'hit'
        else:
            return 'stick'
"""
    def getplayer_value(self):
        return self.player_value_sum

    def getdealer_value(self):
        return self.dealer_value_sum
    """
    
