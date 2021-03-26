from flask import Flask, session, redirect, request, url_for, abort, make_response, render_template, send_file, \
    send_from_directory
from flask import jsonify
from flask_hashing import Hashing
import libs.db


app = Flask(__name__, static_url_path='/static')
hashing = Hashing(app)
handler = None


@app.route("/create_user", methods=['GET'])
def create_user():
    global handler
    handler = libs.db.DBConnection(app)
    username = request.args.get('username')
    password = request.args.get('password')
    
    token = hashing.hash_value(password, salt='OO_X_OO')
    
    res = handler.create_user(username, password, token)
    if res is None or res is False:
        return jsonify({"code": "success"})
    return jsonify({"code": "fail"})


@app.route("/update_user", methods=['GET'])
def update_user():
    global handler
    handler = libs.db.DBConnection(app)
    username = request.args.get('username')
    password = request.args.get('password')
    first_name = request.args.get('first_name',"")
    last_name = request.args.get('last_name',"")
    phone = request.args.get('phone',"")
    email = request.args.get('email',"")
    country = request.args.get('country',"")

    list_country_available = handler.get_list_country_available(country)
    if country in list_country_available:
        token = hashing.hash_value(password, salt='OO_X_OO')
        
        res = handler.update_user(username, password, first_name, last_name, phone, email, country, token)
        if res is None or res is False:
            return jsonify({"code": "success"})
        return jsonify({"code": "fail"})
    return jsonify({"code": "fail", "message": "country is invalid"})


@app.route("/get_user", methods=['GET'])
def get_user():
    global handler
    handler = libs.db.DBConnection(app)
    token = request.args.get('token')
    user = handler.get_user_by_token(token)
    if user is None or user is False:
        return jsonify({"code": "success", "user": user[0]})
    return jsonify({"code": "fail"})