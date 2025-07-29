from flask import Flask,render_template,url_for,request,redirect
from models import Orders
from connection import session


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
@app.route('/Product',methods=['POST','GET'])
def Product():
    products = session.query(Orders).all()
    return render_template('products.html',products=products)

@app.route('/edit_or_delete/<int:product_id>')
def edit_or_delete(product_id):
    # logic here
    pass

if __name__=="__main__":
    app.run(debug=True)

