from flask import Flask, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/painting')
def painting():
    images = os.listdir(UPLOAD_FOLDER + "/painting")
    return render_template('painting.html', images=images)


@app.route('/drawing')
def drawing():
    images = os.listdir(UPLOAD_FOLDER + "/drawing")
    return render_template('drawing.html', images=images)


@app.route('/sculpture')
def sculpture():
    images = os.listdir(UPLOAD_FOLDER + "/sculpture")
    return render_template('sculpture.html', images=images)


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/cv')
def cv():
    return render_template('cv.html')


if __name__ == '__main__':
    app.run(debug=True)
