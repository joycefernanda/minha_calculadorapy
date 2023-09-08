# Importe a biblioteca Flask para criar uma interface web
from flask import Flask, request

# Crie uma instância da classe Flask
app = Flask(__name__)

# Crie uma rota para a página inicial
@app.route('/')
def calculadora():
    return '''
    <form method="POST" action="/calcular">
        <label for="num1">Número 1:</label>
        <input type="number" name="num1"><br>
        <label for="num2">Número 2:</label>
        <input type="number" name="num2"><br><br>
        <input type="submit" value="Somar">
        <input type="submit" value="Subtrair">
        <input type="submit" value="Multiplicar">
        <input type="submit" value="Dividir">
    </form>
    '''

# Crie uma rota para processar os cálculos
@app.route('/calcular', methods=['POST'])
def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacao = request.form['submit']

    resultado = 0

    if operacao == 'Somar':
        resultado = num1 + num2
    elif operacao == 'Subtrair':
        resultado = num1 - num2
    elif operacao == 'Multiplicar':
        resultado = num1 * num2
    elif operacao == 'Dividir':
        resultado = num1 / num2

    return f'O resultado é: {resultado}'

# Execute o aplicativo Flask
if __name__ == '__main__':
    app.run()

