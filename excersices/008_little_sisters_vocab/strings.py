"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return f"un{word}"


def make_word_groups(vocab_words: list[str]):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix = f" {vocab_words[0]}"
    word_with_prefix = prefix.join(vocab_words)
    return word_with_prefix.replace(" ", " :: ")


def remove_suffix_ness(word: str):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    if word.endswith("ness"):
        new_word = word[:-4]
        if new_word and new_word[-1] == 'i':
            new_word = new_word[:-1] + 'y'
        return new_word
    return word


print(remove_suffix_ness("sadness"))


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    words = sentence.split()
    adjective = words[index]
    adjective = adjective.strip(".")
    if adjective.endswith("y"):
        adjective = adjective[:-1] + "i"
    return adjective + "en"
