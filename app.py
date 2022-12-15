from flask import Flask,render_template,request,redirect

app = Flask(__name__)
#路由


@app.route('/', methods = ['GET','POST'])#要去访问的路径/
def login():#这边实现登陆的逻辑
    print() #request 对象可以拿到前端给的所有数据
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print('data from server : ',username,password)


        return redirect('/admin')
    return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


