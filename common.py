import re

from matplotlib import pyplot as plt
from wordcloud import WordCloud


def get_stopwords():
    with open('stopwords/german_stopwords_full.txt', 'r') as stopwords:
        return [line.strip().lower() for line in stopwords.readlines() if not line.startswith(';')]


def generate_wordcloud(text: str):
    generator = WordCloud()
    generator.width = 1920
    generator.height = 1080

    wordcloud = generator.generate(text)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def map_word(word: str):
    return re.sub(r'[^\w]', '', word)
