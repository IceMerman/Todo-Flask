from flask import (
    Flask,
    request,
    make_response,
    redirect,
    escape,
    render_template,
    session,
    url_for,
    flash
)
from flask_bootstrap import Bootstrap5
from core.forms import LoginForm

app = Flask(__name__, template_folder='./templates')
bootstrap = Bootstrap5(app)

app.config['SECRET_KEY'] = 'SHA256 SALTYSALT!289280ff8719fdfd165f8fa0d9df02ed'

todo_list = [f'todo {i:>02}' for i in range(10)]
todo_dict = {i: f'todo {i:>02}' for i in range(10)}

@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    
    user_ip = session.get('user_ip')
    username = session.get('username')
    form = LoginForm()
    
    context = {
        'user_ip': user_ip,
        'todos': todo_list,
        'todo_dict': todo_dict,
        'form': form,
        'username': username
    }

    # Equivalente a detectar el POST
    if form.validate_on_submit():
        username = form.username.data
        # pwd = form.pwd.data
        session['username'] = username
        flash('Nombre de usuario registrado con éxito', category='success')
        return redirect(url_for('index'))

    return render_template('hello.html', **context)

if __name__ == '__main__':
    app.run(debug=True, port=8000)