from flask import Flask
# Special variable (__name__) to identify the current application or module that is being rendered or passed to flask
app = Flask(__name__)

from application import routes
from application import pdf_img
