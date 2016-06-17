from State import State
from Environment import Environment
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import json
from pprint import pprint

class Model:
    def __init__(self,N0):
        self.N0 = N0
        self.states = [[State(i+1, j+1) for j in range(10)] for i in range(21)]
        self.state_win = State(0,0,'win')
        self.state_lose = State(0,0,'lose')
        self.state_draw = State(0,0, 'draw')
        self.agent = {'processing': self.states, 'win': self.state_win, 'lose': self.state_lose, 'draw': self.state_draw}
        self.environment = Environment(self.agent)
        self.stack = []
        #(state,action)

    def MC_control(self,iteration):
        for i in range(iteration):
            del self.stack[:]
            print('Iteration : '+str(i))
            self.currentState = self.states[random.randint(0,9)][random.randint(0,9)]
            while self.currentState.status == 'processing':
                takeAction = self.currentState.getAction()
                self.stack.append((self.currentState , takeAction))
                self.currentState = self.environment.step(self.currentState, takeAction)
            if self.currentState == self.state_win:
                for x in self.stack:
                    x[0].MC_Update_QnN(x[1],1)
                    x[0].MC_Update_policy(self.N0)
            elif self.currentState == self.state_lose:
                for x in self.stack:
                    x[0].MC_Update_QnN(x[1],-1)
                    x[0].MC_Update_policy(self.N0)
            else:
                for x in self.stack:
                    x[0].MC_Update_QnN(x[1],0)
                    x[0].MC_Update_policy(self.N0)
    def surface_plot(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        x = np.arange(1, 11, 1)
        y = np.arange(1, 22, 1)
        z = np.arange(210, dtype = np.float32 ).reshape(21, 10)
        x, y = np.meshgrid(x, y)
        for i in range(10):
            for j in range(21):
                #z[j][i] = self.states[j][i].getmax_value_function()
                z[j][i] = self.states[j][i].policy['stick']
        surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        ax.set_zlim(-1, 1)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()

