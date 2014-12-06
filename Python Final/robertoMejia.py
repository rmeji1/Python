import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

def getData():
    try:
        conn = sqlite3.connect("final_exam.sqlite")
        cursor = conn.cursor()
        result = cursor.execute('SELECT gift, name from gifts')
        data = result.fetchall()
    except Exception as e:
        print(type(e))
        print(e)
    return data

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data = getData());
 
@app.route('/', methods=['POST'])
def indexUpdate():
    
    return render_template('index.html', data = getData());
app.run()