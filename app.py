from flask import Flask, request

app = Flask(__name__)

@app.route('/completed', methods=['POST'])
def complete():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    branch = request.form.get('branch')
    datetime = request.form.get('datetime')
    print(name)
    print(email)
    print(phone)
    print(branch)
    print(datetime)
    return '', 200

if __name__ == '__main__':
    app.run()
