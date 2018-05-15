# Every Makefile should contain this line to avoid trouble on systems where 
# SHELL variable might be inherited. (Not a problem with GNU make).
SHELL=/bin/sh
###############################################################################
APP_NAME=newproj1
APP_PATH=~/.vim/plugin/vimide/samples/python
# in-project log path
LOG_PATH=$(APP_PATH)/log
# alt log path (e.g., logging to RAM disk)
#LOG_PATH=/var/log/$(APP_NAME)
###############################################################################
# RUN_LOG is where console output lands (e.g. runtime errors)
RUN_LOG=$(LOG_PATH)/run.log
# INFO_LOG et al. is where python logging calls land
# (assuming logging.yaml uses the default setup)
# (viewable with make tail-info, etc.)
INFO_LOG=$(LOG_PATH)/info.log			# INFO level logs and above
DEBUG_LOG=$(LOG_PATH)/debug.log			# DEBUG level logs and above
WARNING_LOG=$(LOG_PATH)/warning.log		# WARNING level logs and above
ERROR_LOG=$(LOG_PATH)/error.log			# ERROR level logs and above
# TEST_LOG is the output redirection file for `make test`
# (viewable with `make tail-test`)
TEST_LOG=$(LOG_PATH)/test.log
###############################################################################

# By default, make operates on files, so if there is a file called
# clean-pyc it will try use it instead of a command. Use .PHONY to avoid this:
.PHONY: setup run kill test \
	tail-info tail-debug tail-warning tail-error tail-console tail-test \
	clean clean-pyc log-search

setup:
	@mkdir -p $(LOG_PATH)

test: log-separator
	@touch $(TEST_LOG)
	@echo '' >> $(TEST_LOG)
	@echo '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^' >> $(TEST_LOG)
	@echo '' >> $(TEST_LOG)
	@cd $(APP_PATH) && pipenv run python -u -m unittest discover > $(TEST_LOG) 2>&1 &

run: kill
	@touch $(RUN_LOG)
	@cd $(APP_PATH) && pipenv run python -u app.py > $(RUN_LOG) 2>&1 &

kill: log-separator
	-pkill python

###############################################################################
# view log files
###############################################################################
define tail_file
	@touch $(1)
	@# output tail stderr to /dev/null ("file truncated...")
	-@tail -f $(1) 2> /dev/null
endef
tail-console: setup
	$(call tail_file, $(RUN_LOG))
tail-info: setup
	$(call tail_file, $(INFO_LOG))
tail-debug: setup
	$(call tail_file, $(DEBUG_LOG))
tail-warning: setup
	$(call tail_file, $(WARNING_LOG))
tail-error: setup
	$(call tail_file, $(ERROR_LOG))
tail-test: setup
	$(call tail_file, $(TEST_LOG))
###############################################################################

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +

clean: clean-pyc 

log-separator: setup
	@echo '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^' >> $(INFO_LOG)
	@echo '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^' >> $(DEBUG_LOG)
	@echo '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^' >> $(WARNING_LOG)
	@echo '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^' >> $(ERROR_LOG)
	@echo '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^' >> $(RUN_LOG)

help:
	@echo 'read the Makefile :/'

