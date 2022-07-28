from cmath import pi
from crypt import methods
from statistics import mode
from flask import Flask, appcontext_popped, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/predecir", methods=['POST'])
def predecir():
    cuartos = int(request.form['cuartos'])
    distancia = int(request.form['distancia'])
    prediccion = model.predict([[cuartos,distancia]])
    output = round(prediccion[0],2)
    return render_template('index.html',label_txt=f'Una casa con {cuartos} habitaciones ubicada a {distancia} km tine un costo de S/. {output} cada habitacion')
    

if __name__ == "__main":
    app.run(debug=True)
