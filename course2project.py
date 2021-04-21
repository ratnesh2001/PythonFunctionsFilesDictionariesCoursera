def strip_punctuation(word):
    for i in punctuation_chars:
        word = word.replace(i, '')
    return word

def get_pos(line):
    count = 0
    for word in line.split():
        if strip_punctuation(word).lower() in positive_words:
            count += 1
    return count

def get_neg(line):
    count = 0
    for word in line.split():
        if strip_punctuation(word).lower() in negative_words:
            count += 1
    return count

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

f = open('project_twitter_data.csv', 'r')
ansfile = open('resulting_data.csv', 'w')
ansfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
i = 0
for line in f.readlines():
    if(i == 0):
        i = 1
        continue
    temp = line.split(',')
    retweet_count = temp[1]
    reply_count = temp[2].strip('\n')
    pos_score = get_pos(line)
    neg_score = get_neg(line)
    net_score = pos_score - neg_score
    ansfile.write('{},{},{},{},{}\n'.format(retweet_count, reply_count, pos_score, neg_score, net_score))
    