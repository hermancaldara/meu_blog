PYTHON = python
PIP = pip

tudo: dependências

dependências: django django-pagination django-taggit should_dsl pygments docutils disqus

django:
	@$(PYTHON) -c 'import django' 2>/dev/null || $(PIP) install django
	
django-pagination:
	@$(PYTHON) -c 'import pagination' 2>/dev/null || $(PIP) install django-pagination

django-taggit:
	@$(PYTHON) -c 'import taggit' 2>/dev/null || $(PIP) install django-taggit

should_dsl:
	@$(PYTHON) -c 'import should_dsl' 2>/dev/nulll || $(PIP) install should_dsl
	
pygments:
	@$(PYTHON) -c 'import pygments' 2>/dev/null || $(PIP) install pygments
	
docutils:
	@$(PYTHON) -c 'import docutils' 2>/dev/null || $(PIP) install docutils
	
django-disqus:
	@$(PYTHON) -c 'import disqus' 2>/dev/null || $(PIP) install django-disqus
