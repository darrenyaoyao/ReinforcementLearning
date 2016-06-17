from Model import Model

model = Model(100)
model.MC_control(1000000)
model.surface_plot()
"""for i in range(21):
    for j in range(10):
        print(str(i)+"  "+str(j),end=" ")
        print(model.states[i][j].policy['stick'])
"""
