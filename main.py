from flask import (
    Flask,
    request,
    make_response,
    redirect,
    escape,
    render_template
)

app = Flask(__name__, template_folder='./templates')
todo_list = [f'todo {i:>02}' for i in range(10)]
todo_dict = {i: f'todo {i:>02}' for i in range(10)}

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    user_ip = escape(user_ip)
    context = {
        'user_ip': user_ip,
        'todos': todo_list,
        'todo_dict': todo_dict,
    }
    return render_template('hello.html', **context)

if __name__ == '__main__':
    app.run(debug=True)