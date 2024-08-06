English | [中文](https://github.com/mushinbush/discord-bot-hakka/blob/main/.github/readme_zh.md)

## Description:

This repository hosts a Discord chat bot that leverages some APIs to run conversational models, features:

- Easy one-click installation, simply download and deploy directly (requires python installed).
- Engages in conversations using natural language processing models through APIs that's currently free!
- Customizable personality, allowing to configure the bot's behavior and features to suit your needs.
- Current support: Google's [Gemini](https://ai.google.dev/gemini-api), Cohere's [Command-R+](https://docs.cohere.com/docs/rate-limits)

## Usage:
### Windows
1. Get your own API keys from [Google Gemini](https://ai.google.dev/gemini-api) or [Cohere](https://dashboard.cohere.com).
2. Create your Discord bot and obtain your Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).
3. Install [Python](https://www.python.org/). Make sure to check "Add Python X.X to PATH" during the installation!
4. Clone this repository to your local machine, or you can simply download it (Code -> Download ZIP).
5. Run the `start.bat` file; this will create a virtual environment (venv) and install necessary dependencies.
6. Enter your API key and Discord bot token into `config.json`, then re-run `start.bat`. You can change to your designated model.
7. All set!
### Linux
1. Almost identical to Windows, just run `start.sh` instead.

## Configs:

- You can modify the bot in `config.json`:
  - `sysprompt`: System prompt that defines commands, personality, etc...
  - `sysfstmsg`: An example message from the bot that can better guide the bot's speaking manner.
  - `trigger`: The trigger word for the bot. When a message starts with the configured `trigger`, the bot will respond. Default is `AI,`.
  - `cleantrig`: The trigger word to clear the bot's memory. When a message starts with the configured `cleantrig`, the bot's current memory will be cleared. Default is `cleanAI`.