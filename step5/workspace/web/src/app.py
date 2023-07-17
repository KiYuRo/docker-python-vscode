from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="mysql-step5",  # hostはdocker-compose.ymlファイルで定義したDBのコンテナ名を指定
    user="step5",
    password="step5",
    database="step5"
)

@app.route('/')
def get_data():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()  
    cursor.close()
    return jsonify( data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500)
    