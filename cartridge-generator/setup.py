from setuptools import setup

setup (
    name = 'wildcat',
    version = '0.1',
    py_modules = ['wildcat'],
    install_requires = [
        'markovify==0.9.4',
        'argparse==1.4.0',
        'flask==2.1.2',
        'python-dotenv==0.20.0'
    ],
    entry_points = '''
        [console_scripts]
        generate=generate:__init__
    '''
)