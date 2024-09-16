from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return render_template('success.html', result=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('fail.html', result=score)

#Result checker
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+c+datascience)/4
    
    res = ''
    if total_score >= 35:
        res = 'success'
    else:
        res = 'fail'
    return redirect(url_for(res, score=total_score))
    # return render_template('result.html',result=res)


if __name__ == '__main__':
    app.run()