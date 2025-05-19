from flask import Flask, render_template
from flask import redirect, url_for
from routes import routes
from comment import db
app = Flask(__name__)
app.register_blueprint(routes)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':


    app.run(debug=True)
