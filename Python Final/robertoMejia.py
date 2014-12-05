import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def indexUpdate():
    conn = sqlite3.connect("final_exam.sql")

    return render_template('index.html', data = data);
app.run()