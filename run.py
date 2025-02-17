from model import BirdModel

starter_model = BirdModel(n=1, width=100, height=100)
for _ in range(10):
    starter_model.step()