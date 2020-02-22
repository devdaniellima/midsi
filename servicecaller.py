import subprocess
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/irisjava', methods=['POST'])
def hello_world():
  return subprocess.check_output('java -jar Iris.jar "' + request.form['query'] + '"', shell=True).decode('utf-8')


app.run()
