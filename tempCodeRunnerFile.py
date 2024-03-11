
def not_found(error):
  return jsonify(error="Not Found", message="The requested URL was not found on the server."), 404
