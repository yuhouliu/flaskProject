from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy  # 数据库
import os

app = Flask(__name__)
app.secret_key = 'Secret Key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///idols.sqlite3'  # 指定数据库类型和数据库名称
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # 创建数据库对象


class idols(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    height = db.Column(db.String(50))
    age = db.Column(db.String(10))
    shows = db.Column(db.String(200))

    def __init__(self, name, height, age, shows):
        self.name = name
        self.height = height
        self.age = age
        self.shows = shows

# db.create_all()


@app.route('/')
def home():  # put application's code here
    all_info = idols.query.all()
    return render_template('home.html', idols=all_info)


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        height = request.form['height']
        age = request.form['age']
        shows = request.form['shows']

        insert_data = idols(name,height,age,shows)
        db.session.add(insert_data)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    delete_data = idols.query.get(id)
    db.session.delete(delete_data)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        update_id = request.form.get('id')
        update_data = idols.query.get(update_id)
        update_data.name = request.form['name']
        update_data.height = request.form['height']
        update_data.age = request.form['age']
        update_data.shows = request.form['shows']
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
