from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for,
)

import hashlib
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from datetime import datetime, timedelta
import jwt

import os
from os.path import join, dirname
from dotenv import load_dotenv


SECRET_KEY = 'OKAKSE'
TOKEN_KEY = 'mytoken'

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
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
    print(username)
    print(password)
    password_hash = hashlib.sha256(password. encode('utf-8')).hexdigest()
    
    doc = {
        "username": username,
        "password": password_hash,
        
    }
    db.user.insert_one(doc)
    return jsonify({"result": "success"})


@app.route("/signin", methods=["GET"])
def signin():
    return render_template("login.html")

@app.route("/sign_in", methods=["POST"])
def sign_in():
    username = request.form["username"]
    password = request.form["password"]
    print(username)
    pw_hash = hashlib.sha256(password. encode('utf-8')).hexdigest()
    print(password)
    result = db.user.find_one(
        {
            "username": username,
            "password": pw_hash,
        }
    )
    if result:
        payload = {
            "id": username,
            "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 24),
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        return jsonify(
            {
                "result": "success",
                "token": token,
            }
        )
    else: return jsonify({"result": "success", "user_id": str(result.get("_id"))})
   
    
    

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