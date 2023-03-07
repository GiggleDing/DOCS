import functools
import os
import docx
import re


from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from DOCX.db import get_db

bp = Blueprint('docx', __name__, url_prefix='/docx')

@bp.route('/upload', methods=['POST'])

def upload():
    file = request.files['file']
    if file:
        filename = file.filename
        filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'upload', filename)
        file.save(filepath)
        parse_docx(filepath)
        return 'file uploaded sucessfully!'
    else:
        return 'no file uploaded!'

def parse_docx(docx_file_path):
    doc = docx.Document(docx_file_path)

    db = get_db()

    for para in doc.paragraphs:
        para_text = []
        if re.match(r'\d(\.\d)*\s\S*', str(para.text)):
            db.execute('INSERT INTO paragraph (style, ) VALUES (?)', (para.style.name,))
            paragraph_id = db.lastrowid
            for run in para.runs:
                db.execute('INSERT INTO run (text, style, bold, color, paragraph_id) VALUES (?, ?, ?, ?, ?)', (run.text, run.style.name, run.bold, str(run.font.color.rgb) if run.font.color.rgb else None, paragraph_id))
    
    db.commit()