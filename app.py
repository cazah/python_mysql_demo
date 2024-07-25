from flask import Flask, render_template
from datetime import datetime
import mysql.connector

app = Flask(__name__)

def get_welcome_message():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',    # replace with your MySQL username
        password='root',# replace with your MySQL password
        database='demo'
    )
    cursor = connection.cursor()
    current_hour = datetime.now().hour
    if current_hour < 12:
        cursor.execute("SELECT message FROM messages WHERE message = 'Good Morning'")
    elif 12 <= current_hour < 18:
        cursor.execute("SELECT message FROM messages WHERE message = 'Good Afternoon'")
    else:
        cursor.execute("SELECT message FROM messages WHERE message = 'Good Evening'")
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result[0]

@app.route('/')
def home():
    message = get_welcome_message()
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
