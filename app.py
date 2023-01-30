from flask import Flask, request

app = Flask(__name__)

@app.route('/completed', methods=['POST'])
def process_post():
    data = request.get_json()
    # process the data received in the POST request
    # ...
    return "Data processed successfully", 200

if __name__ == '__main__':
    app.run(debug=True)
