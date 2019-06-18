from flask import Flask,render_template
app = Flask(__name__)

@app.route('/show')
def show_something():
    show = 'goodbye'
    if show == 'goodbye':    
        return render_template('goodbye.html')
    return render_template('hello.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)