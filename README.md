# TwitOff
A web application for comparing Twitter users

# pipenv install

# pipenv shell

# python -m pip install -r requirements.txt

ERROR: Command errored out with exit status 1:
     command: /Users/jamesrowland/.local/share/virtualenvs/TwitOff2-lB4Oa0xD/bin/python -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/2_/ty041dd91nl6kn0t4yj_xxwr0000gn/T/pip-install-umj3dn0k/psycopg2/setup.py'"'"'; __file__='"'"'/private/var/folders/2_/ty041dd91nl6kn0t4yj_xxwr0000gn/T/pip-install-umj3dn0k/psycopg2/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base pip-egg-info
         cwd: /private/var/folders/2_/ty041dd91nl6kn0t4yj_xxwr0000gn/T/pip-install-umj3dn0k/psycopg2/
    Complete output (23 lines):
    running egg_info
    creating pip-egg-info/psycopg2.egg-info
    writing pip-egg-info/psycopg2.egg-info/PKG-INFO
    writing dependency_links to pip-egg-info/psycopg2.egg-info/dependency_links.txt
    writing top-level names to pip-egg-info/psycopg2.egg-info/top_level.txt
    writing manifest file 'pip-egg-info/psycopg2.egg-info/SOURCES.txt'
    
    Error: pg_config executable not found.
    
    pg_config is required to build psycopg2 from source.  Please add the directory
    containing pg_config to the $PATH or specify the full executable path with the
    option:
    
        python setup.py build_ext --pg-config /path/to/pg_config build ...
    
    or with the pg_config option in 'setup.cfg'.
    
    If you prefer to avoid building psycopg2 from source, please install the PyPI
    'psycopg2-binary' package instead.
    
    For further information please check the 'doc/src/install.rst' file (also at
    <http://initd.org/psycopg/docs/install.html>).
    
    ----------------------------------------
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.


# pip install psycopg2-binary

# python app.py

    from decouple import config
ModuleNotFoundError: No module named 'decouple'

# pip install python-decouple

Traceback (most recent call last):
  File "app.py", line 4, in <module>
    from flask import Flask, render_template, request
ModuleNotFoundError: No module named 'flask'

# python app.py

Traceback (most recent call last):
  File "app.py", line 4, in <module>
    from flask import Flask, render_template, request
ModuleNotFoundError: No module named 'flask'
(TwitOff2) bash-3.2$ pip install flask

# pip install flask

# python app.py

Traceback (most recent call last):
  File "app.py", line 5, in <module>
    from .models import DB, User
ModuleNotFoundError: No module named '__main__.models'; '__main__' is not a package
  
# [removed .notation from beginnings of app.py and twitter.py]

# pip install flask_sqlalchemy
# pip install tweepy
# pip install basilica

# python app.py

# [changed twitter api keys]

Traceback (most recent call last):
  File "app.py", line 6, in <module>
    from twitter import add_or_update_user, add_users
  File "/Users/jamesrowland/Desktop/TwitOff2/TwitOff/twitoff/twitter.py", line 7, in <module>
    TWITTER_AUTH = tweepy.OAuthHandler(config('twitter api key'),
  File "/Users/jamesrowland/.local/share/virtualenvs/TwitOff2-lB4Oa0xD/lib/python3.7/site-packages/decouple.py", line 197, in __call__
    return self.config(*args, **kwargs)
  File "/Users/jamesrowland/.local/share/virtualenvs/TwitOff2-lB4Oa0xD/lib/python3.7/site-packages/decouple.py", line 85, in __call__
    return self.get(*args, **kwargs)
  File "/Users/jamesrowland/.local/share/virtualenvs/TwitOff2-lB4Oa0xD/lib/python3.7/site-packages/decouple.py", line 70, in get
    raise UndefinedValueError('{} not found. Declare it as envvar or define a default value.'.format(option))
decouple.UndefinedValueError: 'twitter api key' not found. Declare it as envvar or define a default value.

