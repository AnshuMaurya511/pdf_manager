import os
from flask import render_template, url_for, redirect, flash, Blueprint,session, request,current_app,abort,send_file
from app import db
from app.models import Notes
from werkzeug.utils import secure_filename
from flask import current_app

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/upload_file', methods=['POST', 'GET'])
def upload_file():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        title = request.form.get('title')
        file = request.files.get('file')

        if file:
            filename= secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

            note = Notes(
                title=title,
                filename=filename,
                user_id=session['user_id']
            )
            db.session.add(note)
            db.session.commit()

            flash('File Upload Successfully','success')
            return redirect(url_for('notes.view_notes'))
        
    return render_template('upload.html')
    
@notes_bp.route('/view_notes')
def view_notes():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    notes = Notes.query.filter_by(user_id=session['user_id']).all()
    return render_template('notes.html', notes=notes)

from flask import send_file, abort, current_app
import os

@notes_bp.route('/download/<int:note_id>')
def download(note_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    # 1️⃣ DB se note lao
    note = Notes.query.get_or_404(note_id)

    # 2️⃣ Ownership check
    if note.user_id != session['user_id']:
        abort(403)

    # 3️⃣ Absolute file path
    upload_folder = current_app.config['UPLOAD_FOLDER']
    file_path = os.path.join(upload_folder, note.filename)

    # 4️⃣ File exist check
    if not os.path.exists(file_path):
        abort(404, description="File not found")

    # 5️⃣ Direct send file
    return send_file(
        file_path,
        as_attachment=True
    )
