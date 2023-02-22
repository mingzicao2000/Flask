from flask import Flask,request,url_for

app = Flask(__name__)



@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user',methods=['POST'])
def hello_user():
    return 'hello user'

@app.route('/users/<id>')
def users_id(id):
    return 'users id:' + id

@app.route('/query_id')
def query_id():
    id = request.arg.get('id')
    return 'query id:' + id

@app.route('/query_url')
def query_url():
    return 'query url:' + url_for('users_id')


@app.route('/user1/<username>')
def show_user_profile(username):
    # 显示用户名
    return 'User {}'.format(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
    return 'Post {}'.format(post_id)


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # 显示 /path/ 之后的路径名
    return 'Subpath {}'.format(subpath)



if __name__ =='__main__':
    app.run()