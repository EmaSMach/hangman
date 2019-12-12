REPLACEMENTS = (
    ('á', 'a'),
    ('é', 'e'),
    ('í', 'i'),
    ('ó', 'o'),
    ('ú', 'u'),
    ('ü', 'u')
)

def clean_word(word):
    """Remove all the 'tildes and diéresis' from the given word"""
    word = word.lower().strip()
    for replacement in REPLACEMENTS:
        word = word.replace(replacement[0], replacement[1])
    return word

if __name__ == '__main__':
    # testing our clean_word function
    print('word', clean_word('repláctaño  Ú Ü'))
    print('word', '"' + clean_word('  í  Ó úÚ ') + '"')
