import pymysql

#SQL
def conexion_MYSQL(libro):
    conexion = pymysql.connect('localhost','root','dandy83', 'libreriatoni')
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT b.title,b.price,a.name 
        FROM books as b 
        INNER JOIN authors as a 
        ON b.author_id=a.author_id
        WHERE b.title = '{0}'
        '''.format(libro)
    )
        #ejecutado ok
    conexion.commit()
        #La variable resultado tiene solo los valores a printar
    datos = cursor.fetchall()

    #conexion.close()