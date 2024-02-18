from graph import Graph, start_node, end_node
from syllabipy.sonoripy import SonoriPy
from utils import remove_special_characters, generate_arpabet_transcription, is_vowel, mark_onset, mark_nucleus, mark_coda, generate_word_partial_phonetic

class Translator:
    def __init__(self, text):
        self.text = text

    def create_phonem_graph(self):
        graph = Graph()
        cleaned_text = remove_special_characters(self.text)
        syllables = []

        words = cleaned_text.split(' ')
        for word in words:
            word_syllables = SonoriPy(word)
            for syllable in word_syllables:
                syllables.append(syllable)

        for s in syllables:
            transcription = generate_arpabet_transcription(s)
            if transcription:
                has_onset = False
                has_nucleus = False
                for i in range(len(transcription)):
                    if is_vowel(transcription[i]):
                        has_onset = True

                    if has_onset and not is_vowel(transcription[i]):
                        has_nucleus = True

                    current = transcription[i]
                    if not has_onset:
                        current = mark_onset(current)
                    elif not has_nucleus:
                        current = mark_nucleus(current)
                    else:
                        current = mark_coda(current)

                    if i == 0:
                        graph.add_edge(start_node, current)
                    if i <= len(transcription)-2:
                        next = transcription[i+1]
                        if not has_onset:
                            if is_vowel(next):
                                next = mark_nucleus(next)
                            else:
                                next = mark_onset(next)
                        elif not has_nucleus:
                            if is_vowel(next):
                                next = mark_nucleus(next)
                            else:
                                next = mark_coda(next)
                        else:
                            next = mark_coda(next)

                        graph.add_edge(current, next)
                    if i == len(transcription)-1:
                        graph.add_edge(current, end_node)
        return graph

    def assign_translations(self, new_words):
        word_freq = self.get_word_freq()
        sorted_words = sorted(word_freq, key=word_freq.get, reverse=False)
        translations = {}

        for i, word in enumerate(sorted_words):
            if i < len(new_words):
                translations[word] = new_words[i]

        return translations

    def get_word_freq(self):
        word_freq = {}

        words = remove_special_characters(self.text).split()
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        return word_freq

    def generate_words(self, n):
        graph = self.create_phonem_graph()
        paths = graph.find_best_paths(n)
        transcriptions = [[phonem[0] for phonem in path[0][1:-1]] for path in paths]

        return [generate_word_partial_phonetic(t) for t in transcriptions]

    def translate(self):
        new_words = self.generate_words(len(self.get_word_freq()))

        translations = self.assign_translations(new_words)
        translated_text = ""

        words = remove_special_characters(self.text).split()
        for word in words:
            translated_word = translations.get(word)
            translated_text += translated_word + " "

        return (translated_text.strip(), translations)
