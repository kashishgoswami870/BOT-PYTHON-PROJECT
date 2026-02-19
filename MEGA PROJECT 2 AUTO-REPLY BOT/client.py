from openai import OpenAI 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
base_url="https://openrouter.ai/api/v1",


  api_key="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",
)
command = """
[18:19, 2/18/2026] Kashish: hyyy
[18:19, 2/18/2026] Home Minister 🏡: Hello
[18:19, 2/18/2026] Home Minister 🏡: Bye
[18:19, 2/18/2026] Home Minister 🏡: Sinn
[18:19, 2/18/2026] Home Minister 🏡: Yhe
[18:19, 2/18/2026] Home Minister 🏡: To
[18:19, 2/18/2026] Kashish: what are you doing
[18:20, 2/18/2026] Home Minister 🏡: Kb chaligi niche
"""
completion = client.chat.completions.create(
  model="arcee-ai/trinity-large-preview:free",
  messages=[
    {"role": "system", "content": "You are a person named kashish who speaks hindi as well as english she is from India, Delhi and is a coder , You analyze chat history and respond like kashish"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)
#chatgpt is not free that,s why its not working....