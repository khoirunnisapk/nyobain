import os
import pickle

module_dir = os.path.dirname(__file__)  
model_file = open(os.path.join(module_dir, '../assets/motivation.pickle'), "rb")
vector_file = open(os.path.join(module_dir, '../assets/vectorizer.pickle'), "rb")
model = pickle.load(model_file)
vectorizer = pickle.load(vector_file)

def predict(sentence):
    review_vector = vectorizer.transform([sentence])
    result = model.predict(review_vector)
    return result
