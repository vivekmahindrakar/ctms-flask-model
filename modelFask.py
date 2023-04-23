import base64
import imghdr
import face_recognition
from PIL import Image
from flask import Flask, redirect, url_for, request, jsonify
import urllib.request
import matplotlib.pyplot as plt
import requests
from io import BytesIO
"%matplotlib inline"
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route("/test", methods=['POST'])
def predictTest():
    result = request.form
    print(result)
    return jsonify({
        "message": "Hogaya na bhai"
    })


@app.route("/nearestPoliceStation", methods=['GET'])
def giveLatLong():
    return jsonify([{
        "lat": "18.442269",
        "long": "73.894747"
    },
        {
            "lat": "18.440630",
            "long": "73.894340"
    },
        {
            "lat": "18.441648",
            "long": "73.895777"
    },
        {
            "lat": "18.439507",
            "long": "73.895230"
    },
        {
            "lat": "18.439765",
            "long": "73.893970"
    }

    ]

    )


@app.route("/predict", methods=['POST'])
def predict():
    if (request.method == "POST"):
        imageFile1 = request.files["image2"]
        image2 = request.form["currUrl"]
        print(image2)
        imageFile1.save("./image/a.png")
        # imageFile2Url = request.files["image1"]

        # response = requests.get(imageFile2Url)
        # imagefile2 = BytesIO(response.content)

        cimage = urllib.request.urlopen(image2)
        confirmedVictim = face_recognition.load_image_file(
            cimage)  # unknown1.jpg
        confirmedVictimencoding = face_recognition.face_encodings(confirmedVictim)[
            0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

        unknown_picture = face_recognition.load_image_file("./image/a.png")
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[
            0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

        results = face_recognition.compare_faces(
            [confirmedVictimencoding], unknown_face_encoding)

        if results[0] == True:
            return jsonify({
                "message": "Its a match"
            })

        else:
            return jsonify({
                "message": "Khaak behenchod kuch nahi match hua..."
            })


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
