# build 398c93b006
# (auto) 122242
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
