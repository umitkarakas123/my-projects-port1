from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 = 12, number2 = 15)

@app.route('/mult')
def sum():
    var1 , var2 = 27, 15
    return render_template('body.html', num1 = var1, num2=var2, multiplication = var1*var2)


if __name__=="__main__":
    #app.run(debug = True)
    app.run(host = "0.0.0.0", port = 80)