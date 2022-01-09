from flask import Flask,render_template, redirect, request
import joblib
app=Flask(__name__)

m=joblib.load('model.pkl')

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/home')
def home():
    return redirect('/')

@app.route('/submit', methods=["POST"])
def submit_data():
    if request.method =="POST":
        print(request.form)

        hrs=float(request.form['hrs'])

        print(hrs)
        marks=m.predict([[hrs]])[0][0]
    return render_template('index.html',your_marks=round(marks,2))
    # return redirect('/submit_response')
if __name__=='__main__':
    app.run(debug=True)