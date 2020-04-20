from flask import Flask, render_template, flash, request
import datetime
import webscr

app = Flask(__name__)

# Third Commit


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/time")
def welcome():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title': 'HELLO!',
        'time': timeString
    }
    return render_template('index.html', **templateData)


@app.route("/form")
def form():
    return render_template('form.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)


@app.route("/scrapper")
def scrapp():
    webscr.scrapmain()


@app.route('/variable/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID


if __name__ == "__main__":
    app.run(debug=True)
