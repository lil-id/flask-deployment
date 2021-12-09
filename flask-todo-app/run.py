from flask import Flask, render_template, request, url_for, redirect
import pymysql

app = Flask(__name__, template_folder="templates")

db = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="todolist_db", autocommit=True)

@app.route('/')
def show_todo():
        cursor = db.cursor()
        cursor.execute("SELECT * FROM task")
        result = cursor.fetchall()
        return render_template('index.html', rows=result)


@app.route('/add', methods=['POST', 'GET'])
def addTask():
        cursor = db.cursor()
        if request.method == 'POST':
                name = request.form['todo']
                try:
                        sql = "INSERT INTO task(deskripsi) VALUES ('"+ name +"')"
                        cursor.execute(sql)
                except:
                        db.rollback()
                finally:
                        return redirect((url_for('show_todo')))


@app.route('/update', methods=['POST'])
def update():
        cursor = db.cursor()
        id = request.form['id']
        try:
                sql = "UPDATE task SET status=1 WHERE id="+ id + ""
                cursor.execute(sql)
        except:
                db.rollback()
        finally:
                return redirect((url_for('show_todo')))



@app.route('/delete', methods=['POST'])
def delete():
        id_task = request.form['id']
        cursor = db.cursor()
        try:
                sql = "DELETE FROM task WHERE id="+ id_task + ""
                cursor.execute(sql)
        except:
                db.rollback()
        finally:
                cursor.close()
                return redirect(url_for('show_todo'))

db = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="todolist_db", autocommit=True)
