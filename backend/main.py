import json
import docx
import re
import sqlite3

def parse_docx_to_json(docx_file_path, json_file_path, db_file_path):
    doc = docx.Document(docx_file_path)

    conn = sqlite3.connect(db_file_path)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS paragraphs
        (id INTEGER PRIMARY KEY,
        style TEXT)""")
    c.execute("""
        CREATE TABLE IF NOT EXISTS runs
        (id INTEGER PRIMARY KEY,
        text TEXT,
        style TEXT,
        bold INTEGER,
        color TEXT,
        paragraph_id INTEGER,
        FOREIGN KEY (paragraph_id)REFERENCES paragraphs(id))""")
    
    result = {
        'paragraphs': [],
    }

    for para in doc.paragraphs:
        para_text = []
        if re.match(r'\d(\.\d)*\s\S*', str(para.text)):
            c.execute('INSERT INTO paragraphs (style) VALUES (?)', (para.style.name,))
            paragraph_id = c.lastrowid
            for run in para.runs:
                c.execute('INSERT INTO runs (text, style, bold, color, paragraph_id) VALUES (?, ?, ?, ?, ?)', (run.text, run.style.name, run.bold, str(run.font.color.rgb) if run.font.color.rgb else None, paragraph_id))
                para_text.append({
                    'text': run.text,
                    'style': run.style.name,
                    'bold': run.bold,
                    'color': str(run.font.color.rgb) if run.font.color.rgb else None
                })
        if para_text:
            result['paragraphs'].append({
                'text': para_text,
                'style': para.style.name
            })
    
    conn.commit()
    conn.close()

    with open(json_file_path, "w") as f:
        json.dump(result, f, indent=4)

parse_docx_to_json("example.docx", "example.json", "example.db")