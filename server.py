from flask import Flask, render_template, redirect, session, request
from survey import Survey
app = Flask(__name__)
app.secret_key = 'lock of the key'


@app.route('/')
def survey():
    return render_template('survey.html')


@app.route('/pass_result', methods=['post'])
def pass_result():
    if not Survey.survey(request.form):
        return redirect('/results')

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')


@app.route('/results')
def result():
    return render_template('result_page.html')


@app.route('/return')
def back():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
