from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/music")
def music():
    return render_template('music.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route('/resume')
def file_downloads():
    try:
        return send_file('templates/resume.pdf', attachment_filename='resume.pdf')
    except Exception as e:
        return str(e)
