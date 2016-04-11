from Model import Model

model = Model(100)
model.monte_carlo_control(100000, 200)
model.surface_plot()
