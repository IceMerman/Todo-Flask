from . import auth
from app.forms import LoginForm
from flask import (
    render_template,
    session,
    flash,
    redirect,
    url_for
    )

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    context ={
        'form': form
    }

    # Equivalente a detectar el POST
    if form.validate_on_submit():
        username = form.username.data
        # pwd = form.pwd.data
        session['username'] = username
        flash('Nombre de usuario registrado con éxito', category='success')
        return redirect(url_for('index'))
        
    return render_template('auth/login.html', **context)