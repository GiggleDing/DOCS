import functools
import docx
from docx import Document
from lxml import etree

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        file = request.files['file']
        
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not file:
            error = 'file is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
                
                
                # -------------------------------------------------------
                file.save('/Users/giggleding/Documents/flask-tutorial/doc/text.docx')
                
                doc = Document('/Users/giggleding/Documents/flask-tutorial/doc/text.docx')
                # 创建xml根元素
                root = etree.Element('document')

                # 解析每个段落
                for para in doc.paragraphs:
                    # 创建xml段落元素
                    para_element = etree.SubElement(root, 'paragraph')
                    # 设置段落样式属性
                    para_element.set('style', para.style.name)
                    # 解析每个段落中的文本
                    for run in para.runs:
                        # 创建xml文本元素
                        text_element = etree.SubElement(para_element, 'text')
                        # # 设置文本样式属性
                        # text_element.set('style', run.font.name)
                        # 添加文本内容
                        text_element.text = run.text

                # 保存xml文件
                with open('example.xml', 'wb') as f:
                    f.write(etree.tostring(root, pretty_print=True))
                # --------------------------------------------------------



            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view