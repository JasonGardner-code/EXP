import random
import emoji

def overlay_emoji(emoji_text, overlay_text):
    combined_text = emoji_text + overlay_text
    return combined_text

emoji_list = [
    ":smile:",
    ":heart:",
    ":star:",
    ":fire:",
    ":rocket:"
]

unicode_list = [
    "\u0300", "\u0301", "\u0302", "\u0303", "\u0304", "\u0305",
    "\u0306", "\u0307", "\u0308", "\u0309", "\u030A", "\u030B",
    "\u030C", "\u030D", "\u030E", "\u030F", "\u0310", "\u0311",
    "\u0312", "\u0313", "\u0314", "\u0315", "\u0316", "\u0317",
    "\u0318", "\u0319", "\u031A", "\u031B", "\u031C", "\u031D",
    "\u031E", "\u031F",
    "\u1D49E", "\u1D49F", "\u1D4A2", "\u1D4A5", "\u1D4A9", "\u1D4AA",
    "\u1D4AB", "\u1D4AC", "\u1D4AE", "\u1D4AF", "\u1D4B0", "\u1D4B1",
    "\u1D4B2", "\u1D4B3", "\u1D4B4", "\u1D5C7", "\u1D5C8", "\u1D5C9",
    "\u1D5CA", "\u1D5CB"
]

emoji_text = random.choice(emoji_list)
overlay_text = random.choice(unicode_list)

custom_emoji = overlay_emoji(emoji_text, overlay_text)
print(custom_emoji)
