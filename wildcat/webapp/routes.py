from flask import render_template
from webapp import app
import wildcat

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'fooooooo'}
    name = wildcat.Cartridge()
    return render_template('index.html', name=name)