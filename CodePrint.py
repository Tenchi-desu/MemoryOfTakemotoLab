from flask import Flask, Response
import requests

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    url = 'https://raw.githubusercontent.com/Tenchi-desu/MemoryOfTakemotoLab/main/index.html'
    response = requests.get(url)
    if response.status_code == 200:
        return Response(response.content, mimetype='text/html')

@app.errorhandler(404)
def page_not_found(error):
    return Response("404 - Not Found Memories ...", status=404)

@app.errorhandler(500)
def page_not_found(error):
    return Response("500 - Too many Memories To Process !!", status=500)

if __name__ == '__main__':
    app.run(port=8000, debug=False)