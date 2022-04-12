from distutils.log import debug
import joblib
import cv2
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def Home_index():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def predicted():
    if request.method == "POST":
        user = request.form["FirstName"]
        user1 = request.form["LN"]
        email = request.form["email"]
        
        if request.files:
            images = request.files["imagefile"]
            path = "./static/Uploads" + "/" + images.filename
            images.save(path)
            
            images_read = cv2.imread(path, 0)
            images1 = cv2.resize(images_read, (200,200))
            images1 = images1.reshape(1, -1)
            
            with open('Model_Learning_Covid.joblib', 'rb') as file:
                mdl = joblib.load(file)
            
            predicteds = mdl.predict(images1)
            
            if predicteds == 1:
                predicteds = "Covid"
            else:
                predicteds = "Normal"
            
            images.close()
        return render_template('Predict.html', 
                               temp = user + " " +user1,
                               email = email, 
                               predicteds = predicteds,
                               path = path
                               )
    else:    
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)