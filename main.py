from flask import Flask,render_template,request,redirect,url_for
from flaskext.mysql import MySQL
from BD import *

app = Flask(__name__)

mysql = MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
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



@app.route('/incluso', methods=['GET','POST'])
def incluindo():
    if request.method == 'POST':
        nlogin=request.form.get('nlogin')
        nsenha=request.form.get('nsenha')

        conn = mysql.connect()
        cursor = conn.cursor()

        incluir_user(cursor,conn,nlogin,nsenha)

        cursor.close()
        conn.close()

        return render_template('incluso.html')
    else:
        return render_template('adm_page.html')


@app.route('/incluir_anuncio')
def Incluir_anuncio():
    return render_template('incluir_anuncio.html')

@app.route('/excluir_anuncio')
def excluir_anuncio():
    return render_template('excluir_anuncio.html')


@app.route('/excluir_usuario')
def excluir():
    return render_template('excluir_user.html')

@app.route('/carros_reservados')
def reservas():
    cursor = mysql.get_db().cursor(                  )
    return render_template('carros_reservados.html',carros=get_carros(cursor))


if __name__== '__main__':
    app.run(debug=True)
