from flask import Flask, request, render_template
from calculo import calcula_bacterias
from database import *
from sympy import *

import matplotlib.pyplot as pt

app = Flask(__name__)

@app.route('/')
def inicial():
   return render_template('telaInicial.html')

@app.route('/resultado', methods =['POST'])
def resultado():
   recurso = request.form['recurso']
   listaDados = calcula_bacterias(int(recurso))
   limite = len(listaDados) + 1

   for tempo in range(1, limite):
      print(tempo)

   return render_template('resultado.html', tempo=tempo , lista=listaDados, limite=limite)

if __name__ == '__main__':
   app.run(debug = True)
