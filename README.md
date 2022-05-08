# wildcat-cartridge-generator

Invents new firearm cartridges to inspire your next wildcatting project

# Use local package

```
wildcat $ python3 -m venv venv
wildcat $ source venv/bin/activate
(venv) wildcat $ pip install --editable .
(venv) wildcat $ wildcat
```

# Run flask locally

```
(venv) flask run
 * Serving Flask app 'wildcat.py' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

# Manage deployment with Zappa via Dockerfile
## Deploy

```
$ export AWS_ACCESS_KEY_ID=xxxxxxxxxxxxxxxx
$ export AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxx
$ docker build --platform linux/x86_64 --tag wildcat .
$ docker run -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -it wildcat zappa deploy
```

## Undeploy

```
$ docker run -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -it wildcat zappa undeploy
```