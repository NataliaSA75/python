from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello_world', methods=['GET'])
def say_something():
    data={
        1:"Hello, someone!"
    }
    return jsonify(data)

@app.route('/users/', methods=['GET'])
def getUser():
    id = int(request.args.get("id"))
    pass
    users = {
        1:{
            "name":"Max",
            "age":"23"
        },
        2:{
            "name":"Mix",
            "age":"20"
        },
        3:
        {
            "name":"Nax",
            "age":"4"
        }
    }
    if users.keys().__contains__(id):
        return jsonify(users[id])
    else:
        return jsonify("Error, that key doesn't exist")

if __name__ == "__main__":
    app.run(debug=True)