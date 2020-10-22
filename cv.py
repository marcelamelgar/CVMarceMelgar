from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment,  FileSystemLoader
import yaml

file_loader = FileSystemLoader('templates')
environment = Environment(loader = file_loader)

app = Flask(__name__)

with open('data.yaml') as f:
    fileyaml = yaml.load(f, Loader = yaml.FullLoader)


@app.route('/')
def homelt():
    myHTML = environment.get_template('linkedtree.html')
    picture = url_for('static', filename = fileyaml['fotografia'])
    contactos = fileyaml['contactos']
    autora = fileyaml['informacion_pagina']['autor']
    return myHTML.render(picture = picture, contactos = contactos, autora = autora)

@app.route('/CV')
def index():
    myHTML = environment.get_template('index.html')
    foto = url_for('static', filename = fileyaml['fotografia'])
    titulo = fileyaml['informacion_pagina']['titulo']
    autor = fileyaml['informacion_pagina']['autor']
    nombre = fileyaml['informacion_personal']['nombre_completo']
    pais = fileyaml['informacion_personal']['pais_de_nacimiento']
    idioma1 = fileyaml['informacion_personal']['idiomas'][0]
    idioma2 = fileyaml['informacion_personal']['idiomas'][1]
    edad = fileyaml['informacion_personal']['edad']
    sobreMi = fileyaml['informacion_personal']['acerca_de_mi']
    experiencia = fileyaml['informacion_personal']['experiencia']
    intereses = fileyaml['informacion_personal']['intereses']
    telefono = fileyaml['informacion_personal']['telefono']
    correo = fileyaml['informacion_personal']['correo']
    tecnologias = fileyaml['informacion_profesional']['tecnologias']
    educacion = fileyaml['informacion_profesional']['educacion']
    carrera = fileyaml['informacion_profesional']['carrera']
    refprof = fileyaml['informacion_referencias']['referencias_laborales']
    refper = fileyaml['informacion_referencias']['referencia_personal']
    return myHTML.render(foto = foto, titulo = titulo, autor = autor, nombre = nombre, 
    pais = pais, idioma1 = idioma1, idioma2 = idioma2, edad = edad, sobreMi = sobreMi, experiencia = experiencia, 
    intereses = intereses, telefono = telefono, correo = correo, tecnologias = tecnologias, 
    educacion = educacion, carrera = carrera, refper = refper, refprof = refprof)



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)

#utilice un template de W3SCHOOLS.COM para el cv