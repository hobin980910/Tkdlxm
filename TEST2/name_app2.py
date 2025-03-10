from flask import Flask, render_template, redirect, request
app=Flask(__name__)

name_cards=[{'cno':1, 'name':'yj','tel':'5892'},{'cno':2, 'name':'kyj','tel':'1218'}]
cno=3

@app.route("/card/list")
def list():
    error = request.args.get('error')
    message = ''
    if error=='insert':
        message = '연락처가 이미 존재합니다'
    elif error=='delete':
        message = '연락처를 찾을수없습니다'
    return render_template("card2/list.html", name_cards=name_cards, message=message)

@app.route("/card/insert", methods=['post'])
def insert():
    global cno
    name = request.form.get('name',None)
    tel = request.form.get('tel',None)
    # 이름과 연락처가 모두 중복이면 에러코드를 가지고 /card/list로 이동
    for card in name_cards:
        if card['name']==name and card['tel']==tel:
            return redirect("/card/list?error=insert")
    new_card = {'cno' : cno, 'name' : name , 'tel' : tel}
    name_cards.append(new_card)
    cno+=1
    return redirect("/card/list")

@app.route("/card/delete", methods=['post'])
def delete():
    # 없으면 어떡하지 -> 오류처리
    cno = int(request.form.get('cno'))
    for card in name_cards:
        if card['cno']==cno:
            name_cards.remove(card)
            return redirect("/card/list")
    return redirect("/card/list?error+delete")





app.run(debug=True)