from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import db
from models import User

app = Flask(__name__)

DATABASE = 'database/app.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template("index.html", users=users)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        points = request.form['points']

        conn = get_db_connection()
        conn.execute('INSERT INTO users (Name, Id, Points) VALUES (?, ?, ?)', (name, id, points))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))

    return render_template('create_user.html')


@app.route('/update/<int:id>', methods=('GET', 'POST'))
def update(id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE Id = ?', (id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        points = request.form['points']
        
        conn.execute('UPDATE users SET Name = ?, Points = ? WHERE Id = ?', (name, points, id))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))

    return render_template('update_user.html', user=user)


@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE Id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
