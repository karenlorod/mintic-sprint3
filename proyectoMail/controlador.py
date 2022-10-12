from db import get_db, close_db

def ver_enviados(correo):
    db = get_db()
    cursor=db.cursor()
    consulta="select  m.asunto,m.mensaje,m.fecha, m.hora, u.nombreusuario  from usuarios u, mensajeria m where u.correo=m.id_usu_recibe and m.id_usu_envia='"+correo+"' order by fecha desc,hora desc"
    cursor.execute(consulta)
    resultado=cursor.fetchall()
    close_db()
    return resultado

def ver_recibidos(correo):
    db = get_db()
    cursor=db.cursor()
    consulta="select  m.asunto,m.mensaje,m.fecha, m.hora, u.nombreusuario  from usuarios u, mensajeria m where u.correo=m.id_usu_envia and m.id_usu_recibe='"+correo+"' order by fecha desc,hora desc"
    cursor.execute(consulta)
    resultado=cursor.fetchall()
    close_db()
    return resultado

def validar_usuario(usuario, password):
    db = get_db()
    cursor=db.cursor()
    consulta="select *from usuarios where correo='"+usuario+"' and password='"+password+"' and estado='1'"
    cursor.execute(consulta)
    resultado=cursor.fetchall()
    close_db()
    return resultado

def lista_destinatarios(usuario):
    db = get_db()
    cursor=db.cursor()
    consulta="select *from usuarios where correo<>'"+usuario+"' "
    cursor.execute(consulta)
    resultado=cursor.fetchall()
    close_db()
    return resultado


def actualizapass(password, correo):
    db = get_db()
    cursor=db.cursor()
    consulta="update usuarios set password='"+password+"' where correo='"+correo+"'"
    cursor.execute(consulta)
    db.commit()
    close_db()
    return "1"

def registrar_mail(origen, destino, asunto, mensaje):
    db = get_db()
    cursor=db.cursor()
    consulta="insert into mensajeria (asunto,mensaje,fecha,hora,id_usu_envia,id_usu_recibe,estado) values ('"+asunto+"','"+mensaje+"',DATE('now'),TIME('now'),'"+origen+"','"+destino+"','0')"
    cursor.execute(consulta)
    db.commit()
    close_db()
    return "1"

def registrar_usuario(nombre,correo, password,codigo):
    try:
        db = get_db()
        cursor=db.cursor()
        consulta="insert into usuarios (nombreusuario,correo,password,estado,codigoactivacion) values ('"+nombre+"','"+correo+"','"+password+"','0','"+codigo+"')"
        print("op 1")
        cursor.execute(consulta)
        print("op 2")
        db.commit()
        print("op 3")
        close_db()
        return "Usuario Registrado Satisfactoriamente"
    except:
        return "ERROR!!! No es posible registrar al usuario debido a que el CORREO y/o NOMBRE DE USUARIO existen. Lo invitamos a modificar los campos pertinentes."

def activar_usuario(codigo):
    db = get_db()
    cursor=db.cursor()
    consulta="update usuarios set estado='1' where codigoactivacion='"+codigo+"'"
    cursor.execute(consulta)
    db.commit()
    
    consulta2="select *from usuarios where codigoactivacion='"+codigo+"' and estado='1'"
    cursor.execute(consulta2)
    resultado=cursor.fetchall()
    close_db()
    return resultado
    
   


    