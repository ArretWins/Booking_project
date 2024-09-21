PYTEST=pytest
ALLURE_DIR=allure-results/
ALL=allure_all


MAIN_FILES = tests/test_main.py

test-all:
	$(PYTEST) --alluredir $(ALLURE_DIR)$(ALL)

test-all-firefox:
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR)$(ALL)

report-all:
	allure serve $(ALLURE_DIR)$(ALL)
