from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.debug = True

# index 페이지 
@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

# member 페이지
@app.route('/join', methods = ['GET'])
def join():
    return render_template("join.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/register', methods = ['GET', 'POST'])
def register():
    return render_template("register.html")

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route('/findUid', methods = ['GET', 'POST'])
def findUid():
    return render_template("findUid.html")

@app.route('/findPass', methods = ['GET', 'POST'])
def findPass():
    return render_template("findPass.html")

# admin 페이지
@app.route('/admin_index', methods = ['GET'])
def admin_index():
    return render_template("admin_index.html")

@app.route('/admin_list', methods = ['GET'])
def admin_list():
    return render_template("admin_list.html")

@app.route('/admin_register', methods = ['GET'])
def admin_register():
    return render_template("admin_register.html")

# sub 페이지
@app.route('/delivery-check', methods = ['GET', 'POST'])
def delivery_check():
    return render_template("delivery-check.html")

@app.route('/event', methods = ['GET', 'POST'])
def event():
    return render_template("event.html")

@app.route('/faq', methods = ['GET', 'POST'])
def faq():
    return render_template("faq.html")

@app.route('/notice', methods = ['GET', 'POST'])
def notice():
    return render_template("notice.html")

@app.route('/qna', methods = ['GET', 'POST'])
def qna():
    return render_template("qna.html")

# shop 페이지
@app.route('/cart', methods = ['GET', 'POST'])
def cart():
    return render_template("cart.html")

@app.route('/search', methods = ['GET', 'POST'])
def search():
    return render_template("search.html")

@app.route('/order', methods = ['GET', 'POST'])
def order():
    return render_template("order.html")

@app.route('/order-complete', methods = ['GET', 'POST'])
def order_complete():
    return render_template("order-complete.html")

@app.route('/view', methods = ['GET', 'POST'])
def view():
    return render_template("view.html")

if __name__ == '__main__':
    app.run()