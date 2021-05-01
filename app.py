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

# shop 페이지
# sub 페이지


if __name__ == '__main__':
    app.run()