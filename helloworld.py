from flask import Flask, request, redirect, render_template, session
from DatabaseHelper import *

app = Flask(__name__)

app.secret_key = 'QWERTYUIOP'

@app.route('/test', methods=['GET', "POST"])  # 路由默认接收请求方式位POST，然而登录所需要请求都有，所以要特别声明。
def test():
    if request.method == 'GET':
        return render_template('test.html')

@app.route('/login', methods=['GET', "POST"])  # 路由默认接收请求方式位POST，然而登录所需要请求都有，所以要特别声明。
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    sql = "SELECT * from user where user_name=" + "'" + user + "'" + "and user_password=" + "'" + pwd + "'"
    result = select(sql)
    n = list(result)
    if ((user == 'admin' and pwd == '123')or(len(n)!=0)):  # 这里可以根据数据库里的用户和密码来判断，因为是最简单的登录界面，数据库学的不是很好，所有没用。
        session['user_info'] = user
        return redirect('/index')
    else:
        return render_template('login.html', msg='wrong!')

@app.route('/forgetpwd', methods=['GET', "POST"])
def forgetpwd():
    if request.method == 'GET':
        return render_template('forgetpwd.html')
    user = request.form.get('user')
    question=request.form.get("userquestion")
    answer=request.form.get("useranswer")
    if((len(user)!=0)and question and(len(question)!=0) and answer and(len(answer)!=0)):
        sql = "SELECT user_password from user where user_name=" + "'" + user + "'" + "and user_question=" + "'" + question + "'" + "and user_answer=" + "'"+answer+"'"
        result=select(sql)
        n=list(result)
        if(len(n)!=0):
            return n
        if(len(n)==0):
            return render_template('forgetpwd.html',msg='not found!')
    else:
        return render_template('forgetpwd.html', msg='plz fill every blank')



@app.route('/index')
def index():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    return 'hello'+user_info



@app.route('/register', methods=['GET', "POST"])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        dic={}
        dic["username"]=request.form.get("username")
        dic["first_name"]=request.form.get("firstname")
        dic["last_name"]=request.form.get("lastname")
        dic["user_email"]=request.form.get("email")
        dic["user_phone"]=request.form.get("phone")
        dic["account_type"]=request.form.get("usertype")
        dic["user_password"]=request.form.get("password")
        dic["user_question"]=request.form.get("userquestion")
        dic["user_answer"]=request.form.get("useranswer")
        dic["verified"]="1"
        #
        if((len(dic["username"].strip())!=0)and(len(dic["first_name"].strip())!=0)and(len(dic["last_name"].strip())!=0)and(len(dic["user_email"])!=0)and(len(dic["user_phone"].strip())!=0)and dic["user_question"]and(len(dic["account_type"].strip())!=0)and(len(dic["user_password"].strip())!=0)and dic["user_question"] and(len(dic["user_question"].strip())!= 0) and (len(dic["user_answer"].strip())!= 0)):
            insert("user", dic)
            return render_template('register.html', msg='Success!')
        else:
            return render_template('register.html', msg='Wrong!')


if __name__ == "__main__":
    app.run()