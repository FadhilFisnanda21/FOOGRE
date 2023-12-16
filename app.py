from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for,
)
from pymongo import MongoClient

SECRET_KEY = 'FOOGRE'

client = MongoClient("mongodb+srv://Test:yoi22@cluster0.poxbckg.mongodb.net/?retryWrites=true&w=majority")
db = client.FOOGRE

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    msg = request.args.get("msg")
    return render_template("login.html", msg=msg)

@app.route("/signup")
def signup():
    return render_template("register.html")

@app.route("/sign_up/save", methods=["POST"])
def sign_up():
    username = request.form.get("username")
    password = request.form.get("password")
    doc = {
        "username": username,
        "password": password
        
    }
    db.user.insert_one(doc)
    return jsonify({"result": "success"})

@app.route("/signin")
def signin():
    return render_template("login.html")

@app.route("/sign_in", methods=["POST"])
def sign_in():
    username = request.form["username"]
    password = request.form["password"]
    print(username)
    print(password)
    result = db.user.find_one(
        {
            "username": username,
            "password": password,
        }
    )
    
    

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/menudetail")
def menudetail():
    return render_template("menudetail.html")

@app.route("/cekpesanan")
def cekpesanan():
    return render_template("cekpesanan.html")

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)