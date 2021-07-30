from flask import Flask
from flask import request
from flask import jsonify
from DataStore import DataStore
from Dispatcher import Dispatcher
from Loan import Loan

app = Flask(__name__)
data_store = DataStore("D:\Download\small")
dispatcher = Dispatcher(data_store)

@app.route("/assign-loan", methods=['POST'])
def assign():
    """
    possible request json
    {
        "id": 1,
        "amount": 100,
        "interest_rate": 0.1,
        "default_likelihood": 0.01,
        "state": "CA"
    }
    """
    if not request.json:
        return
    loan = Loan(request.json["id"], request.json["amount"], request.json["interest_rate"], request.json["default_likelihood"], request.json["state"])
    facility_id = dispatcher.dispatch(loan)
    return jsonify({'assigned': facility_id})


@app.route("/export", methods=['GET'])
def export():
    # export yields and assignment csv file
    file_url_assignments = data_store.export_assignments()
    file_url_yields = data_store.export_yields()
    return jsonify({'assign': file_url_assignments, "yields": file_url_yields})


if __name__ == '__main__':
    data_store.read_banks()
    data_store.read_facilities()
    data_store.read_covenants()
    app.run(debug=True)
