from flask import Flask, render_template,request,redirect
app = Flask(__name__)

@app.route("/ejgk", methods=['get'])
def ejgk_get():
   return render_template("ejgk.html")

@app.route("/ejgk", methods=['post'])
def ejgk_post():
      a = float(request.form.get('tntwk1',0))
      b = float(request.form.get('tntwk2',0))
      hap = a + b
      return redirect(f"/successs?hap={hap}")

@app.route("/successs", methods=['get'])
def success():
   hap = request.args.get("hap")
   return render_template("successs.html", hap=hap)



app.run(debug=True)