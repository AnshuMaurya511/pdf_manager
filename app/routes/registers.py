from flask import render_template, session, flash, redirect, Blueprint, url_for
from app.forms import RegistrationForm
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User

registers_bp=Blueprint('registers', __name__)

@registers_bp.route('/register', methods=['POST', 'GET'])
def sign_up():
    form=RegistrationForm()

    if form.validate_on_submit():
        existing = User.query.filter_by(email=form.email.data).first()
        if existing:
            flash('Email has Already Exist', 'danger')
            return redirect(url_for('registers.sign_up'))
        
        hashed=generate_password_hash(form.password.data)
        user = User(
            fullname=form.fullname.data,
            email=form.email.data,
            password_hashed=hashed
        )
        
        db.session.add(user)
        db.session.commit()

        flash('Account Create Successfully, Login now', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)