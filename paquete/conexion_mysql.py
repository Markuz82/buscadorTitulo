import pymysql

conexion = pymysql.connect('localhost','root','123456', 'libreriaToni')
cursor = conexion.cursor()

#SQL


def resultado(titulo):
    #resultados van a cursor
    cursor.execute('''
    SELECT b.title,b.price,a.name 
    FROM books as b 
    JOIN authors as a 
    ON b.author_id=a.author_id
    WHERE b.title LIKE "%{0}%"
    ;
    '''.format(titulo))
    #ejecutado ok
    conexion.commit()
    #La variable resultado tiene solo los valores a printar
    resultado = cursor.fetchall()
    return  resultado

    # for linea in resultado:
    #     titulo = linea[0]
    #     precio = linea[1]
    #     autor = linea[2]
    # 
    #conexion.close()