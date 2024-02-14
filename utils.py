from nltk.corpus import cmudict
import re
import random
import heapq

pronouncing_dict = cmudict.dict()

def get_transcription(word):
    transcriptions = pronouncing_dict.get(word.lower())
    if transcriptions:
        return transcriptions[0]
    else:
        return None

def remove_special_characters(text):
    pattern = r'[^a-zA-Z0-9\s]'
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text

def dijkstra_shortest_path(graph, start, end):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph.nodes}
    # Distance from start to start is 0
    distances[start] = 0
    # Initialize a priority queue with start node and its distance
    pq = [(0, start)]
    # Initialize dictionary to store the previous node in the shortest path
    previous = {}

    # Dijkstra's algorithm
    while pq:
        current_distance, current_node = pq.pop(0)

        # Stop if the current node is the end node
        if current_node == end:
            break

        # Visit each neighbor of the current node
        for neighbor, weight in graph.nodes[current_node].neighbors.items():
            distance = current_distance + weight
            # If new distance is shorter than the recorded distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Update the priority queue with the new distance
                pq.append((distance, neighbor))
                # Update the previous node in the shortest path
                previous[neighbor] = current_node
                # Sort the priority queue based on distances
                pq.sort(key=lambda x: -x[0])

    # Construct list of values in each node on the way
    path = []
    current = end
    while current in previous:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()
    return path

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


  # syllables = SonoriPy(word)
  # print("Syllables:", syllables)