import random

# Creating a list of emojis to choose from
emoji_list = [
    "📤", "📪", "📩", "🌡️", "🧪", "🧬", "📥", "💤", "📡",
    "💡", "🔦", "🧯", "🛜", "🆚", "💯", "🕳️", "🔎", "⚗️", 
    "🔭", "🔬", "⏰", "🔍", "💾", "🤹‍♂️", "⌚", "📱", "📲", 
    "🛎️", "🗝️", "🔑", "🔓", "🔏", "📶", "🚧", "🛰️", "🎱"
]

# Generating SSIDs by randomly selecting emojis and concatenating them to form a string of 7 emojis
ssids_emoji = ['"' + ''.join(random.choices(emoji_list, k=7)) + '"' for _ in range(32)]
ssids_emoji_row = ' '.join(ssids_emoji)
print(ssids_emoji_row)
