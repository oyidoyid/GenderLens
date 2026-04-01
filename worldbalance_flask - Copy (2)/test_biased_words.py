# test_biased_words.py

from biased_words import highlight_text, calculate_bias_percentage

def main():
    sample_text = "The chairman and the cameraman talked to the mailman about manpower."

    print("Original text:")
    print(sample_text)
    print("-" * 40)

    # Test highlight_text
    highlighted, suggestions = highlight_text(sample_text)
    print("Highlighted text (HTML):")
    print(highlighted)
    print("-" * 40)

    print("Suggestions (biased term -> replacements):")
    for word, replacements in suggestions:
        print(f"{word} -> {list(replacements)}")
    print("-" * 40)

    # Test calculate_bias_percentage
    bias_pct, biased_count, total_words = calculate_bias_percentage(sample_text)
    print("Bias analysis:")
    print(f"  Bias percentage: {bias_pct}%")
    print(f"  Biased words:    {biased_count}")
    print(f"  Total words:     {total_words}")

if __name__ == "__main__":
    main()