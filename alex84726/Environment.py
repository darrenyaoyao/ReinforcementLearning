import random

class Environment:
    def __init__(self, agents):
        self.agents = agents
        #agents is dict / keys: processing/win/lose/draw
    def getcard(self):
        num = int(random.randint(0,9)+1)
        if random.random() < 1/3:
            print ('Get red '+str(num))
            return -1*num
        else:
            print ('Get black '+str(num))
            return num

    def agent_hit(self, state):
        new_player_value_sum = state.player_value_sum + self.getcard()
        if (new_player_value_sum > 21) or (new_player_value_sum < 1):
            self.agents['lose'].player_value_sum = new_player_value_sum
            self.agents['lose'].dealer_value_sum = state.dealer_value_sum
            return self.agents['lose']
        else:
            return self.agents['processing'][new_player_value_sum-1][state.dealer_value_sum-1]

    def agent_stick(self, state):
        terminal = False
        new_dealer_value_sum = state.dealer_value_sum
        #dealer get cars
        while not terminal:
            new_dealer_value_sum += self.getcard()
            if new_dealer_value_sum > 17 or new_dealer_value_sum < 1:
                terminal = True
        #judging the game
        if (new_dealer_value_sum > 21) or (new_dealer_value_sum < 1):
            self.agents['win'].dealer_value_sum = new_dealer_value_sum
            self.agents['win'].player_value_sum = state.player_value_sum
            return self.agents['win']
        else:
            if new_dealer_value_sum > state.player_value_sum:
                self.agents['lose'].dealer_value_sum = new_dealer_value_sum
                self.agents['lose'].player_value_sum = state.player_value_sum
                return self.agents['lose']
            elif new_dealer_value_sum < state.player_value_sum:
                self.agents['win'].dealer_value_sum = new_dealer_value_sum
                self.agents['win'].player_value_sum = state.player_value_sum
                return self.agents['win']
            else:
                self.agents['draw'].dealer_value_sum = new_dealer_value_sum
                self.agents['draw'].player_value_sum = state.player_value_sum
                return self.agents['draw']

    def step(self, state, action):
        if action == 'hit':
            return self.agent_hit(state)
        else:
            return self.agent_stick(state)
