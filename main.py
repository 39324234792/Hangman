import time
import random
word_bank = ['able', 'about', 'acid', 'across', 'act', 'addition', 'adjustment', 'advertisement', 'after', 'again', 'agreement', 'air', 'all', 'almost', 'among', 'amount', 'and', 'angle', 'angry', 'animal', 'answer', 'ant', 'any', 'apple', 'arch', 'argument', 'arm', 'army', 'art', 'as', 'at', 'attack', 'attempt', 'attention', 'attraction', 'authority', 'awake', 'baby', 'back', 'bad', 'bag', 'ball', 'band', 'base', 'basin', 'basket', 'bath', 'be', 'because', 'bed', 'bee', 'before', 'belief', 'bell', 'bent', 'berry', 'bird', 'birth', 'bit', 'bite', 'bitter', 'black', 'blade', 'blood', 'blow', 'blue', 'board', 'boat', 'body', 'boiling', 'bone', 'book', 'boot', 'bottle', 'box', 'boy', 'brain', 'brake', 'branch', 'brass', 'bread', 'breath', 'brick', 'bridge', 'bright', 'broken', 'brown', 'brush', 'bucket', 'bulb', 'burn', 'burst', 'but', 'butter', 'button', 'by', 'cake', 'camera', 'canvas', 'card', 'care', 'carriage', 'cart', 'cat', 'cause', 'chain', 'chalk', 'chance', 'change', 'cheap', 'cheese', 'chest', 'chief', 'chin', 'church', 'circle', 'clean', 'clear', 'clock', 'cloth', 'cloud', 'coal', 'coat', 'cold', 'collar', 'colour', 'comb', 'come', 'comfort', 'committee', 'common', 'comparison', 'competition', 'complete', 'complex', 'condition', 'conscious', 'control', 'cook', 'copper', 'copy', 'cord', 'cork', 'cotton', 'cough', 'country', 'cover', 'cow', 'crack', 'credit', 'crime', 'cruel', 'crush', 'cry', 'cup', 'current', 'curtain', 'curve', 'cushion', 'cut', 'damage', 'danger', 'dark', 'day', 'dead', 'dear', 'death', 'debt', 'deep', 'degree', 'delicate', 'dependent', 'design', 'desire', 'detail', 'development', 'different', 'digestion', 'direction', 'dirty', 'discussion', 'disgust', 'distance', 'distribution', 'do', 'dog', 'door', 'doubt', 'down', 'drain', 'drawer', 'dress', 'drink', 'driving', 'drop', 'dry', 'dust', 'ear', 'early', 'earth', 'east', 'edge', 'effect', 'egg', 'electric', 'end', 'engine', 'enough', 'equal', 'error', 'even', 'event', 'ever', 'every', 'exchange', 'existence', 'expansion', 'experience', 'expert', 'eye', 'face', 'fact', 'fall', 'false', 'family', 'far', 'farm', 'fat', 'father', 'fear', 'feeble', 'feeling', 'female', 'fiction', 'field', 'fight', 'finger', 'fire', 'first', 'fish', 'fixed', 'flag', 'flame', 'flat', 'flight', 'floor', 'flower', 'fly', 'fold', 'food', 'foot', 'for', 'force', 'fork', 'form', 'fowl', 'frame', 'free', 'friend', 'from', 'front', 'fruit', 'full', 'future', 'garden', 'general', 'get', 'girl', 'give', 'glass', 'glove', 'go', 'goat', 'gold', 'good', 'grain', 'grass', 'great', 'green', 'grey', 'grip', 'group', 'growth', 'guide', 'gun', 'hair', 'hammer', 'hand', 'happy', 'hard', 'hat', 'hate', 'have', 'he', 'head', 'healthy', 'hearing', 'heart', 'heat', 'help', 'here', 'high', 'history', 'hole', 'hollow', 'hook', 'hope', 'horn', 'horse', 'hospital', 'hour', 'house', 'how', 'humour', 'ice', 'idea', 'if', 'ill', 'impulse', 'in', 'industry', 'ink', 'insect', 'insurance', 'interest', 'invention', 'iron', 'island', 'jelly', 'jewel', 'join', 'judge', 'jump', 'keep', 'kettle', 'key', 'kick', 'kind', 'kiss', 'knee', 'knife', 'knot', 'knowledge', 'land', 'language', 'last', 'late', 'laugh', 'law', 'lead', 'leaf', 'leather', 'left', 'leg', 'let', 'letter', 'level', 'library', 'lift', 'light', 'like', 'limit', 'line', 'linen', 'lip', 'liquid', 'list', 'little', 'living', 'lock', 'long', 'look', 'loose', 'loss', 'loud', 'love', 'low', 'make', 'male', 'man', 'map', 'mark', 'market', 'mass', 'match', 'material', 'may', 'meal', 'meat', 'meeting', 'memory', 'metal', 'middle', 'military', 'milk', 'mind', 'mine', 'minute', 'mist', 'mixed', 'money', 'monkey', 'month', 'moon', 'mother', 'motion', 'mouth', 'move', 'much', 'muscle', 'music', 'nail', 'name', 'narrow', 'nation', 'natural', 'near', 'neck', 'need', 'needle', 'nerve', 'net', 'new', 'news', 'night', 'no', 'noise', 'normal', 'north', 'nose', 'not', 'note', 'now', 'number', 'nut', 'observation', 'of', 'off', 'offer', 'office', 'oil', 'old', 'on', 'only', 'open', 'opinion', 'or', 'orange', 'order', 'ornament', 'other', 'out', 'oven', 'over', 'owner', 'page', 'pain', 'paint', 'paper', 'parcel', 'part', 'past', 'paste', 'peace', 'pen', 'pencil', 'person', 'picture', 'pig', 'pin', 'pipe', 'place', 'plane', 'plant', 'plate', 'play', 'please', 'plough', 'pocket', 'point', 'poison', 'polish', 'political', 'poor', 'porter', 'possible', 'pot', 'potato', 'powder', 'power', 'present', 'price', 'print', 'prison', 'private', 'probable', 'process', 'produce', 'profit', 'prose', 'protest', 'public', 'pull', 'pump', 'punishment', 'purpose', 'push', 'put', 'quality', 'question', 'quick', 'quiet', 'quite', 'rail', 'rain', 'range', 'rat', 'rate', 'ray', 'reading', 'ready', 'reason', 'receipt', 'record', 'red', 'regret', 'regular', 'relation', 'religion', 'representative', 'respect', 'rest', 'reward', 'rhythm', 'rice', 'right', 'ring', 'river', 'road', 'rod', 'roll', 'roof', 'room', 'root', 'rough', 'round', 'rub', 'rule', 'run', 'sad', 'safe', 'sail', 'salt', 'same', 'sand', 'say', 'scale', 'school', 'scissors', 'screw', 'sea', 'seat', 'second', 'secret', 'see', 'seed', 'seem', 'self', 'send', 'sense', 'serious', 'servant', 'sex', 'shade', 'shake', 'shame', 'sharp', 'sheep', 'shelf', 'ship', 'shirt', 'shock', 'shoe', 'short', 'shut', 'side', 'sign', 'silk', 'silver', 'simple', 'sister', 'size', 'skin', 'skirt', 'sky', 'sleep', 'slip', 'slope', 'slow', 'small', 'smash', 'smell', 'smile', 'smoke', 'smooth', 'snake', 'sneeze', 'snow', 'so', 'soap', 'sock', 'soft', 'solid', 'some', 'son', 'song', 'sort', 'sound', 'soup', 'south', 'space', 'spade', 'sponge', 'spoon', 'spring', 'square', 'stage', 'stamp', 'star', 'start', 'station', 'steam', 'steel', 'stem', 'step', 'stick', 'sticky', 'stiff', 'still', 'stitch', 'stocking', 'stomach', 'stone', 'stop', 'store', 'story', 'straight', 'strange', 'street', 'strong', 'substance', 'such', 'sudden', 'sugar', 'suggestion', 'summer', 'sun', 'surprise', 'sweet', 'swim', 'system', 'table', 'tail', 'take', 'talk', 'tall', 'taste', 'tax', 'tendency', 'test', 'than', 'that', 'the', 'then', 'theory', 'there', 'thick', 'thin', 'thing', 'this', 'though', 'thread', 'throat', 'thumb', 'ticket', 'tight', 'till', 'time', 'tin', 'tired', 'to', 'toe', 'tomorrow', 'tongue', 'tooth', 'top', 'touch', 'town', 'trade', 'train', 'transport', 'tray', 'tree', 'trick', 'trousers', 'true', 'turn', 'twist', 'under', 'unit', 'up', 'use', 'value', 'verse', 'very', 'vessel', 'view', 'voice', 'walk', 'wall', 'war', 'warm', 'wash', 'waste', 'watch', 'water', 'wave', 'wax', 'way', 'week', 'weight', 'well', 'west', 'wet', 'wheel', 'when', 'where', 'while', 'whip', 'white', 'who', 'why', 'wide', 'will', 'wind', 'window', 'wine', 'wing', 'winter', 'wire', 'wise', 'with', 'woman', 'wood', 'wool', 'word', 'work', 'worm', 'wound', 'wrong', 'year', 'yellow', 'yes', 'you', 'young']


def lost():
    print('          ')
    print('   _____  ')
    print('   |   0  ')
    print('   |  /|\\')
    print('   |  / \\    ')
    print('   |    ')
    print('___|___   ')
    print('You Lose')


def head():
    print('          ')
    print('   _____  ')
    print('   |   0  ')
    print('   |  ')
    print('   |      ')
    print('   |    ')
    print('___|___   ')


def head_body():
    print('          ')
    print('   _____  ')
    print('   |   0  ')
    print('   |   |')
    print('   |      ')
    print('   |    ')
    print('___|___   ')


def one_arm():
    print('          ')
    print('   _____  ')
    print('   |   0  ')
    print('   |  /|')
    print('   |      ')
    print('   |    ')
    print('___|___   ')


def two_arms():
    print('          ')
    print('   _____  ')
    print('   |   0  ')
    print('   |  /|\\')
    print('   |      ')
    print('   |    ')
    print('___|___   ')


def one_leg():
    print('          ')
    print('   _____  ')
    print('   |   0  ')
    print('   |  /|\\')
    print('   |  /     ')
    print('   |    ')
    print('___|___   ')


def listtostring(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


phrase = random.choice(word_bank)
phrase_list = []
phrase_full = []
lives = [1, 1, 1, 1, 1, 1]
for letter in phrase:
    phrase_full.append(letter)
    if letter == ' ':
        phrase_list.append(' ')
    else:
        phrase_list.append('_')

print(listtostring(phrase_list))
losses = 0
last_one = False
for life_left in lives:
    if phrase_list == phrase_full:
        print('You Win')
        quit()
    else:
        Guess = input('guess a letter: ')
        check = False
        bom = 0
        for letter in phrase_full:
            if letter == phrase_full[len(phrase_full) - 1]:

                last_one = True
            else:
                last_one = False
            if Guess == letter:
                check = True
                lives.append(1)
                print('correct')
                after = []
                before = []
                if bom > 0 & bom < len(phrase_list):
                    after = phrase_list[bom + 1:]
                    before = phrase_list[:bom]
                if bom == 0:
                    after = phrase_list[bom + 1:]
                if bom == len(phrase_list):
                    before = phrase_list[:bom - 1]
                phrase_list = []
                for item in before:
                    phrase_list.append(item)
                phrase_list.append(Guess)
                for item1 in after:
                    phrase_list.append(item1)
                print(listtostring(phrase_list))

            else:
                if check == False and last_one == True:
                    print('incorrect')
                    losses = losses + 1
                    if losses == 1:
                        head()
                    if losses == 2:
                        head_body()
                    if losses == 3:
                        one_arm()
                    if losses == 4:
                        two_arms()
                    if losses == 5:
                        one_leg()
                    if losses == 6:
                        lost()
                        time.sleep(2)
                        print(phrase)
                else:
                    pass

            bom = bom + 1
