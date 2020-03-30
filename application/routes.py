import os
from application import app
from flask import render_template, request, redirect, url_for, json, Response
from application import pdf_img
from PIL import Image

# This could be the Root directory in the URL
# Note: These are called decorators. They decorate the underline definition or function.
@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", index=True, loginUser=True)
@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/courses")
def courses():
    courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]

    return render_template("courses.html", courseData=courseData, courses=True)

@app.route("/register")
def register():
    return render_template("register.html", register=True)

@app.route('/upload', methods=['POST'])
def upload():
    loginUser = False
    pdf_target = os.path.join(pdf_img.APP_ROOT, 'static/pdf')

    # Preparing directory
    if not os.path.isdir(pdf_target):
        os.mkdir(pdf_target)

    # Uploading File
    for file in request.files.getlist('file'):
        filename = file.filename
        destination = "/".join([pdf_target,filename])
        file.save(destination)

        # Creating images
        if os.path.isfile(destination):
            imgPath_data = pdf_img.prepare_images(destination)
            loginUser = False
            
    return render_template("index.html", loginUser=loginUser, imgStatus=True, imgPath_data=imgPath_data)

@app.route("/api/")
def api():

    filename = "CR 2019-0976-0979-1.pdf"
    pdf_target = os.path.join(pdf_img.APP_ROOT, 'static/pdf')
    destination = "/".join([pdf_target,filename])

    # Creating images
    if os.path.isfile(destination):
        imgPath_data = pdf_img.prepare_images(destination)
        loginUser = False
    return Response(json.dumps(imgPath_data), mimetype="application/json")
