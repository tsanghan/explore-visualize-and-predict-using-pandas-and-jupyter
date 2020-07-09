ENV := ../env

.phony: help
help:
	@echo 'make update       Build class'


.phony: update
update:
	$(ENV)/bin/jupyter_manip -r --input "Solutions/begpandas.py" --output "Class/begpandas.ipynb"
	$(ENV)/bin/jupyter_manip -r --input "Solutions/mastering_pandas.py" --output "Class/mastering_pandas.ipynb" 
