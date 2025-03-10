# 명함관리
# 명함 : 이름과 연락처 -> {'name' : '홍길동', tel', '1234.}
# 명함 리스트, 명함 추가, 명함 삭제

from flask import Flask, render_template, redirect, request

# __name__은 현재 실행중인 모듈의 이름을 나타내는 내장 변수
# 모듈 이름을 이용해서 templates, static 등을 관리한다
app = Flask(__name__)

# 실제 저장은 외부의 오라클을 사용할것이다
name_cards=[{'name':'홍길동','tel':'1234'},{'name':'전우치','tel':'5678'}]

@app.route("/card/list")
def list():
    return render_template('card/list.html',name_cards=name_cards)

@app.route("/card/insert", methods=["post"])
def insert():
    name = request.form.get("name", None)
    tel = request.form.get("tel", None)
    new_card = {'name':name, 'tel':tel}
    name_cards.append(new_card)
    return redirect("/card/list")

@app.route("/card/delete", methods=["post"])
def delere():
        name = request.form.get("name", None)
        for card in name_cards:
           if card['name']==name:
               name_cards.remove(card)
        return redirect("/card/list")

app.run(debug=True)