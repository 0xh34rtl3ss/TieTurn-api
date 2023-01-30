from flask import Flask, request

app = Flask(__name__)

@app.route('/completed', methods=['POST'])
def complete():
    name = request.form.get('name')
    print(name)
    return '', 200

if __name__ == '__main__':
    app.run()
