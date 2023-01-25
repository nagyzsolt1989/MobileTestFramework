<div align="center">

![Logo](https://user-images.githubusercontent.com/12999800/214615365-86872ee9-1d11-42d0-91a6-bc4a6646d9af.jpeg)

# Python Mobile Automation Framework

[Overview](#scroll-overview)
•
[Framework Stack](#factory-framework-stack)
•
[Documentation](#blue_book-documentation)
•
[Demo](#dvd-demo)

</div>

## :bookmark_tabs: Menu

- [Overview](#scroll-overview)
- [Framework Stack](#factory-framework-stack)
- [Documentation](#blue_book-documentation)
    - [Prerequisites](#exclamation-prerequisites)
    - [Design Patterns](#rice_scene-design-patterns)
    - [Directory Tree](#open_file_folder-directory-tree)
    - [Dependencies and libs](#floppy_disk-dependencies)
- [Demo](#dvd-demo)

## :scroll: Overview

An end to end python mobile test framework utilizing the latest tech available in January 2023.

## :factory: Framework Stack

![framework stack](https://user-images.githubusercontent.com/12999800/214615298-6245117d-e794-4bda-a8ca-79d8319cfc09.png)

# :blue_book: Documentation

## :exclamation: Prerequisites

- Python 3
- Pycharm
- PIP
- Appium 2
- Selenium 4
- Android Emulator 
- iOS Simulator

## :rice_scene: Design Patterns


## Getting Started
```
1. git clone https://github.com/nagyzsolt1989/MobileTestFramework.git
2. Navigate to `MobileTestFramework`and install the requirements with `pip install requirements.txt`
3. Replace <ANDROID EMULATOR> placeholder with you Android Emulator in MobileTestFramework/tests/android/AndroidBaseTest.py
4. Replace <ANDROID APP ABSOLUTE PATH> placeholder with the absolute path of your apk in MobileTestFramework/tests/android/AndroidBaseTest.py
5. Change the platformVersion value to your emulators' version if it is neccessary
6. Replace <IOS SIMULATOR> placeholder with you iOS Simulator in MobileTestFramework/tests/ios/IOSBaseTest.py
4. Replace <IOS APP ABSOlUTE PATH> placeholder with the absolute path of your zip in MobileTestFramework/tests/ios/IOSBaseTest.py
5. Change the platformVersion value to your simulators' version if it is neccessary
```

## Running a Test
```
1. Run `pytest -v <FILE_NAME> --html=test_report.html` in the terminal to start a test execution
```

### Reports used
- Pytest HTML Report

## :floppy_disk: Dependencies

## :open_file_folder: Directory Tree
```
/Users/zsnagy/Repos/MobileTestFramework

├── apps
│   ├── demoApp.apk
│   └── demoApp.zip
├── framework
│   ├── __init__.py
│   └── core
│       ├── __init__.py
│       ├── page_base.py
│       └── test_base.py
├── pages
│   ├── __init__.py
│   ├── android
│   │   ├── __init__.py
│   │   ├── page_home.py
│   │   ├── page_sign_in.py
│   │   └── page_validation.py
│   └── ios
│       ├── __init__.py
│       ├── page_home.py
│       ├── page_sign_in.py
│       └── page_validation.py
├── tests
│   ├── __init__.py
│   ├── android
│   │   ├── __init__.py
│   │   ├── test_home.py
│   │   ├── test_sign_in.py
│   │   └── test_validation.py
│   └── ios
│       ├── __init__.py
│       ├── test_home.py
│       ├── test_sign_in.py
│       └── test_validation.py
├── utils
│   ├── __init__.py
│   ├── listeners
│   │   ├── __init__.py
│   │   └── event_listener.py
│   └── slack
│       ├── __init__.py
│       └── slack_notification.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── testrail.cfg
```

## :dvd: Demo

![allure_1](https://user-images.githubusercontent.com/12999800/214614068-72a6030c-2d98-4619-a1d4-e2f13acfe9ee.png)
![allure_2](https://user-images.githubusercontent.com/12999800/214614118-8d032d5e-cc06-4725-a8ce-45dddf24dbae.png)

![slack_notification](https://user-images.githubusercontent.com/12999800/214614189-450c08d2-967a-4654-85e5-6a321738a34c.png)
