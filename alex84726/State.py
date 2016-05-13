import random

class State:
    reward = 0
    def __init__(self, player_value_sum=0, dealer_value_sum=0,status='processing'):
        self.player_value_sum = player_value_sum
        self.dealer_value_sum = dealer_value_sum
        self.status = status
        self.action = { 'hit' : [0,0],'stick':[0,0] }
        # action : [Q value, N visited]
        self.policy = { 'hit' :0.5,'stick':0.5}
        
    def getAction(self):
        if random.random() < self.policy['hit']:
            return 'hit'
        else:
            return 'stick'

    def state_visited(self):
        num = self.action['hit'][1] + self.action['stick'][1]
        return num

    def MC_Update_QnN(self, action, reward):
        if action=='hit':
            temp = self.action['hit'][0]
            self.action['hit'][1] += 1
            self.action['hit'][0] = temp + ((reward-temp)/(self.action['hit'][1]))
        elif action=='stick':
            temp = self.action['stick'][0]
            self.action['stick'][1] += 1
            self.action['stick'][0] = temp + ((reward-temp)/(self.action['stick'][1]))
        else:
            print("Warning: error action input")

    def MC_Update_policy(self,N0=100):
        epison = N0/(N0+self.state_visited())
        if (self.action['hit'][0]) > (self.action['stick'][0]):
            self.policy['hit'] = (1 - (epison/2))
            self.policy['stick'] = epison/2
        else:
            self.policy['stick'] = (1 - (epison/2))
            self.policy['hit'] = epison/2


