from flask import Flask, render_template, request, redirect
from passlib.hash import sha256_crypt
import pymysql

app = Flask(__name__)

# 오류 표시, 나중에 배포할 때는 app.debug 지우거나 False로 고쳐주기
app.debug = True

# Database 연결
db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'dust'
)

# index page
@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

# news page
@app.route('/news', methods = ['GET', 'POST'])
def news():
    return render_template("news.html")

# info page
@app.route('/info', methods = ['GET', 'POST'])
def info():
    return render_template("info.html")

# login page
@app.route('/login', methods = ['GET', 'POST'])
def login():
    cursor = db.cursor()
    
    if request.method == "POST":
        userid = request.form['userid']
        password = request.form['password']

        sql = "SELECT * FROM `users` WHERE userid = %s;"
        input_data = [userid]

        cursor.execute(sql, input_data)
        user = cursor.fetchone()

        if user == None:
            print(user)
            return redirect('/register')
        else:
            return redirect('/')
    else:
        return render_template('login.html')
    
# register page
@app.route('/register', methods = ['GET', 'POST'])
def register():
    cursor = db.cursor()
    
    if request.method == "POST":
        userid = request.form['userid']
        password = sha256_crypt.encrypt(request.form['password'])

        sql = "INSERT INTO `users` (`userid`, `password`) VALUES (%s, %s);"
        input_data = [userid, password]

        cursor.execute(sql, input_data)
        db.commit()

        # db.close()

        return redirect("/")
    else:
        return render_template("register.html")

# @app.route('/logout')
# def logout():
    


if __name__ == '__main__':
    app.run()