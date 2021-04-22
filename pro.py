from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template('primer.html')
    elif request.method == 'POST':
        print(request.form['m'])
        print(request.form['a'])
        print(request.form['breakfest'], request.form['class1'])
        print(request.form['lunch'], request.form['class2'])
        print(request.form['night'], request.form['class3'])
        return "Форма отправлена"



if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')