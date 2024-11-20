import pickle

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)