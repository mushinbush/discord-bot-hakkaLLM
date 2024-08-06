import os, time, shutil, sys, yaml
import discord
from litellm import completion

# cfgs
if not os.path.exists('config.yml'):
    shutil.copyfile('config_example.yml', 'config.yml')
    print("\nCreated new config.yml. Enter your API key and Discord bot token into the config file and restart.")
    sys.exit()
with open('config.yml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

MODEL = config.get('model', 'gemini-1.5-flash')
APIKEY = config.get('api-key')
if APIKEY == "YOUR_API_KEY" or not APIKEY:
    raise ValueError("API key is required in the config file")
BOTTOKEN = config.get('token')
if BOTTOKEN == "YOUR_DISCORD_BOT_TOKEN" or not BOTTOKEN:
    raise ValueError("Discord bot token is required in the config file")
TRIG = config.get('trigger')
CLNT = config.get('cleantrig')
SYSP = config.get('sysprompt')
SYSM = config.get('sysfstmsg')

# Create bot
intents = discord.Intents.default()
intents.message_content = True
activity = discord.CustomActivity(MODEL)
client = discord.Client(intents=intents, activity=activity)

# API Key
if MODEL.startswith('gemini'):
    os.environ['GEMINI_API_KEY'] = APIKEY
    FMODEL = f'gemini/{MODEL}'
elif MODEL.startswith('command'):
    os.environ['COHERE_API_KEY'] = APIKEY
    FMODEL = MODEL

global history
history = []

@client.event
async def on_ready():
    print('Startup complete. Bot is ready!')

# System prompt & First msg
def historyInit():
    history.append({
            "role": "system",
            "content": SYSP
        })
    history.append({
            "role": "assistant",
            "content": SYSM
    })
historyInit()

def requestLLM(chat_prompt):
    max_retries = 5  # Maximum retry
    retries = 0  # Current retry
    history.append({"role": "user", "content": chat_prompt})
    history_copy = history.copy()
    while retries < max_retries:
        try:
            start_time = time.time()
            response = completion(
                model = FMODEL, 
                messages=history_copy
            )
            end_time = time.time()
            elapsed_time = end_time - start_time

            if response.choices[0].finish_reason == 'stop':
                # print(response)
                reply = response.choices[0].message.content
                print(f"Response: {reply}|Inference time = {round(elapsed_time, 2)}s")
                history.append({"role": "assistant", "content": reply})
                return reply
            else:
                print('Cannot connect to API, retrying')
        except Exception as e:
            retries += 1
            print(f'API Error: {str(e)}')
            if retries == max_retries:
                return 'API error: Retry limit exceeded.'


@client.event
async def on_message(message):
    substring_to_remove = TRIG
    # Bot ignores itself
    if message.author == client.user:
        return
    # Check trigger
    if message.content.startswith(substring_to_remove):
        text_input = message.content[len(substring_to_remove):]
        print("===========================\nInput:" + text_input)
        await message.channel.send(requestLLM(text_input))
    # Check clear trigger
    if message.content.startswith(CLNT):
        global history
        history.clear()
        historyInit()
        print("Memory Cleared.")
        await message.channel.send("Memory Cleared.")
# Start bot
client.run(BOTTOKEN)
