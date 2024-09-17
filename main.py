from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/decision/<int:score>')
def decision(score):
    return render_template('decide.html',result=score)

@app.route('/success/<int:score>')
def success(score):
    return render_template('success.html', result=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('fail.html', result=score)

@app.route('/table')

#Result checker
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    the_dictionary = {}
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science+maths+c+datascience)/4
        
        the_dictionary['science'] = science
        the_dictionary['maths'] = maths
        the_dictionary['c'] = c
        the_dictionary['total_score'] = total_score
    
    # res = ''
    # WRITING THIS CONDITION IN JINJA2 TEMPLATE
    # if total_score >= 35:
    #     res = 'success'
    # else:
    #     res = 'fail'
    
    # return render_template('result.html',result=res)

    # return redirect(url_for('decision', score=total_score))


    return render_template('table.html',result = the_dictionary)


if __name__ == '__main__':
    app.run(debug=True)