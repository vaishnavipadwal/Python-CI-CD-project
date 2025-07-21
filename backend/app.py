from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route("/data")
def data():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="rootpass",
            database="mydb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
