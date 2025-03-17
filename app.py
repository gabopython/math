from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suma', methods=['GET', 'POST'])
def suma():
    result = None
    if request.method == 'POST':
        dato1 = request.form.get('dato1')
        dato2 = request.form.get('dato2')
        if dato1 and dato2:
            try:
                num1 = float(dato1)
                num2 = float(dato2)
                result = num1 + num2
            except ValueError:
                result = "ingresar solo numeros"
    return render_template('suma.html', result=result)

@app.route('/resta', methods=['GET', 'POST'])
def resta():
    result = None
    if request.method == 'POST':
        dato1 = request.form.get('dato1')
        dato2 = request.form.get('dato2')
        if dato1 and dato2:
            try:
                num1 = float(dato1)
                num2 = float(dato2)
                result = num1 - num2
            except ValueError:
                result = "ingresar solo numeros"
    return render_template('resta.html', result=result)

@app.route('/multiplicacion', methods=['GET', 'POST'])
def multiplicacion():
    result = None
    if request.method == 'POST':
        dato1 = request.form.get('dato1')
        dato2 = request.form.get('dato2')
        if dato1 and dato2:
            try:
                num1 = float(dato1)
                num2 = float(dato2)
                result = num1 * num2
            except ValueError:
                result = "ingresar solo numeros"
    return render_template('multiplicacion.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)