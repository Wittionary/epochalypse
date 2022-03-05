from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route("/")
def index():
    now = time.time()
    timeleft = (2**31) - now
    return render_template('index.html', timeleft=timeleft)