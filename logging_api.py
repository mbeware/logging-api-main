from flask import Flask, jsonify, request
import sys
import os

BASE_LOGFOLDER = "log_files"
app = Flask(__name__)

running_port = sys.argv[1] if len(sys.argv) > 1 else 5000
output_file = sys.argv[2] if len(sys.argv) > 2 else "log.txt"
output_file = sys.argv[2] if len(sys.argv) > 2 else "log.txt"
output_target = os.path.join(BASE_LOGFOLDER ,  output_file)
if not os.path.exists(BASE_LOGFOLDER):
    try :
        os.makedirs(BASE_LOGFOLDER)
    except Exception as e:
        print( f"Erreur à la création du répertoire de log {e}")
        exit(255)

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
        with open(output_target, "a+", encoding="utf-8") as out_file:
                out_file.write(message + "\n")
    except Exception as e: 
         return f"Erreur à l'écriture du log {e}"                
    
    return "Information logged"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=running_port)


