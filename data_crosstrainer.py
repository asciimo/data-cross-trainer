from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', title="Main application")

@app.route("/user/<username>")
def profile(username):
    return render_template('profile.html', title="Proofile for user %s" % username)

@app.route("/admin")
def admin():
    return render_template('admin.html', title="Administration interface")

if __name__ == "__main__":
    app.debug = True
    app.run()
