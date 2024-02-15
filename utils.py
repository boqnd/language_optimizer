import re
from graph import Graph
from syllabipy.sonoripy import SonoriPy

def remove_special_characters(text):
    pattern = r'[^a-zA-Z0-9\s]'
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text

def generate_word_partial_phonetic(arpabet):
    arpabet_to_letters_dict = {
        'AA': 'a',
        'AE': 'a',
        'AH': 'uh',
        'AO': 'aw',
        'AW': 'ow',
        'AY': 'ai',
        'B': 'b',
        'CH': 'ch',
        'D': 'd',
        'DH': 'th',
        'EH': 'e',
        'ER': 'er',
        'EY': 'ay',
        'F': 'f',
        'G': 'g',
        'HH': 'h',
        'IH': 'i',
        'IY': 'ee',
        'JH': 'j',
        'K': 'k',
        'L': 'l',
        'M': 'm',
        'N': 'n',
        'NG': 'ng',
        'OW': 'o',
        'OY': 'oy',
        'P': 'p',
        'R': 'r',
        'S': 's',
        'SH': 'sh',
        'T': 't',
        'TH': 'th',
        'UH': 'oo',
        'UW': 'oo',
        'V': 'v',
        'W': 'w',
        'Y': 'y',
        'Z': 'z',
        'ZH': 'zh'
    }

    word = ''
    for phoneme in arpabet:
        phoneme = phoneme[0:-1]
        if phoneme in arpabet_to_letters_dict:
            word += arpabet_to_letters_dict[phoneme]
    return word

def generate_arpabet_transcription(word):
    arpabet_transcription = []

    phonetic_rules = {
        'fl': ['F', 'L'],      # 'fl' is pronounced as F and L
        'bl': ['B', 'L'],      # 'bl' is pronounced as B and L
        'br': ['B', 'R'],      # 'br' is pronounced as B and R
        'dr': ['D', 'R'],      # 'dr' is pronounced as D and R
        'kl': ['K', 'L'],      # 'kl' is pronounced as K and L
        'kr': ['K', 'R'],      # 'kr' is pronounced as K and R
        'gl': ['G', 'L'],      # 'gl' is pronounced as G and L
        'gr': ['G', 'R'],      # 'gr' is pronounced as G and R
        'pl': ['P', 'L'],      # 'pl' is pronounced as P and L
        'pr': ['P', 'R'],      # 'pr' is pronounced as P and R
        'sl': ['S', 'L'],      # 'sl' is pronounced as S and L
        'sr': ['S', 'R'],      # 'sr' is pronounced as S and R
        'tr': ['T', 'R'],      # 'tr' is pronounced as T and R
        'tw': ['T', 'W'],      # 'tw' is pronounced as T and W
        'dw': ['D', 'W'],      # 'dw' is pronounced as D and W
        'kw': ['K', 'W'],      # 'kw' is pronounced as K and W
        'sk': ['S', 'K'],      # 'sk' is pronounced as S and K
        'sw': ['S', 'W'],      # 'sw' is pronounced as S and W
        'squ': ['S', 'K', 'W'],# 'squ' is pronounced as S, K, and W
        'bl': ['B', 'L'],      # 'bl' is pronounced as B and L
        'br': ['B', 'R'],      # 'br' is pronounced as B and R
        'str': ['S', 'T', 'R'],# 'str' is pronounced as S, T, and R
        'thr': ['TH', 'R'],    # 'thr' is pronounced as TH and R
        'fr': ['F', 'R'],      # 'fr' is pronounced as F and R
        'fl': ['F', 'L'],      # 'fl' is pronounced as F and L
        'cr': ['K', 'R'],      # 'cr' is pronounced as K and R
        'cl': ['K', 'L'],      # 'cl' is pronounced as K and L
        'gl': ['G', 'L'],      # 'gl' is pronounced as G and L
        'pr': ['P', 'R'],      # 'pr' is pronounced as P and R
        'pl': ['P', 'L'],      # 'pl' is pronounced as P and L
        'bl': ['B', 'L'],      # 'bl' is pronounced as B and L
        'sl': ['S', 'L'],      # 'sl' is pronounced as S and L
        'gr': ['G', 'R'],      # 'gr' is pronounced as G and R
        'kl': ['K', 'L'],      # 'kl' is pronounced as K and L
        'gl': ['G', 'L'],      # 'gl' is pronounced as G and L
        'kl': ['K', 'L'],      # 'kl' is pronounced as K and L
        'fl': ['F', 'L'],      # 'fl' is pronounced as F and L
        'vl': ['V', 'L'],      # 'vl' is pronounced as V and L
        'sl': ['S', 'L'],      # 'sl' is pronounced as S and L
        'sl': ['S', 'L'],      # 'sl' is pronounced as S and L
        'th': ['TH'],          # 'th' is pronounced as TH
        'ch': ['CH'],          # 'ch' is pronounced as CH
        'sh': ['SH'],          # 'sh' is pronounced as SH
        'ng': ['NG'],          # 'ng' is pronounced as NG
        'ai': ['AY'],          # 'ai' is pronounced as AY
        'ei': ['EY'],          # 'ei' is pronounced as EY
        'oi': ['OY'],          # 'oi' is pronounced as OY
        'au': ['AO'],          # 'au' is pronounced as AO
        'ou': ['AW'],          # 'ou' is pronounced as AW
        'zh': ['ZH'],          # 'zh' is pronounced as ZH
        'a': ['AH'],           # 'a' is pronounced as AH
        'e': ['EH'],           # 'e' is pronounced as EH
        'i': ['IH'],           # 'i' is pronounced as IH
        'o': ['OW'],           # 'o' is pronounced as OW
        'u': ['AH', 'W'],      # 'u' is pronounced as AH and W
        'v': ['V'],            # 'v' is pronounced as V
        'z': ['Z'],            # 'z' is pronounced as Z
        'm': ['M'],            # 'm' is pronounced as M
        'n': ['N'],            # 'n' is pronounced as N
        'k': ['K'],            # 'k' is pronounced as K
        'p': ['P'],            # 'p' is pronounced as P
        'b': ['B'],            # 'b' is pronounced as B
        't': ['T'],            # 't' is pronounced as T
        'd': ['D'],            # 'd' is pronounced as D
        'f': ['F'],            # 'f' is pronounced as F
        'g': ['G'],            # 'g' is pronounced as G
        's': ['S'],            # 's' is pronounced as S
        'r': ['R'],            # 'r' is pronounced as R
        'y': ['Y'],            # 'y' is pronounced as Y
        'w': ['W'],            # 'w' is pronounced as W
        'hh': ['HH'],          # 'hh' is pronounced as HH
        'l': ['L'],            # 'l' is pronounced as L
        'j': ['JH'],           # 'j' is pronounced as JH
    }

    segments = []
    i = 0
    while i < len(word):
        for j in range(len(word), i, -1):
            if word[i:j] in phonetic_rules:
                segments.append(phonetic_rules[word[i:j]])
                i = j
                break
        else:
            i += 1

        arpabet_transcription = [phoneme for segment in segments for phoneme in segment]

    return arpabet_transcription

def create_phonem_graph(input_text):
  cleaned_text = remove_special_characters(input_text)
  syllables = []

  words = cleaned_text.split(' ')
  for word in words:
    word_syllables = SonoriPy(word)
    for syllable in word_syllables:
      syllables.append(syllable)

  graph = Graph()
  start = '__start__'
  end = '__end__'

  for s in syllables:
    transcription = generate_arpabet_transcription(s)
    if transcription:
      has_onset = False
      has_nucleous = False
      has_coda = False
      for i in range(len(transcription)):
        print(transcription, transcription[i])
        if is_vowel(transcription[i]):
          has_onset = True

        if has_onset and not is_vowel(transcription[i]):
          has_nucleous = True

        current = transcription[i]
        if not has_onset:
          current = mark_onset(current)
        elif not has_nucleous:
          current = mark_nucleus(current)
        else:
          current = mark_coda(current)
        print(current)
        if i == 0:
          graph.add_edge(start, current)
        if i <= len(transcription)-2:
          next = transcription[i+1]
          if not has_onset:
            if is_vowel(next):
              next = mark_nucleus(next)
            else:
              next = mark_onset(next)
          elif not has_nucleous:
            if is_vowel(next):
              next = mark_nucleus(next)
            else:
              next = mark_coda(next)
          else:
            next = mark_coda(next)
          print(next)

          graph.add_edge(current, next)
        if i == len(transcription)-1:
          graph.add_edge(current, end)

  return graph

def is_vowel(phonem):
  vowels = ['W','Y','UH','UW','OW','OY','IH','IY','EH','ER','EY','AA','AE','AH','AO','AW','AY']
  return phonem in vowels

def mark_onset(phonem):
    return phonem+'+'

def mark_nucleus(phonem):
    return phonem+'.'

def mark_coda(phonem):
    return phonem+'-'

def generate_words(text, n):
    graph = create_phonem_graph(text)
    print(graph)

    paths = graph.find_best_paths(n)
    transcriptions = [[phonem[0] for phonem in path[0][1:-1]] for path in paths]

    return [generate_word_partial_phonetic(t) for t in transcriptions]