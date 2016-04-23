from Model import Model

model = Model(100)
model.monte_carlo_control(1000000, 1)
model.dump_states("1000000i_result.json")
model.surface_plot()
