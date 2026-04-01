import re


biased_dict_raw = {
    ("career girl", "career man"): ["professional", "manager", "executive"],
    ("businessman", "businesswoman"): ["business executive", "entrepreneur"],
    ("saleslady", "salesman"): ["sales clerk", "sales rep", "sales agent"],
    ("landlady", "landlord"): ["proprietor", "building manager"],
    ("chairwoman", "chairman"): ["chair", "chairperson"],
    ("brotherhood", "sisterhood"): ["kinship", "community"],
    ("policeman", "policewoman"): ["police officer"],
    "mankind": ["humankind"],
    "cleaning lady": ["cleaner"],
    "delivery boy": ["courier", "messenger"],
    "manpower": ["workforce"],
    "mailman": ["mail carrier", "letter carrier"],
    "newsman": ["journalist", "reporter"],
    "waitress": ["server", "waiter"],
    "alumni": ["graduates"],
    "freshman": ["first-year student"],
    "middleman": ["go-between"],
    "spokesman": ["spokesperson", "representative"],
    "countryman": ["compatriot"],
    "fatherland": ["native land"],
    "king-size": ["jumbo", "gigantic"],
    "manpower": ["human resources"],
    "man made": ["artificial", "synthethic", "machine-made"],
    "motherly": ["loving", "warm", "nurturing"],
    "camera man": ["camera operator", "camera crew"],
}


biased_dict = {}
for k, v in biased_dict_raw.items():
    if isinstance(k, tuple):
        for phrase in k:
            biased_dict[phrase] = v
    else:
        biased_dict[k] = v


sorted_keys = sorted(biased_dict.keys(), key=len, reverse=True)

parts = []
group_to_key = {}
for i, key in enumerate(sorted_keys):

    escaped = re.escape(key).replace(r'\ ', r'\s+')
    group_name = f"K{i}"
    parts.append(fr"(?<!\w)(?P<{group_name}>{escaped})(?!\w)")
    group_to_key[group_name] = key


pattern = re.compile("|".join(parts), flags=re.IGNORECASE)


def highlight_text(text):
    """
    Highlight biased words/phrases and return:
    - highlighted HTML string
    - set of suggestions (dictionary key, replacements)
    """
    suggestions = set()

    def _repl(match):
        g = match.lastgroup
        key = group_to_key[g]
        matched = match.group(0)

        replacement = biased_dict[key]
        suggestions.add((key, tuple(replacement)))

        return f"<span style='background-color: yellow; font-weight:bold;'>{matched}</span>"

    highlighted = pattern.sub(_repl, text)
    return highlighted, suggestions


def calculate_bias_percentage(text):
    """
    Returns:
    - bias_percentage (float)
    - biased_count (int)
    - total_words (int)
    """

    # Count total words
    words = re.findall(r"\b\w+\b", text)
    total_words = len(words)

    if total_words == 0:
        return 0.0, 0, 0

    # Count biased occurrences
    biased_matches = list(pattern.finditer(text))
    biased_count = len(biased_matches)

    bias_percentage = (biased_count / total_words) * 100

    return round(bias_percentage, 2), biased_count, total_words