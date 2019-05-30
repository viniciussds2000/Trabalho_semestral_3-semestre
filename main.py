import os

from flask import Flask,flash,render_template,request,redirect,url_for,send_file,send_from_directory
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename
from BD import *

app = Flask(__name__)

UP_FOLDER = 'imagens\\carros'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
mysql = MySQL()

mysql.init_app(app)

app.config['UP_FOLDER'] = UP_FOLDER
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'semestral3.'

@app.route('/')
def home():
    cursor = mysql.get_db().cursor()

    return render_template("home.html",detail_url='http://127.0.0.1:5000/detalhes/carro/',carros=get_top10(cursor))

@app.route('/detalhes/carro/<carros>', methods=['GET','POST'])
def detalhes_carro(carro):
    conn= mysql.connect()
    cursor=conn.cursor()
    return render_template('detalhes.html', carros=get_carro_id(cursor, numero_carro),url=call_imagem(cursor,conn,carro))



@app.route('/resultado', methods=['GET','POST'])
def resultados():
    if request.method == 'POST':
        pesquisa = request.form.get('campo_pesquisa')
        cursor = mysql.get_db().cursor()
        teste_busca= busca(cursor,pesquisa)
        if teste_busca is None:
            return render_template('home.html')
        else:
            cursor = mysql.get_db().cursor()
            return render_template('buscando.html',consulta=busca(cursor,pesquisa))

    return

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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
        top10 = request.form.get('top_choice')
        file = request.form.get('file')
        if top10 == "Sim":
            top10=1
        else:
            top10=0

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_location = os.path.join(app.config['UP_FOLDER'], filename)
            print(filename)
            print(file_location)
            print(file_location)
            escaped_file_location = file_location.replace('\\', '/')
            print(escaped_file_location)
            file.save(os.path.join(app.config['UP_FOLDER'], filename))

            conn = mysql.connect()
            cursor = conn.cursor()


            # adicionar_imagem(cursor,conn,arquivo)
            incluir_anuncio(cursor, conn, nomecarro, marcacarro, anocarro, corcarro, cambiocarro, preçocarro,
                            placacarro, top10,escaped_file_location)

            cursor.close()
            conn.close()

            return redirect(url_for('uploads_file', filename=filename))
    return render_template('incluir_anuncio')

@app.route('/upload/<filename>', methods=['GET','POST'])
def uploads_file(filename):


    return send_from_directory(app.config['UP_FOLDER'],
                               filename)





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

@app.route('/edit_top10')
def editar_top10():
    cursor = mysql.get_db().cursor()
    return render_template('edit_top10.html',carros=get_carros(cursor))

@app.route('/top10_editado', methods=['GET','POST'])
def top_editado():
    if request.method == 'POST':
        eplaca=request.form.get('ePlaca')
        etop= request.form.get('eTop10')
        if etop == "Sim":
            top10 = 1
        else:
            top10 = 0

        conn = mysql.connect()
        cursor = conn.cursor()
        print(top10)

        edit_top10(cursor,conn,top10,eplaca)

        cursor.close()
        conn.close()

        return render_template('incluso.html')
    else:
        return render_template('adm_page.html')
'''
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_location = os.path.join(app.config['UP_FOLDER'], filename)
            print(file_location)
            escaped_file_location  = file_location.replace('\\','/')
            print(escaped_file_location)
            file.save(os.path.join(app.config['UP_FOLDER'], filename))

            conn = mysql.connect()
            cursor = conn.cursor()

            adicionar_imagem(cursor, conn, filename)

            cursor.close()
            conn.close()

            return redirect(url_for('uploads_file',filename=filename))
    return render_template('teste.html')

@app.route('/upload/<filename>', methods=['GET','POST'])
def uploads_file(filename):


    return send_from_directory(app.config['UP_FOLDER'],
                               filename)'''


@app.route('/carros_reservados')
def reservas():
    cursor = mysql.get_db().cursor()
    return render_template('carros_reservados.html',carros=get_carros(cursor), base_url='http://127.0.0.1:5000/upload/')



if __name__== '__main__':
    app.run(debug=True)
