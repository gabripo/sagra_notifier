# SAGRA-NOTIFIER 🌭🐖
Do not miss out the sagre!

The application lists all the sagre at [https://www.sagreinemilia.it/sagre_per_provincia/8/ferrara](https://www.sagreinemilia.it/sagre_per_provincia/8/ferrara) .

## Deployed version
"Yeah, I do not care about code and all these nerd-stuff! I want just my sagra!"
"Ok! Go here [https://sagra-info-5d63fun7iq-oa.a.run.app/](https://sagra-info-5d63fun7iq-oa.a.run.app/) "

## Technical aspects (may result boring and interesting at the same time)
- Backend: [Flask](https://flask.palletsprojects.com/en/stable/) 🌶️
- Frontend: plain HTML file
- Web Server: [gunicorn](https://gunicorn.org/) 🦄
- Containerazed application through [Docker](https://www.docker.com/) 🐳
- Hosted on [GCP](https://console.cloud.google.com/)

## "I want to develop it further!"
Here we go, another nerd doing unuseful stuff...

Ok, set-up your configuration with:
```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

The Flask executable is `flask_app.py` : by running it
```bash
python flask_app.py
```
the application will be served on [http://0.0.0.0:3000](http://0.0.0.0:3000) .
