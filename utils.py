from nltk.corpus import cmudict
import re


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
        if phoneme in arpabet_to_letters_dict:
            word += arpabet_to_letters_dict[phoneme]
    return word

def generate_arpabet_transcription(word):
    arpabet_transcription = []
    
    # Define phonetic rules for non-words
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
    
    # Split the word into phonetic segments based on known rules
    segments = []
    current_segment = ''
    i = 0
    while i < len(word):
        for j in range(len(word), i, -1):
            if word[i:j] in phonetic_rules:
                segments.append(phonetic_rules[word[i:j]])
                i = j
                break
        else:  # No rule matched, treat current character as unknown sound
            if word[i] != '\n':
              segments.append([word[i].upper()])
            i += 1
    
    # Flatten the segments into a single list
    arpabet_transcription = [phoneme for segment in segments for phoneme in segment]
    
    return arpabet_transcription