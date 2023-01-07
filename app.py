import flask
from flask import Flask, request, jsonify

app = flask.Flask(__name__)


data = {
    "name": "name",
    "id": 1,
    "date": "test",
    "content": "test"
}

@app.route('/submit', methods=['POST'])
def submit():
    data = flask.request.get_json()
    name = data['name']
    id = data['id']
    date = data['date']
    content = data['content']

    # You can save the name, id, date, and content to a database here
    print(str(name)+str(id)+str(date)+str(content))
    return 'Complaint added with success'

@app.route('/data', methods=['GET'])
def get_data():
    data = {
        "name": "Test Name",
        "id": 1,
        "date": "DD/MM/YYY",
        "content": "test contenu de justificatif"
    }
    return flask.jsonify(data)

@app.route('/data', methods=['PUT'])
def update_data():
    updated_data = flask.request.get_json()
    data.update(updated_data)
    return 'Success'

@app.route('/api/certifs/<id>', methods=['GET'])
def get_info(id):
    # Retrieve the name and list of items based on the id
    name = 'John Doe'
    items = [
        {'certificate id': 1, 'certificate date': '2022-01-01', 'isapproved': True},
        {'certificate id': 2, 'certificate date': '2022-02-01', 'isapproved': False},
        {'certificate id': 3, 'certificate date': '2022-03-01', 'isapproved': True}
    ]
    num_items = len(items)


    # Return the response as JSON
    return jsonify({'name': name, 'id': id, 'items': items,'taux_certifs': num_items})


@app.route('/api/certifs', methods=['POST'])
def add_item():
    # Retrieve the request data
    data = request.get_json()
    certificate_id = data.get('certificate id')
    certificate_date = data.get('certificate date')
    isapproved = data.get('isapproved')

    # Save the item to the database
    item = {'certificate id': certificate_id, 'certificate date': certificate_date, 'isapproved': isapproved}
    # ...

    # Return a success response
    return jsonify({''+str(item)+'success': True})


@app.route('/api/notify', methods=['POST'])
def notify():
    # Retrieve the request data
    data = request.get_json()
    message = data.get('message')
    id = data.get('id')

    # Generate the response message
    response_message = f"Chef dpt : {id} notifié"

    # Return the response message as JSON
    return jsonify({'message': response_message +"| "+message})

if __name__ == '__main__':
    app.run()
