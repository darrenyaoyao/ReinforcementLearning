from Model import Model

model = Model(100)
model.backward_sarsa_control_linear_function_appro(500000, 0.1)
model.dump_states("0.1sarsa_linearfunction_result.json")
model.surface_plot()