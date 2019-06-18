from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def show():
    if request.method == 'POST':
        text = request.form['name']
        return render_template('index.html', text=text)
    return render_template('index.html', text='Stranger')

if __name__ == "__main__":
    app.run(debug=True)