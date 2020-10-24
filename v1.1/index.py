# -*- coding: utf-8 -*-
"""
@author: mabl
@software: PyCharm
@file: flask.py
@date: 2020/9/28
"""

import hashlib
from db.configs import db
from db.models import Chat
import datetime
import os
from operator import itemgetter
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)
app.debug = True

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/", methods=["GET"])
def main():
    # print(request.headers["X-Natapp-Ip"])

    return render_template("main.html")

@app.route("/submitText", methods=["POST"])
def submitText():
    timeStamp = int(datetime.datetime.timestamp(datetime.datetime.now()))
    userid = request.form.get("userid")
    text = request.form.get("text")
    ip = request.headers["X-Real-Ip"]
    time = str(datetime.datetime.now())

    id = str(str(timeStamp) + str(userid) + str(ip))
    id = md5(id)


    data = [id, time, userid, text, ip]
    print(data)
    insert_data(dict(zip(["_id", "time", "userid", "text", "ip"], data)))

    return jsonify({"ip": ip, "code": 200})

@app.route("/chatList", methods=["POST"])
def chatList():
    timeStamps = []
    chat_detail = []
    labels = ["time", "text"]
    ct = Chat()
    chats = ct.query.all()
    for chat in chats:
        timeStamps.append(datetime.datetime.timestamp(datetime.datetime.strptime(str(getattr(chat, labels[0])), '%Y-%m-%d %H:%M:%S.%f'))*1000000)
        chat_detail.append([getattr(chat, labels[0])[5:19], getattr(chat, labels[1])])
    chat_list = dict(zip(timeStamps, chat_detail))
    chat_list = sorted(chat_list.items(), key=itemgetter(0))
    chat_list = dict(chat_list)
    # chat_list.reverse()
    return jsonify(chat_list)



def insert_data(data):
    if(type(data) != type({})):
        raise(TypeError)
    data = Chat(**data)
    db.session.add(data)
    db.session.commit()
    # print(data)

def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf-8"))
    return m.hexdigest()

app.run(host="127.0.0.1", port='8000')