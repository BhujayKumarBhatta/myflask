# Controllers API

# This doesn't need authentication
@app.route("/api/public")
@cross_origin(headers=['Content-Type', 'Authorization'])
def public():
    response = "Hello from a public endpoint! You don't need to be authenticated to see this."
    return jsonify(message=response)

# This does need authentication
@app.route("/api/private")
@cross_origin(headers=['Content-Type', 'Authorization'])
@requires_auth
def private():
    response = "Hello from a private endpoint! You need to be authenticated to see this."
    return jsonify(message=response)

'''
Did it help?Yes/No

Protect API Endpoints
The routes shown below are available for the following requests:
GET /api/public: available for non-authenticated requests
GET /api/private: available for authenticated requests containing an Access Token with no additional scopes
GET /api/private-scoped: available for authenticated requests containing
 an Access Token with the read:messages scope granted
 
 '''