from spellchecker import SpellChecker

def spell_check(text):
    spell = SpellChecker()

    # Split the text into words
    words = text.split()

    # Find misspelled words
    misspelled = spell.unknown(words)

    # Correct misspelled words
    corrected_text = []
    for word in words:
        if word in misspelled:
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)

    return ' '.join(corrected_text)

# Example usage
text_to_check = result_text
corrected_text = spell_check(text_to_check)

print(f"Original text: {text_to_check}")
print(f"Corrected text: {corrected_text}")
