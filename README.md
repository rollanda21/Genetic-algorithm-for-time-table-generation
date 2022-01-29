# Genetic-algorithm-for-time-table-generation

## Getting started
Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r https://raw.githubusercontent.com/juanifioren/django-project-template/master/requirements.txt

# You may want to change the name `projectname`.
$ django-admin startproject --template https://github.com/juanifioren/django-project-template/archive/master.zip projectname

$ cd projectname/
$ cp settings_custom.py.edit settings_custom.py
$ python manage.py migrate
$ python manage.py runserver
```

## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).
* time table generation.
* Sqlite database is okay.
* The user athentication system is complete!
* Admin params: username: admin
*               pwd: admin

## Feel free to reach out to me with your questions here: rollanda21@gmail.com 

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.
