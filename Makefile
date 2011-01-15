PYTHON = python
PIP = pip

tudo: dependências

dependências: django django-pagination django-taggit should_dsl

django:
	@$(PYTHON) -c 'import django' 2>/dev/null || $(PIP) install django
	
django-pagination:
	@$(PYTHON) -c 'import pagination' 2>/dev/null || $(PIP) install django-pagination

django-taggit:
	@$(PYTHON) -c 'import taggit' 2>/dev/null || $(PIP) install django-taggit

should-dsl:
	@$(PYTHON) -c 'import should_dsl' 2>/dev/nulll || $(PIP) install should_dsl
