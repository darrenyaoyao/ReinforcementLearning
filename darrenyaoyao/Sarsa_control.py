from Model import Model

model = Model(100)
model.backward_sarsa_control(100000, 0.1)
model.dump_states("0.1sarsa_result.json")
model.surface_plot()