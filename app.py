# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:24:12 2021

@author: kevun
"""

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Sitio cargado en el servidor..."

@app.route("/qs")
def qs():
    return "Acerca de nuestro equipo de trabajo"
if __name__=='__main__':
    app.run(debug = True, port = 8000)