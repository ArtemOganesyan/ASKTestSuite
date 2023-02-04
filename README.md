# Framework for UI, API, dB Testing/Data Verification

External packages:
1. pytest (Test) 
2. mysql-connector-python (dB)
3. pyyaml (.yaml parser)
4. requests (API)
5. selenium (WEB)
6. webdriver-manager(WEB)
7. pytest-xdist (WEB)
8. pytest-selenium(Browserstack integration)

Useful links:

* [ASK API documentation](http://ask.portnov.com/api-doc/#/)
* [pytest documentation](https://docs.pytest.org/en/7.2.x/)
* [requests documentation](https://pypi.org/project/requests/)
* [mysql-connector-python documentation](https://pypi.org/project/mysql-connector-python/)
* [selenium documentation](https://pypi.org/project/selenium/)
* [webdriver-manager documentation](https://pypi.org/project/webdriver-manager/)
* [pytest-xdist](https://pypi.org/project/pytest-xdist/)
* [pytest-selenium](https://pypi.org/project/pytest-selenium/)
* [browserstack](https://automate.browserstack.com/dashboard/v2/quick-start/setup-browserstack-sdk)





Configuration:
* config.yaml

CLI options for parallel execution:
* -n=auto (to execute all tests collected)
* -n=<number of tests to be executed>

CLI options for cross-browser execution:
* --browser chrome
* --browser firefox
* default browser is crome

CLI options for browser-stack execution:
* browserstack-sdk pytest tests_web/test_sign_in.py
* make sure browserstackLocal option is set to  'false' in browserstack.yaml

