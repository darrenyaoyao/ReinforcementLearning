from Model import Model

model = Model(100)
model.MC_control(1000000)
model.surface_plot()
