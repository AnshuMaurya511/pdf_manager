import os
from flask import render_template, url_for, redirect, flash, Blueprint,session, request
from app import db
from app.models import Notes
from werkzeug.utils import secure_filename


notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/upload_file', methods=['POST', 'GET'])
def upload_file():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        title = request.form.get('title')
        file = request.form.get('file')

        if file:
            filename= secure_filename(file.filename)
            file.save(os.path.join(notes_bp.config['UPLOAD_FOLDER'], filename))

            note = Notes(
                title=title,
                filename=filename,
                user_id=session['user_id']
            )
            db.session.add(note)
            db.session.commit()

            flash('File Upload Successfully')
            return redirect(url_for('notes.view_notes'))
        
    return render_template('upload.html')
    
@notes_bp.route('/view_notes')
def view_notes():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    notes = Notes.query.filter_by(user_id=session['user_id']).all()
    return render_template('notes.html', notes=notes)