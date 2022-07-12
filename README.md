# MobileTestFramework
Sample Appium Test Framework in Python

## Pre-Requisite
```
1. Python 3
2. Pycharm
3. PIP
4. Running Appium client
5. Suitable Android and iOS binaries
```

## Getting Started
```
1. git clone https://github.com/nagyzsolt1989/MobileTestFramework.git
2. Navigate to `MobileTestFramework`and install the requirements with `pip install to-requirements.txt`
3. Replace <ANDROID EMULATOR> placeholder with you Android Emulator in MobileTestFramework/tests/android/AndroidBaseTest.py
4. Replace <ANDROID APP ABSOLUTE PATH>> placeholder with the absolute path of your apk in MobileTestFramework/tests/android/AndroidBaseTest.py
5. Change the platformVersion value to your emulators' version
6. Replace <IOS SIMULATOR> placeholder with you iOS Simulator in MobileTestFramework/tests/ios/IOSBaseTest.py
4. Replace <IOS APP ABSOlUTE PATH> placeholder with the absolute path of your zip in MobileTestFramework/tests/ios/IOSBaseTest.py
5. Change the platformVersion value to your simulators' version
```

## Runing a Test
```
1. Run `pytest -v <FILE_NAME> --html=test_report.html` in the terminal to start a test execution
```

### Reports used
- Pytest HMTL Report

### Sample Report
![Screenshot 2022-07-12 at 23 24 20](https://user-images.githubusercontent.com/12999800/178598510-bc1a6e26-0fe1-40d7-8ec9-cabecb6b2fa7.png)
