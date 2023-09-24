from flask import Flask # import flask

app = Flask(__name__) # create an app instance

@app.route("/") # at the end point /
def hello_World(): # call method hello_world
    return "hello Kishan" # which returns "hello world" 

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)