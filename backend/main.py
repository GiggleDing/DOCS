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
        text TEXT,
        style TEXT)""")
    result = {
        'paragraphs': [],
    }

    for para in doc.paragraphs:
        para_text = []
        if re.match(r'\d(\.\d)*\s\S*', str(para.text)):
            for run in para.runs:
                para_text.append({
                    'text': run.text,
                    'style': run.style.name,
                    'bold': run.bold,
                    'color': str(run.font.color.rgb) if run.font.color.rgb else None
                })
        if para_text:
            c.execute('INSERT INTO paragraphs (text, style) VALUES (?, ?)', (json.dumps(para_text), para.style.name))
            result['paragraphs'].append({
                'text': para_text,
                'style': para.style.name
            })
    
    conn.commit()
    conn.close()

    with open(json_file_path, "w") as f:
        json.dump(result, f, indent=4)

parse_docx_to_json("example.docx", "example.json", "example.db")