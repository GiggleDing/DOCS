from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    result = []
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    cursor = c.execute("""
        SELECT id, style
        FROM paragraphs
    """)
    conn.commit()
    for row in cursor:
        result.append({
            'paragraph': select_runs(row[0]),
            'style': row[1]
        })
    conn.close()
    return jsonify(result)

def select_runs(paragraph_id):
    text = []
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    cursor = c.execute("""
        SELECT text, style, bold, color, paragraph_id
        FROM runs
        WHERE paragraph_id = (?)""", 
        str(paragraph_id))
    conn.commit()
    for row in cursor:
        text.append({
            'text': row[0],
            'style': row[1],
            'bold': row[2],
            'color': row[3]
        })
    conn.close()
    return text