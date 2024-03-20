from flask import Flask

app = Flask(__name__)

@app.route("/")

def read_front():
    with open('index.html') as front_file:
        front = front_file.read()
        return front
        
result = read_front()

def show_message():
    # return "<html><head><style>*{font-family: Arial, sans-serif;}</style></head><body><center><h1>Flask Py Test</h1></center></body></html>"
    return result