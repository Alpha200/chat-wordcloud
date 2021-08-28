import csv
from typing import List

from common import map_word, get_stopwords, generate_wordcloud


def generate_threema_wordcloud(file):
    data = csv.DictReader(file, delimiter=',', quotechar='"')

    messages: List[str] = [message['body'] for message in data if message['type'] == 'TEXT']
    num_messages = len(messages)

    words = [map_word(word.lower()) for message in messages for word in message.split()]
    words = [word for word in words if len(word) > 1]

    num_words = len(words)
    num_words_per_message = num_words / num_messages

    stopwords = get_stopwords()

    filtered_words = [word for word in words if word not in stopwords]
    num_filtered_words = len(filtered_words)

    print(f"Loaded {num_messages} and {num_words} words ({num_words_per_message:.02f} words per message)")
    print(f"Removed {num_words - num_filtered_words} stop words")

    text = ' '.join(filtered_words)
    generate_wordcloud(text)
