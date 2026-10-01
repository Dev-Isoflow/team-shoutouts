"""Shoutout Bot: listens to Slack and replies.

- @mention the bot  -> it says hello
- type "shoutout"   -> it replies with the latest shoutout from messages.json

Runs on your computer using Slack's Socket Mode (no server needed).
It only responds while this script is running.
"""
import json
import os
import re

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ["SLACK_BOT_TOKEN"])


def latest_shoutout():
    with open("messages.json", encoding="utf-8") as f:
        messages = json.load(f)
    latest = messages[-1]
    return f"📣 Shoutout from *{latest['from']}*: {latest['message']}"


@app.event("app_mention")
def say_hello(event, say):
    say(f"Hey <@{event['user']}>! 👋 Type `shoutout` to hear the latest shoutout.")


@app.message(re.compile(r"^shoutout$", re.IGNORECASE))
def reply_with_shoutout(say):
    say(latest_shoutout())


@app.event("message")
def ignore_other_messages():
    pass  # Every other message: do nothing


if __name__ == "__main__":
    print("⚡ Shoutout Bot is running. Press Ctrl+C to stop.")
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
