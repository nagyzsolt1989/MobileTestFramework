from dotenv import load_dotenv
import requests
import json
import os

# Add your slack webhook as SLACK_WEB_HOOK in the .env file of the project root
load_dotenv(".env")
web_hook = os.getenv("SLACK_WEB_HOOK")


def send_slack_notification(web_hook, message):
    url = web_hook
    data = message
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    requests.post(url, data=json.dumps(data), headers=headers)


def compose_message(platform, device, os, passed, failed, skipped, total, duration, failed_tests):
    return {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*" + platform + " Test Result*"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Device:*\n" + device
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*App version:*\n1.12.0"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Operating System:*\n" + platform + " " + os
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Environment:*\n Stage"
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Branch:*\n <google.com|Master>"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Commit:*\n <google.com|Add Slack integration>"
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Execution time:*\n" + duration
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*\u2022 Passed:* " + str(passed) + "\n*\u2022 Failed:* " + str(failed) +
                            "\n*\u2022 Skipped:* " + str(skipped) + "\n\n*\u2022 Total:* " + str(total)
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://files.slack.com/files-pri/T04KPGE914Y-F04KTER7W3V/ios.png",
                    "alt_text": "platform_icon",
                },
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Failed test cases:*\n" + failed_tests
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Pipeline:*\n <google.com|#10356>"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Allure:*\n <google.com|Test Report>"
                    }
                ]
            },
        ]
    }
