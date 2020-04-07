import re
from collections import Counter, defaultdict


def build_vocab(corpus):
    '''
    Initialize vocabulary, add special char </w> to each word
    ''' 
    chars = [" ".join(word) + " </w>" for word in corpus.split()]
    
    # Count frequency of chars in corpus
    vocab = Counter(chars)

    return vocab


def get_pair_counts(vocab):
    '''
    Get counts of the pairs of all consecutive symbols
    '''

    pair_counts = defaultdict(int)
    for word, frequency in vocab.items():
        chars = word.split()

        for i in range(len(chars) - 1):
            pair_counts[chars[i], chars[i + 1]] += frequency

    return pair_counts


def merge_most_frequent(pair: tuple, v_in: dict) -> dict:
    '''
    Merge all occurrences of the most frequent pair
    '''
    
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    
    for word in v_in:
        # replace most frequent pair in all vocabulary
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]

    return v_out

corpus = '''
Smoke the first 48 hours, grind 22 and sleep two hours
Put 24s on the new Audi, white on white like baby powder
Drop ya' boo off at Fulton County
Might count it up and then re-count it
Double cups like Tunechi, yeah
Bust it down with these goonies, yeah
Give no effs yeah, we don't give no effs, yeah
Go fill my cup yeah, yo go fill my cup, yeah
You heard that the slums made me, I'm cool with the Konvicts
The coupe look like Akon, eff all that bum shit
'''

vocab = build_vocab(corpus)

num_merges = 50
for i in range(num_merges):
    pair_counts = get_pair_counts(vocab)

    if not pair_counts:
        break

    most_frequent = max(pair_counts, key=pair_counts.get)
    vocab = merge_most_frequent(most_frequent, vocab)

    
print(vocab)