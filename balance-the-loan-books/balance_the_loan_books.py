from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/assign-loan", methods=['POST'])
def assign():
    if not request.json:
        pass



if __name__ == '__main__':
    app.run(debug=True)
