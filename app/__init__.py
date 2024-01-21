import pickle
from flask import Flask

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

from app import views