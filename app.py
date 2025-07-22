from flask import Flask,render_template,url_for,request,redirect,session
from models import Orders
from connection import data,session


app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
          Product=request.form['Product']
          Quantity=request.form['Quantity']
          Price=request.form['Price']

          new_Product=Orders(Product=Product,Quantity=Quantity,Price=Price)
          session.add(new_Product)
          session.commit()
    return render_template("home.html")


if __name__=="__main__":
    app.run(debug=True)
