INSTALL_TO=/opt/hrai
MASTER_PY=hrai.py
HELPERS=add.py add-category.py init.py list.py mark.py

BASH_COMPLETION=bash_completion.d/hrai
BASH_COMPLETION_INSTALL_TO=$$HOME/.bash_completion.d

all:
	@echo Nothing to do here...

install:
	@mkdir -p $(INSTALL_TO)/bin
	@mkdir -p $(INSTALL_TO)/libexec
	@cp $(MASTER_PY) $(INSTALL_TO)/bin/$(basename $(MASTER_PY))
	@cp $(HELPERS) $(INSTALL_TO)/libexec/
	@cp $(BASH_COMPLETION) $(BASH_COMPLETION_INSTALL_TO)
