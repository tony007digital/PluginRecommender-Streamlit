import json

# Read the file
with open('chatgpt_plugins.json', 'r', encoding='utf-8') as f:
    data = f.read()

# Escape control characters
cleaned_data = json.dumps(data)

# Write the cleaned data back to the file
with open('chatgpt_plugins.json', 'w', encoding='utf-8') as f:
    f.write(cleaned_data)