from flask import Flask, request, render_template, jsonify
import psycopg2
from psycopg2 import sql, OperationalError

app = Flask(__name__)

# Подключение к базе данных
def get_db_connection():
    conn = psycopg2.connect(
        host="pg3.sweb.ru",
        port="5432",
        database="kkiruskin4",
        user="kkiruskin4",
        password="KIRIll567"
    )
    return conn

@app.route('/submit-email', methods=['POST'])
def submit_email():
    email = request.form.get('email')

    if not email:
        return jsonify(error="Поле email не должно быть пустым"), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO emails (email) VALUES (%s)", (email,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify(message="Email отправлен успешно!")
    except Exception as e:
        print("Ошибка при добавлении email в БД:", e)  # Вывод ошибки в терминал
        return jsonify(error="Произошла ошибка на сервере"), 500


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
