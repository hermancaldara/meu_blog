PYTHON = python
PIP = pip

tudo: dependências

dependências: django django-pagination django-taggit

django:
	@$(PYTHON) -c 'import django' 2>/dev/null || $(PIP) install django
	
django-pagination:
	@$(PYTHON) -c 'import pagination' 2>/dev/null || $(PIP) install django-pagination

django-taggit:
	@$(PYTHON) -c 'import taggit' 2>/dev/null || $(PIP) install django-taggit
