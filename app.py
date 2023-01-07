import flask
from flask import Flask, request, jsonify
#import sms_provider

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


@app.route('/api/notifyDpt', methods=['POST'])
def notifyDpt():
    # Retrieve the request data
    data = request.get_json()
    message = data.get('message')
    id = data.get('id')

    # Generate the response message
    response_message = f"Chef dpt : {id} notifié"

    # Return the response message as JSON
    return jsonify({'message': response_message +"| "+message})




@app.route('/send_sms', methods=['PUT'])
def send_sms():
  phone_number = request.args.get('phone_number')
  message = request.args.get('message')
  provider_id = request.args.get('sms_provider_id')

  # Check if required parameters are present
  if not phone_number or not message:
    return "Missing required parameters to : "+str(phone_number), 400

  # Use SMS provider module to send the message
  #sms_provider.send_sms(phone_number, message, provider_id)

  return "SMS sent successfully to : "+str(phone_number), 200

@app.route('/send_email', methods=['POST'])
def create_email():
    email_number = request.json.get('email')
    email_provider = request.json.get('email_provider_id')
    email_content = request.json.get('email_content')
    if not email_number or not email_provider or not email_content:
    # Create a new email using the email number, email provider, and email content
    #create_email(email_number, email_provider_id, email_content)
        return 'Email sent succesfully to :'+str(email_number), 201

if __name__ == '__main__':
    app.run()
