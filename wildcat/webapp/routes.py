from itertools import count
from flask import render_template
from webapp import app
# from Cartridge import Cartridge
from wildcat import __init__ as wildcat

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'fooooooo'}
    count = 1
    # cartridge = Cartridge.generate_cartridge(count)
    name = wildcat()
    return render_template('index.html', name=name)