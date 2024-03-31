from flask import Flask
from datetime import datetime
 

 
import pyodbc


# Connection string
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:link-to-database.database.windows.net,1433;Database=link-to;Uid=root1;Pwd=Shiva242004;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
# Establish connection
connection = pyodbc.connect(connection_string)
print("Connection to SQL Server successful")


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
