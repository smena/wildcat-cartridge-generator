from itertools import count
from flask import render_template
from webapp import app
from Cartridge import Cartridge
from argparse import Namespace

@app.route('/')
@app.route('/index')
def index():
    args_dict = {'username': 'fooooooo',
                'count': 1
                }
    args = Namespace(**args_dict)
    # cartridge = Cartridge.generate_cartridge(count)
    name = Cartridge.generate_cartridge(args)
    print(name)
    return render_template('index.html', name=name)