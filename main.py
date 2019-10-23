#inicializadmos librerías/dependencias
from flask import Flask #para publicar en web
from flask import render_template #renderizar html y pasarlo a ruta. crear ruta
from flask import request #rescatar/recuperar información enviada
# from paquete import conexion_mysql usamos el siguiente aunque este esta bien
from paquete.conexion_mysql import * #importamos todo lo de la carpeta paquete

#instanciamos flask para recuperar las instancias que tiene Flask
#inicializa app del tipo clase Flask
app = Flask(__name__)

#creamos las rutas porque hemos llamado a Flask
@app.route('/', methods=['GET','POST'])
#funcion que se va a ejecutar al cargar la ruta '/'
def inicio():
    #si tu recibes (método POST) haz. (método POST lo convierte todo en string OJO)
    if request.method == 'POST':
        libro = request.form['libro']
        consulta = conexion_MYSQL(libro)
        print(consulta)

    return render_template('index.html', )

#arrancamos el servidor
if __name__ == "__main__":
    app.run('127.0.0.1', 5009, debug=True)