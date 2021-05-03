#Importing Flask
from Flask import Flask

def home():
    return "Hello"

app = Flask(__main__)

if __main__ == "__main__" :
    app.run()
