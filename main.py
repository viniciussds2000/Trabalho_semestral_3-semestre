from flask import Flask,render_template,request
from flaskext.mysql import MySQL
from BD import *

app = Flask(__name__)

mysql = MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'semestral3'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/adm_page',methods=['GET','POST'])
def logando():
    if request.method == 'POST':
        login=request.form.get('login')
        senha=request.form.get('senha')

        cursor = mysql.get_db().cursor()

        idlogin = validar_login(cursor,login,senha)

        if idlogin is None:
            return render_template('home.html')

        else:

            return render_template('adm_page.html')

    else:
        return render_template('home.html')

@app.route('/incluir_usuario')
def incluir():
    return render_template('incluir_user.html')

@app.route('/incluso')
def incluindo():
    if request.method == 'POST':
        nlogin=request.form.get('login')
        nsenha=request.form.get('senha')

        cursor = mysql.get_db().cursor()

        nuser= incluir_user(cursor,nlogin,nsenha)

        if nuser is None:
            return render_template('Incluir_user.html')

        else:
            return render_template("incluir_user.html")
    else:
        return render_template('adm_page.html')



if __name__== '__main__':
    app.run(debug=True)
