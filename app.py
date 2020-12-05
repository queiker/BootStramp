from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    label = ""
    id_email = "id_email"
    return render_template('index.html', label = label, id_email = id_email )


if __name__ == '__main__':


    app.run()
