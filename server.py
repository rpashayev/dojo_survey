from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/process', methods = ['POST'])
def process_form():
    session['dojo_first_name'] = request.form['first_name']
    session['dojo_last_name'] = request.form['last_name']
    session['dojo_city'] = request.form['city']
    session['dojo_language'] = request.form['language']
    session['dojo_comment'] = request.form['comment']
    print(request.form)
    return redirect('/result')

@app.route('/result')
def result_page():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug = True)
