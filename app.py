from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/servicios")
def servicios():
    return render_template('servicios.html')

@app.route("/contactos")
def contacto():
    return render_template('contactos.html')

@app.route("/ubicacion")
def ubicacion():
    return render_template('ubicacion.html')


if __name__ == "__main__" :
    app.run(debug= True, port= 5001)

