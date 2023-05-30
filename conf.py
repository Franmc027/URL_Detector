""" 
Autor: Francisco Moya 
Fecha: 
Descripción: 
"""
import pickle


def load_model(url_model):
    file = open(url_model, 'rb')
    model = pickle.load(file)
    file.close()
    return model
