from flask import Flask, jsonify, request
import sys
import os
import argparse

app = Flask(__name__)


def SetGlobal(args):
    global running_port
    global output_file
    running_port = args.port
    output_file = args.logfile  

def setup_argparsers():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000, help='port number')
    parser.add_argument('-l','--logfile', type=str, default='/var/log/logging_api.log', help='log file location')
    parser.set_defaults(func=SetGlobal)
    return parser
    

@app.route('/', methods=['POST'])
def racine_post():
    if request.is_json:
        message = str(request.json)
    elif request.data :
        message = request.data.decode("utf-8")
    elif request.form :
         message = str(request.form)
    elif request.args :
         message = str(request.args)
    else :
        message = str(request)
    try :
        with open(output_file, "a+", encoding="utf-8") as out_file:
                out_file.write(message + "\n")
    except Exception as e: 
         return f"Erreur à l'écriture du log {output_file} : {e}"                
    
    return f"Information logged in {output_file})"


if __name__ == '__main__':
    parser = setup_argparsers()
    args = parser.parse_args()
    args.func(args)

    app.run(host="0.0.0.0", port=running_port)


