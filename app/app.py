from flask import Flask, request, Response
import json
import psutil

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
   return 'Hello, World!'


@app.route('/version')
def index():
   return "version 0.0.5"

@app.route('/cpu', methods=['POST', 'GET'])
def cpu():
   cpu = psutil.cpu_times()

   return Response(json.dumps(cpu))

#return Response(json.dumps(cpu), mimetype='application/json')





if __name__ == '__main__':
   app.run(host='0.0.0.0', port=4001, debug=True)
