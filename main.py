#inicializadmos librerías/dependencias
from flask import Flask #para publicar en web
from flask import render_template #renderizar html y pasarlo a ruta. crear ruta
from flask import request 
from paquete import conexion_mysql#rescatar/recuperar información enviada

#instanciamos flask para recuperar las instancias que tiene Flask
#inicializa app del tipo clase Flask
app = Flask(__name__)

#creamos las rutas porque hemos llamado a Flask
@app.route('/', methods=['GET','POST'])
#funcion que se va a ejecutar al cargar la ruta '/'
def inicio():
    #si tu recibes (método POST) haz. (método POST lo convierte todo en string OJO)
    if request.method == 'POST':
        #la variable viene del formulario como string
        titulo = request.form['titulo']

        nombre = conexion_mysql.resultado(titulo)

        return render_template('index.html', titulo=nombre)

    return render_template('index.html', titulo=[])
    #renderizado el index. Carga la ruta en el servidor. Si se cumple el if este return no se ejecuta
    #Los returns estén donde estén acaban la función

#arrancamos el servidor
if __name__ == "__main__":
    app.run('127.0.0.1', 5009, debug=True)