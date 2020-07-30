from mdl import UnitConversion
from mdl import getUn, joinall
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
import os

app = Flask(__name__)


def uper(j):
	a = ""
	for t in j.split("-"):
		a += t[0].upper()
		a += t[1:].lower()
		a += "."
	a = a[:-1]
	return a


@app.route("/")
def index():
	return redirect("/distance")


@app.route("/<prop>", methods=["POST", "GET"])
def propchosen(prop):
	props = []
	for p, d, f in os.walk(joinall("units")):
		for i in f:
			props.append([i, uper(i), uper(i).lower()])
	units = getUn(joinall("units", prop))
	time = getUn(joinall("time"))
	# print(props)
	if request.method == "POST":
		iv = float(request.form["iv"])
		iu = request.form["iu"]
		it = request.form["it"]
		ou = request.form["ou"]
		ot = request.form["ot"]
		uci = UnitConversion(iv, iu, it, ou, ot, prop)
		res = uci.Result
		selun = [iv, iu, it, ou, ot]
	else:
		res = 0
		selun = [1.0, "", "", "", ""]
	return render_template("index.html", props=props, res=res, selun=selun,
						   propsel=[prop, uper(prop), uper(prop).lower()], units=[f[0] for f in units], time=[f[0] for f in time])


# @app.route("/css/my.css")
# def cssmine():
#     fr = ""
#     with open("templates/css/my.css") as f:
#         fr += f.read()
#     return fr


if __name__ == '__main__':
	app.run(port="80", host="0.0.0.0")
