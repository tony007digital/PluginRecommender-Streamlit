import streamlit as st
import json
import pandas as pd

# This function will only be run once, and its result will be cached.
@st.cache(allow_output_mutation=True)
def load_data():
    with open('chatgpt_plugins.json', 'r', encoding='utf-8') as f:
        plugins = json.load(f)
    return plugins

# Load plugins list from chatgpt_plugins.json file
plugins = load_data()

# Convert plugins to DataFrame
df = pd.DataFrame(plugins)

# App title
st.title("Plugin Recommender for ChatGPT")

# Display DataFrame
st.dataframe(df)

# User input
user_input = st.text_input("What kind of project are you building?", "")

# Find plugins whose descriptions contain the user's input
matching_plugins = df[df['description'].str.contains(user_input, case=False, na=False)]

# Display the matching plugins
for index, plugin in matching_plugins.iterrows():
    st.write(f"**{plugin['name']}**: {plugin['description']}")