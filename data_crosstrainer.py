from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', title="Main application", strava_client_id="10279")

@app.route("/strava-auth-redirect")
def strava_auth_redirect():
    content=request.args 
    return render_template('generic.html', content=content)

@app.route("/user/<username>")
def profile(username):
    return render_template('profile.html', title="Proofile for user %s" % username)

@app.route("/admin")
def admin():
    return render_template('admin.html', title="Administration interface")

if __name__ == "__main__":
    app.debug = False
    app.run(host="0.0.0.0", port=int("80"))
