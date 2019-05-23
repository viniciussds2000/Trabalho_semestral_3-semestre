from flask import Flask,render_template,request,send_file
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename
from BD import *

app = Flask(__name__)

mysql = MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'semestral3'

@app.route('/')
def home():
    cursor = mysql.get_db().cursor()
    return render_template("home.html",carros=get_carros(cursor))

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

@app.route('/excluir_usuario')
def excluir():
    return render_template('excluir_user.html',)

@app.route('/excluido', methods=['GET','POST'])
def excluindo():
    if request.method == 'POST':
        slogin=request.form.get('slogin')
        ssenha=request.form.get('ssenha')

        conn = mysql.connect()
        cursor = conn.cursor()

        excluir_user(cursor,conn,slogin,ssenha)

        cursor.close()
        conn.close()

        return render_template('incluso.html')
    else:
        return render_template('adm_page.html')

@app.route('/incluir_anuncio')
def Incluir_anuncio():
    cursor = mysql.get_db().cursor()
    return render_template('incluir_anuncio.html',carros=get_carros(cursor))

@app.route('/anuncio_incluso', methods=['GET','POST'])
def incluindo_anuncio():
    if request.method == 'POST':
        nomecarro=request.form.get('nomecar')
        marcacarro=request.form.get('marcacar')
        anocarro=request.form.get('anocar')
        corcarro=request.form.get('corcar')
        cambiocarro=request.form.get('cambiocar')
        preçocarro=request.form.get('preçocar')
        placacarro=request.form.get('placacar')
        arquivo = request.files['file']

        conn = mysql.connect()
        cursor = conn.cursor()

        adicionar_imagem(cursor,conn,arquivo)
        incluir_anuncio(cursor,conn,nomecarro,marcacarro,anocarro,corcarro,cambiocarro,preçocarro,placacarro)

        cursor.close()
        conn.close()



        return render_template('incluso.html')
    else:
        return render_template('adm_page.html')


@app.route('/excluir_anuncio')
def ex_anuncio():
    cursor=mysql.get_db().cursor()
    return render_template('excluir_anuncio.html',carros=get_carros(cursor))

@app.route('/anuncio_excluido', methods=['GET','POST'])
def excluindo_anuncio():
    if request.method == 'POST':
        placacar = request.form.get('placacar')

        conn = mysql.connect()
        cursor = conn.cursor()

        excluir_anuncio(cursor,conn,placacar)

        cursor.close()
        conn.close()

        return render_template('incluso.html')
    else:
        return render_template('adm_page.html')


@app.route('/carros_reservados')
def reservas():
    cursor = mysql.get_db().cursor()
    return render_template('carros_reservados.html',carros=get_carros(cursor))




if __name__== '__main__':
    app.run(debug=True)
