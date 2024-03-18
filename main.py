import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    value = 'Кот'
    return flask.render_template('index.html', value=value)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
