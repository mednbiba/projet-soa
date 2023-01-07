#API Endpoints
The API has the following endpoints:

POST /submit
Submits a complaint with the following data:

name: the name of the person submitting the complaint (string)
id: the id of the person submitting the complaint (integer)
date: the date of the complaint (string)
content: the content of the complaint (string)
GET /data
Gets the current complaint data.

PUT /data
Updates the current complaint data with the following data:

name: the name of the person submitting the complaint (string)
id: the id of the person submitting the complaint (integer)
date: the date of the complaint (string)
content: the content of the complaint (string)
GET /api/certifs/<id>
Gets the name, id, and list of items for a given id. The items contain the following data:

certificate id: the id of the certificate (integer)
certificate date: the date of the certificate (string)
isapproved: a boolean value indicating whether the certificate is approved or not
POST /api/certifs
Adds a new item with the following data:

certificate id: the id of the certificate (integer)
certificate date: the date of the certificate (string)
isapproved: a boolean value indicating whether the certificate is approved or not
POST /api/notify
Notifies the chef dpt with the following data:

message: the message to send (string)
id: the id of the chef dpt to notify (integer)
