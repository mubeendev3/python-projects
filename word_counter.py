def count_text_statistics(text: str) -> dict:
    """
    Count words, characters, and sentences in a given text.
    """
    characters = len(text)
    words = len(text.split())
    sentences = sum(text.count(symbol) for symbol in ".!?")

    return {
        "characters": characters,
        "words": words,
        "sentences": sentences
    }


def main():
    print("📝 Word Counter Application")
    text = input("Enter your text: ")

    stats = count_text_statistics(text)

    print("\n--- Text Statistics ---")
    print(f"Characters: {stats['characters']}")
    print(f"Words: {stats['words']}")
    print(f"Sentences: {stats['sentences']}")


if __name__ == "__main__":
    main()
