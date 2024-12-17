from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    
    def __repr__(self) -> str:
        return f"<User id={self.id}, email={self.email}>"
    
@app.route('/')
def home():
    return "Hello, World!"

# @app.route('/users')
    # users: List[User] = 

if __name__ == "__main__":
    app.run(debug=True, port=7020)