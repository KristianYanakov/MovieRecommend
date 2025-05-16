from flask import Flask
from flask import redirect, url_for
from routes import routes
app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/info')
def info():
    return "Hello fellow Movie Enjoyer ;)"

if __name__ == '__main__':
    app.run(debug=True)
