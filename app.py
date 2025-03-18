from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/operacion', methods=['POST'])
def operacion():
    dato1 = request.form.get('dato1')    
    dato2 = request.form.get('dato2')
    action = request.form.get('action')
    result = "resultados acá"
    if dato1 and dato2:
        try:
            num1 = float(dato1)
            num2 = float(dato2)
            if action == 'sumar':
                result = num1 + num2
            elif action == 'restar':
                result = num1 - num2
            elif action == 'multiplicar':
                result = num1 * num2
        except ValueError:
            result = "ingresar solo numeros"
    return render_template('operacion.html', result=result, operacion=action)

if __name__ == '__main__':
    app.run(debug=True)