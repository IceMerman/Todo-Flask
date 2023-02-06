from flask import (
    request,
    make_response,
    redirect,
    render_template,
    session,
    url_for
)
from app import create_app
from app.forms import LoginForm
from unittest import TestLoader, TextTestRunner

app = create_app()

todo_list = [f'todo {i:>02}' for i in range(10)]
todo_dict = {i: f'todo {i:>02}' for i in range(10)}

# Command line interface
@app.cli.command()
def test():
    tests = TestLoader().discover('tests')
    TextTestRunner().run(tests)

@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route('/hello')
def hello():
    
    user_ip = session.get('user_ip')
    username = session.get('username')
    
    context = {
        'user_ip': user_ip,
        'todos': todo_list,
        'todo_dict': todo_dict,
        'username': username
    }

    return render_template('hello.html', **context)

if __name__ == '__main__':
    app.run(debug=True, port=8000)