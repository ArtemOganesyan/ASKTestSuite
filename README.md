# Framework for UI, API, dB Testing/Data Verification

External packages:
1. pytest (Test) 
2. mysql-connector-python (dB)
3. pyyaml (.yaml parser)
4. requests (API)
5. selenium (WEB)
6. webdriver-manager(WEB)
7. pytest-xdist (WEB)

Useful links:

* [ASK API documentation](http://ask.portnov.com/api-doc/#/)
* [pytest documentation](https://docs.pytest.org/en/7.2.x/)
* [requests documentation](https://pypi.org/project/requests/)
* [mysql-connector-python documentation](https://pypi.org/project/mysql-connector-python/)
* [selenium documentation](https://pypi.org/project/selenium/)
* [webdriver-manager documentation](https://pypi.org/project/webdriver-manager/)
* [pytest-xdist](https://pypi.org/project/pytest-xdist/)



Configuration:
* config.yaml

CLI options for parallel execution:
* -n=auto (to execute all tests collected)
* -n=<number of tests to be execute>

CLI options for browser modes:
* --browser chrome
* --browser firefox
* default browser is chrome
* --mode headless
* default browser mode is regular (ui) 

CLI options for generating allure reports
* pytest --alluredir allure test.py
* allure serve allure

* --lf - to rerun failing tests