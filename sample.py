"""
1. api tests_api class TestRegistrationEmail updated: test data is called from json file
2. utilities.test_data.py updated: function that parses json file is added
3. api tests_api sample tests_api, api unfinished tests are deleted
4. api tests_api class E2E, api est_e2e_student_regi_activ_sign_in are updated: test data is called from json file,
 created user is deleted after test execution
5. api test data is moved to api_test_data.json
6. modules for web testing are added: pom directory with page files, web.web_common.py with common selenium methods,
json with test data, conftest.py for browser invoking
7. web sing_in test suit is added: teacher positive/negative, student positive/negative
8. READ ME file is updated
9. Config.yaml updated: mock-service configurations are added

? waits
? git ignore

2 DO:

safari fix
firefox teardown

/// git reset --hard

*** Browser Stack ****

https://automate.browserstack.com/dashboard/v2/quick-start/setup-browserstack-sdk

1

# Set these values in your ~/.zprofile (zsh) or ~/.profile (bash)
export BROWSERSTACK_USERNAME="artkrylov_HOnNub"
export BROWSERSTACK_ACCESS_KEY="7jkViUM3qqpKcsPRRoos"

2

# install BrowserStack SDK
python3 -m pip install browserstack-sdk
# create browserstack.yml config file
browserstack-sdk setup --framework "pytest" --username "artkrylov_HOnNub" --key "7jkViUM3qqpKcsPRRoos"

3 browserstack.yml

userName: artkrylov_HOnNub
accessKey: 7jkViUM3qqpKcsPRRoos
platforms:
  - os: OS X
    osVersion: Ventura
    browserName: Chrome
    browserVersion: latest
  - os: Windows
    osVersion: 11
    browserName: Edge
    browserVersion: latest-beta
  - os: OS X
    osVersion: Big Sur
    browserName: Chrome
    browserVersion: 90.0
browserstackLocal: true
buildName: ASK 1.0.7
buildIdentifier: ${BUILD_NUMBER}
projectName: BrowserStack Sample
debug: true
networkLogs: true
consoleLogs: info
framework: pytest

4 browserstack-sdk pytest <path-to-test-files>

"""
