import pickle


# Saving the model at the folder path given
def save_obj(obj, path):
    with open(path, 'wb')as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


# Loading the model from the given path
def load_obj(path):
    with open(path, 'rb') as f:
        return pickle.load(f)