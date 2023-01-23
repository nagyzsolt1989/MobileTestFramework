<div align="center">

![Logo](docs/logo.jpeg)

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

## :dvd: Demo

### Sample Report
![Screenshot 2022-07-12 at 23 24 20](https://user-images.githubusercontent.com/12999800/178598510-bc1a6e26-0fe1-40d7-8ec9-cabecb6b2fa7.png)
