##1. Had to install virualenv & Django

It was actually already installed. I followed [this](https://docs.djangoproject.com/en/3.1/topics/install/#installing-an-official-release-with-pip) to do it.

To get into venv, you do `source /path/to/env/bin/activate`. Do deactivate it, do `deactivate`.

In venv, check python version, make sure it's v3.x. Then do `python -m pip install Django`. Check in python shell, or just `python -m django --version`.

**TODO** wasn't there a way where just entering the env activated the env? Something like that. Document it. _(yeah, it does enter automatically. I updated ohmyzsh, and that stopped it from happening this last time, which is why I was confused. Nothing in my ~/.zshrc seems to make the venv activate happen. Huh. Magic ✨)_

## Creating project

`django-admin startproject mysite`

Can reference what each file does [here](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#creating-a-project).

run with `python manage.py runserver`

I created polls with `python manage.py startapp polls`