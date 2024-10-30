import sys
from flask import Flask, render_template, request

app = Flask(__name__)
temp = 'no/main.html'

@app.route('/')
def home():
    return render_template(temp)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'prod': # Not sure here
        app.run(host='0.0.0.0', debug=True)
    else:
        app.run(debug=True)
