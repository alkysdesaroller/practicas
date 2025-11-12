from flask import Flask # type: ignore
import mysql.connector # pyright: ignore[reportMissingImports]
from db_config import db_config # type: ignore

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT 'Conexión exitosa a MySQL!' AS mensaje;")
        result = cursor.fetchone()
        return f"<h1>Hola Mundo desde Flask!</h1><p>{result[0]}</p>"
    except Exception as e:
        return f"<h1>Error conectando a MySQL:</h1><p>{e}</p>"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
