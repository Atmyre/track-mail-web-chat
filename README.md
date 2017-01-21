# track-mail-web
Social network as 2nd term Technotrack project autumn 2016

Register-Login/Logout, chat made on React functionality

------------------
### virtualenv:
trackwebenv: sourse trackwebenv/bin/activate

------------------
### start celery:
celery -A social_n worker -l info --beat

------------------
### build webpack (react):
./node_modules/.bin/webpack --config webpack.config.js

------------------
### start centrifugo:
./centrifugo --admin --web

### tutorials:
django oauth tutorial: 
http://django-oauth-toolkit.readthedocs.io/en/latest/tutorial/tutorial_01.html
react configuration tutorial: 
http://geezhawk.github.io/using-react-with-django-rest-framework , 
http://djbook.ru/examples/75/
