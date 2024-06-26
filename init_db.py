from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/contents.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    db.create_all()
    return "Database has been recreated."

if __name__ == '__main__':
    app.run(debug=True)
