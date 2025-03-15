from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def math_tool():
    result = None
    if request.method == 'POST':
        dato1 = request.form.get('dato1')
        dato2 = request.form.get('dato2')
        action = request.form.get('action')
        if dato1 and dato2:
            try:
                num1 = float(dato1)
                num2 = float(dato2)
                if action == 'Suma':
                    result = num1 + num2
                elif action == 'Resta':
                    result = num1 - num2
                elif action == 'Multiplicacion':
                    result = num1 * num2
            except ValueError:
                result = "ingresar solo numeros"
    return render_template('math_tool.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)