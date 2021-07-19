from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://yoyo:Aa147@mycluster.iumxk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#把資料放進資料庫
db = client.WTFORMS #選擇操作WTFORMS資料庫
customer_collection = db.members #選擇操作members集合
#把資料新增到集合中


@app.route("/")
def home_page():
    online_users = db.users.find({"online": True})
    return render_template("index.html",
        online_users=online_users)

@app.route("/read")
def read_data():
    customer = (customer_collection.find())
    return render_template('index.html', customer=customer)


@app.route("/form")
def form():

    return render_template('form.html')


@app.route("/data", methods=['GET'])
def show_data():
    if request.method == 'GET':
        name = request.args.get("x")
        phone = request.args.get("y")
        loc = request.args.get("z")
        if name != "" and phone != "" and loc != "":
            customer = customer_collection.insert_one(
                {"name": name, "phone": phone, "location": loc})
            return ("data added to the database")
        else:
            return ("Kindly fill the form")


@app.route("/delete")
def delete():
    customer_collection.remove({})
    return "All data deleted"


if __name__ =='__main__':
      app.run(host='0.0.0.0',port =3000,debug=True)