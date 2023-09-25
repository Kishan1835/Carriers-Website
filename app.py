from flask import Flask, render_template # import flask


app = Flask(__name__) # create an app instance

@app.route("/") # at the end point /
def hello_World(): # call method hello_world
    return render_template('home.html') 

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)