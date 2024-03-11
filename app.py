from flask import Flask, request, jsonify
from flask_cors import CORS
from kelas import *

app = Flask(__name__,)
CORS(app)

token = "LMq0u8En80qOJI90rKTg6NNlhg5SGh95OApioGeU"


###########################DEFAULT ROUTE######################  
@app.route('/')
def index():
    response_data = {
        "Status": 'Api Ready',
        "query": '/api/jadkul?kelas=[kelas nya]'
    }
    return jsonify(response_data)


####################ERROR HANDLING###########################
@app.route('/maintenance')
def maintenance():
    response_data = {"Status": 'Server Under Maintenance'}
    return jsonify(response_data)

app.errorhandler(500)
def internal_server_error(e):
    response_data = {
        "error": {
        "code": 500,
        "message": "Internal Server Erorr"
            }
        }
    return jsonify(response_data)

@app.errorhandler(404)
def page_not_found_error(e):
    response_data = {
        "error": {
        "code": 404,
        "message": "Page Not Found"
            }
        }
    return jsonify(response_data)

@app.errorhandler(405)
def method_not_allowed_error(e):
    response_data = {
        "error": {
        "code": 405,
        "message": "Method not Allowed"
            }
        }
    return jsonify(response_data)


######################MAIN ROUTE#############################
@app.route('/api/jadkul', methods=['GET'])
def getKelas():
    kelas = request.args.get('kelas')
    url = f"https://baak.gunadarma.ac.id/jadwal/cariJadKul?_token={token}&teks={kelas}"
    if kelas is not None:
        getJadwal = scrape_jadwal(url)
        output = {
         'status':"sukses",   
         'kelas': kelas,
         'jadwal': getJadwal,
     }
        return jsonify(output), 200
    else:
        return jsonify({'error': 'Server kampus Error'}), 400



if __name__ == '__main__':
    app.run(debug=True)