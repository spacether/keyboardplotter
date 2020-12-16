# 2.0.0 - draft
- KeyboardLayout layout_name input type changed from str to LayoutName enum
- Fixed typo in readme code sample
- Python samples renamed to include pygame_ or tkinter_ prefix
- Adds init docstrings to KeyboardInfo, KeyInfo
- Adds Rect class for keyboardlayout's tkinter implementation

# 1.0.0
- qwerty + azerty included
- dynamically generate a pygame sprite group showing a keyboard
- customize the keyboard with sizes, colors, key margin, padding, font, location, etc
- override the default KeyInfo by passing in overrides
- update a specific key with update_key