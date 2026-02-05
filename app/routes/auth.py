from flask import render_template, url_for, redirect,Blueprint, request,flash,session
from app import db
from app.models import User
from app.forms import LoginForm
from werkzeug.security import check_password_hash,generate_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hashed, form.password.data):
            session['user_id']= user.id
            session['user']=user.fullname
            flash(f'{session['user']} Login Successfully', 'success' )
            return redirect(url_for('notes.upload_file'))
        
        flash('Invaild Email or Password ','danger')
        return redirect(url_for('auth.login'))
    
    return render_template('login.html', form=form)
 
@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logout Successfully', 'success')
    return redirect(url_for('auth.login'))