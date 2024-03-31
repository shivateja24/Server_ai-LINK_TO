from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def greet():
    # Get today's date and current time
    now = datetime.now()
    current_date_and_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Customize the message with the name and current date and time
    message = f"Hi Shiva Teja {current_date_and_time}"
    
    return message

if __name__ == '__main__':
    app.run(debug=True)
