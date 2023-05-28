from flask import Flask, render_template
import os

app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'IMG')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/')
def home():
    img1 = os.path.join(app.config['UPLOAD_FOLDER'], 'elecflexible.jpg')
    img2 = os.path.join(app.config['UPLOAD_FOLDER'], 'circuitelec.jpg')
    img3 = os.path.join(app.config['UPLOAD_FOLDER'], 'spray-pyrolysis.png')
    img4 = os.path.join(app.config['UPLOAD_FOLDER'], 'zno.jpg')
    img5 = os.path.join(app.config['UPLOAD_FOLDER'], 'programacion.jpg')
    icon1 = os.path.join(app.config['UPLOAD_FOLDER'], 'python-icon.png')
    icon2 = os.path.join(app.config['UPLOAD_FOLDER'], 'flask.jpg')
    icon3 = os.path.join(app.config['UPLOAD_FOLDER'], 'pandas.png')
    icon4 = os.path.join(app.config['UPLOAD_FOLDER'], 'Silvaco.png')
    icon5 = os.path.join(app.config['UPLOAD_FOLDER'], 'spice.jpg')
    icon6 = os.path.join(app.config['UPLOAD_FOLDER'], 'origin.png')
    icon7 = os.path.join(app.config['UPLOAD_FOLDER'], 'latex.png')
    icon8 = os.path.join(app.config['UPLOAD_FOLDER'], 'proteus.jpg')
    icon9 = os.path.join(app.config['UPLOAD_FOLDER'], 'office.png')
    return render_template('home.html',user_image=img1, user_image1=img2, 
                           user_image2=img3, user_image3=img4, user_image4 = img5,
                           user_icon1 = icon1, user_icon2 = icon2, user_icon3 = icon3, 
                           user_icon4 = icon4, user_icon5 = icon5,user_icon6 = icon6,
                           user_icon7 = icon7, user_icon8 = icon8, user_icon9 = icon9)


@app.route('/academic')
def academic():
    img1 = os.path.join(app.config['UPLOAD_FOLDER'], 'Buap.jpg')
    img2 = os.path.join(app.config['UPLOAD_FOLDER'], 'ittla.png')
    return render_template('academic.html',user_image1=img1, user_img2 = img2)

@app.route('/projects')
def porjects():
    return render_template('project.html')

@app.route('/paper')
def paper():
    return render_template('paper.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)