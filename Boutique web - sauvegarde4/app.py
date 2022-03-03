from flask import Flask, redirect, request, url_for, render_template, session
from functools import wraps
import sqlite3
from werkzeug.exceptions import abort


app = Flask(__name__)
app.config['SECRET_KEY'] = 'filesystem'




def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'login' not in session:
            return redirect('/account')
        return f(*args, **kwargs)
    return decorated_function

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(cars_id):
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars WHERE id = ?',(cars_id,)).fetchone()
    conn.close()
    if cars is None:
        abort(404)
    return cars

@app.route('/<int:cars_id>')
def cars(cars_id):
    cars = get_post(cars_id)
    conn = get_db_connection()
    cars_rand = conn.execute('SELECT * FROM (SELECT * FROM cars EXCEPT SELECT * FROM cars WHERE id=?) ORDER BY RANDOM() LIMIT 3 ;', [cars['id']]).fetchall()
    conn.close()
    return render_template('products-details.html', cars=cars, cars_rand=cars_rand)

@app.route("/")
def home():
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars ORDER BY RANDOM() LIMIT 3;').fetchall()
    concept = conn.execute('SELECT * FROM concept ORDER BY RANDOM() LIMIT 3;').fetchall()
    conn.close()

    return render_template("index.html", cars=cars, concept=concept)


@app.route('/account', methods = ['POST', 'GET'])
def account():
    if request.method == 'POST':
        conn = get_db_connection()
        if request.form['submit'] == 'btn_log':
            username = request.form['username']
            password = request.form['password']

            
            cur = conn.cursor()
            statement = f"SELECT * FROM user WHERE username= '{username}' AND password= '{password}';"
            cur.execute(statement)
            if not cur.fetchone():
                return redirect(url_for('account'))
            else:
                session['login'] = username
                #return  redirect(url_for('log', login = True))
            return redirect('/account_log')

        if request.form['submit'] == 'btn_reg':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

            cur = conn.cursor()
            cur.execute("INSERT INTO User (username,email,password) VALUES (?,?,?);",(username,email,password) )    
            conn.commit()
        
            return redirect(url_for('home'))
    
    return render_template('account.html')


@app.route('/account_log', methods= ['POST', 'GET'])
@login_required
def account_log():

    if request.method == 'POST':
        session.clear()
        return redirect('/')

    result = None

    if 'login' in session:
        result = session['login']
    else:
        result = 'Anonymous'

    return render_template('log.html', username=result)

@app.route("/products")
def products():
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM cars').fetchall()
    conn.close()
    return render_template("products.html", cars=cars)

@app.route("/cart")
def cart():
    if 'cart' in session:
        productsCart = []
        conn = get_db_connection()
        for i in range(len(session['cart'])):
            productsCart.append(conn.execute('SELECT * FROM cars WHERE id=?', [session['cart'][i]]).fetchall())
        
        conn.close()
    else:
        productsCart = ''

    print(productsCart)
    return render_template("cart.html", products=productsCart)

@app.route('/addCart/<idProduct>', methods=['POST', 'GET'])
def addCart(idProduct):

    if 'cart' not in session:
        session['cart'] = []
    list_temp = session['cart']
    list_temp.append(idProduct)
    session['cart'] = list_temp

    return idProduct

@app.route('/removeProductCart/<idProduct>', methods=['GET', 'POST'])
def removeProductCart(idProduct):

    cart_temp = session['cart']
    print(cart_temp)
    for j in cart_temp:
        print("elem", type(j))
        if j == idProduct:
            cart_temp.remove(idProduct)
    session['cart'] = cart_temp
    print(session['cart'])  


    return idProduct


@app.route("/about_us")
def about_us():
    return render_template("about-us.html")


if __name__== "__main__":
    app.run(debug=True)
