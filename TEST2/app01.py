from flask import Flask, render_template,redirect, request

app = Flask(__name__)

@app.route("/login",methods=['get'])
def login_get():
    state = request.args.get('state')
    message = '로그인실패했어요' if state!=None else ""
    return render_template("login.html", message=message)


@app.route("/login",methods=['post'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    if username=='spring' and password=='1234':
        return redirect("/success")
    else:
        return redirect("/login?state=fail")

@app.route("/success")
def success():
    return render_template("success.html")


app.run(debug=True)