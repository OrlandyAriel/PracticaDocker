from flask import Flask as f
from redis import Redis as r
 
app = f(__name__)
redis = r(host='redis', port=6379)

@app.route('/')
def pagina():
    autor = "<h2 style='color:green'> Alumno: Orlandy Ariel Sánchez Acosta.<h2>"
    contador_visitas = redis.incr('count', 1) 
    titulo = '<h1 style="color:blue">Curso Docker FGULL</h1>'
    contenido ="<h2>Práctica final.</h2>"
    cont_visual = "<b> Tu has visitado %i veces esta página"%contador_visitas
    mensaje =autor+ titulo + contenido + cont_visual

    if( contador_visitas > 9):
        redis.set('count', 0) 
        mensaje = '<b style="color:red;"> Límite de visitas por un día es de 10 visualizaciones.</br>Su siguiente visita reiniciará el contador.</b>'

    return mensaje
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)