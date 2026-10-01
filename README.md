# Team Shoutouts 📣

A tiny project for learning GitHub. Shoutouts live in `messages.json`,
and our Slack bot replies with the latest one.

## Talk to the bot in Slack
- **@mention the bot**: it says hello
- **Type `shoutout`**: it replies with the newest shoutout in `messages.json`

## Run the bot
```
pip3 install -r requirements.txt
export SLACK_BOT_TOKEN="xoxb-..."
export SLACK_APP_TOKEN="xapp-..."
python3 bot.py
```
The bot only responds while this is running. Never commit the tokens.

## Add a shoutout
1. Create a branch: `git checkout -b add-my-shoutout`
2. Add your entry to the end of `messages.json`
3. Commit and push, then open a pull request and merge it
4. Pull the latest `main`, restart the bot, and type `shoutout` in Slack
