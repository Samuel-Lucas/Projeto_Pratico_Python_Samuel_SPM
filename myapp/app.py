from flask import Flask, request, render_template

app=Flask(__name__)

@app.route("/", methods=['POST', 'GET'])

def caculate():
    imc = ''
    if request.method == 'POST' and 'peso' in request.form and 'altura' in request.form:
        peso = float(request.form.get("peso"))
        altura = float(request.form.get("altura"))
        imc = round(peso/((altura/100)**2), 2)
    return render_template("index.html", imc = imc)