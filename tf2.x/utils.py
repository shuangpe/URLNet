from tensorflow.keras.utils import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

def get_word_vocab(urls, max_length_words, min_word_freq=0):
    tokenizer = Tokenizer(lower=False)
    tokenizer.fit_on_texts(urls)

    if min_word_freq > 0:
        wcounts = list(filter(lambda x: x[1] > min_word_freq, tokenizer.word_counts.items()))
        wcounts.sort(key=lambda x: x[1], reverse=True)
        tokenizer.word_index = dict(zip(wcounts.keys(), list(range(1, len(wcounts) + 1))))
        tokenizer.index_word = {c: w for w, c in tokenizer.word_index.items()}

    sequences = tokenizer.texts_to_sequences(urls)
    padded = pad_sequences(sequences, max_length_words, padding='post', truncating='post')
    vocab_dict = tokenizer.word_index
    reverse_dict = dict(zip(vocab_dict.values(), vocab_dict.keys()))
    return padded, reverse_dict