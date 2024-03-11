from flask import Flask, Response
import requests
import jsonify

app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def index():
  url = 'https://raw.githubusercontent.com/Tenchi-desu/MemoryOfTakemotoLab/main/test.html'
  response = requests.get(url)
  if response.status_code == 200:
    return Response(response.content, mimetype='text/html')

@app.errorhandler(404)
def not_found(error):
  return jsonify(error="Not Found", message="The requested URL was not found on the server.as"), 404

@app.errorhandler(500)
def internal_server_error(error):
  return jsonify(error="Internal Server Error", message="An internal server error occurred.as"), 500

app.run(port=8000, debug=True)