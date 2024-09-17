from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hi Samira'

@app.route('/success/<int:score>')
def success(score):
    return f'Congratulations! You have scored : {score}'

@app.route('/fail/<int:score>')
def fail(score):
    return f'Oopsie! You have scored : {score}'

@app.route('/results/<int:score>')
def results(score):
    results = ''
    if score>=35:
        results = 'success'
        return redirect(url_for('success',score=score))
    else:
        # results = 'fail'
        return redirect(url_for('fail',score=score))

if __name__ == '__main__':
    app.run(debug=True)