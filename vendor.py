from flask import Flask, render_template,url_for, request
 
app = Flask(__name__) 
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cart/')
def cart():
    return render_template('cart.html')

@app.route('/statement/')
def statement():
    return render_template('statement.html')

if __name__ == '__main__': 
	
 app.run(host='localhost', port=5000)
