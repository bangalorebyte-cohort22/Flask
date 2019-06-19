from flask import Flask, render_template, request
import model


app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def show():
    if request.method == 'POST':        
        text = request.form['name']
        status = model.add_name(text)
        names = model.get_names()
        return render_template('index.html', text=status , names=names)
    names = model.get_names()
    return render_template('index.html', text='Stranger' , names=names )

if __name__ == "__main__":
    app.run(debug=True)