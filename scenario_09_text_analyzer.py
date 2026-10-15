msg = input("Enter a sentence or message: ")

total_chars = len(msg)
trimmed_len = len(msg.strip())

vowel_count = 0
digit_count = 0
space_count = 0

for ch in msg:
    lower_ch = ch.lower()
    if lower_ch == 'a' or lower_ch == 'e' or lower_ch == 'i' or lower_ch == 'o' or lower_ch == 'u':
        vowel_count += 1
    elif ch.isdigit():
        digit_count += 1
    elif ch == ' ':
        space_count += 1

search_phrase = input("Enter a word/phrase to search for: ")
phrase_found = search_phrase.lower() in msg.lower()

print("\n--- Text Message Analysis ---")
print(f"Original Message: {msg}")
print(f"Uppercase: {msg.upper()}")
print(f"Lowercase: {msg.lower()}")
print(f"Total Characters: {total_chars}")
print(f"Length excluding leading/trailing spaces: {trimmed_len}")
print(f"Number of Vowels: {vowel_count}")
print(f"Number of Digits: {digit_count}")
print(f"Number of Spaces: {space_count}")
print(f"Phrase '{search_phrase}' found: {phrase_found}")