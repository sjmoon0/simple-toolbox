'''
Program to generate all the possible seven letter words that can
be rolled in the game of Word Yahtzee. 
Steven Moon
'''
import string
from datetime import datetime

die_one = ["O","W","U","M","P","Y"]
die_two = ["B","E","X","S","A","Y"]
die_three = ["R","Q","J","N","A","D"]
die_four = ["A","C","E","F","I","Z"]
die_five = ["P","I","M","E","G","_"]
die_six = ["T","E","S","L","A","H"]
die_seven = ["V","U","N","C","O","K"]
dice=[die_one,die_two,die_three,die_four,die_five,die_six,die_seven]

def build_word_trie():
    trie_root = ("",{})
    seven_letter_word_file = open("seven_letter_words.txt")
    for word in seven_letter_word_file:
        word = word.strip()
        curr_letter_p = 0
        curr_node = trie_root
        while curr_letter_p < len(word):
            if word[curr_letter_p] not in curr_node[1].keys():
                new_node = (word[curr_letter_p],{})
                curr_node[1][word[curr_letter_p]] = new_node
                curr_node = new_node
            else:
                curr_node = curr_node[1][word[curr_letter_p]]
            curr_letter_p = curr_letter_p + 1
    return trie_root

def print_to_file(out_file,word_list):
    word_list.sort()
    for word in word_list:
        print(word,file=out_file)
    out_file.close()

def check_prefix(prefix):
    prefix = prefix.lower()
    curr_node = word_trie
    ctr = 0
    while ctr < len(prefix): 
        try:
            curr_node[1][prefix[ctr]]
        except KeyError:
            break
        curr_node = curr_node[1][prefix[ctr]]
        ctr = ctr + 1
    return ctr == len(prefix)

def perm(prefix_dice,rest):
    order = prefix_dice + rest
    prefix=""
    for a in range(6):
        prefix=""
        prefix = prefix + order[0][a]
        # vv Die 1 Blank vv
        if order[0][a] == "_":
            for char in string.ascii_uppercase:
                prefix_copy = prefix[:]
                prefix_copy = prefix_copy.replace("_",char)
                if not check_prefix(prefix_copy):
                    prefix_copy = prefix_copy[:-1]
                    continue
                for b in range(6):
                    prefix_copy = prefix_copy + order[1][b]
                    if not check_prefix(prefix_copy):
                        prefix_copy = prefix_copy[:-1]
                        continue
                    for c in range(6):
                        prefix_copy = prefix_copy + order[2][c]
                        if not check_prefix(prefix_copy):
                            prefix_copy = prefix_copy[:-1]
                            continue
                        for d in range(6):
                            prefix_copy = prefix_copy + order[3][d]
                            if not check_prefix(prefix_copy):
                                prefix_copy = prefix_copy[:-1]
                                continue
                            for e in range(6):
                                prefix_copy = prefix_copy + order[4][e]
                                if not check_prefix(prefix_copy):
                                    prefix_copy = prefix_copy[:-1]
                                    continue
                                for f in range(6):
                                    prefix_copy = prefix_copy + order[5][f]
                                    if not check_prefix(prefix_copy):
                                        prefix_copy = prefix_copy[:-1]
                                        continue
                                    for g in range(6):
                                        prefix_copy = prefix_copy + order[6][g]
                                        if not check_prefix(prefix_copy):
                                            prefix_copy = prefix_copy[:-1]
                                            continue
                                        else:
                                            if prefix_copy not in word_list:
                                                word_list.append(prefix_copy)
                                                #print("Found word blank 1: ",prefix_copy)
                                                #print(prefix_copy,file=possible_words)
                                    prefix_copy = prefix_copy[:-1]
                                prefix_copy = prefix_copy[:-1]
                            prefix_copy = prefix_copy[:-1]
                        prefix_copy = prefix_copy[:-1]
                    prefix_copy = prefix_copy[:-1]
                prefix_copy = prefix_copy[:-1]
        # ^^ Die 1 Blank ^^
        if not check_prefix(prefix):
            prefix = prefix[:-1]
            continue
        for b in range(6):
            prefix = prefix + order[1][b]
            # vv Die 2 Blank vv
            if order[1][b] == "_":
                for char in string.ascii_uppercase:
                    prefix_copy = prefix[:]
                    prefix_copy = prefix_copy.replace("_",char)
                    for c in range(6):
                        prefix_copy = prefix_copy + order[2][c]
                        if not check_prefix(prefix_copy):
                            prefix_copy = prefix_copy[:-1]
                            continue
                        for d in range(6):
                            prefix_copy = prefix_copy + order[3][d]
                            if not check_prefix(prefix_copy):
                                prefix_copy = prefix_copy[:-1]
                                continue
                            for e in range(6):
                                prefix_copy = prefix_copy + order[4][e]
                                if not check_prefix(prefix_copy):
                                    prefix_copy = prefix_copy[:-1]
                                    continue
                                for f in range(6):
                                    prefix_copy = prefix_copy + order[5][f]
                                    if not check_prefix(prefix_copy):
                                        prefix_copy = prefix_copy[:-1]
                                        continue
                                    for g in range(6):
                                        prefix_copy = prefix_copy + order[6][g]
                                        if not check_prefix(prefix_copy):
                                            prefix_copy = prefix_copy[:-1]
                                            continue
                                        else:
                                            if prefix_copy not in word_list:
                                                word_list.append(prefix_copy)
                                                #print("Found word blank 2: ",prefix_copy)
                                                #print(prefix_copy,file=possible_words)
                                    prefix_copy = prefix_copy[:-1]
                                prefix_copy = prefix_copy[:-1]
                            prefix_copy = prefix_copy[:-1]
                        prefix_copy = prefix_copy[:-1]
                    prefix_copy = prefix_copy[:-1]
            # ^^ Die 2 Blank ^^
            if not check_prefix(prefix):
                prefix = prefix[:-1]
                continue
            for c in range(6):
                prefix = prefix + order[2][c]
                # vv Die 3 Blank vv
                if order[2][c] == "_":
                    for char in string.ascii_uppercase:
                        prefix_copy = prefix[:]
                        prefix_copy = prefix_copy.replace("_",char)
                        for d in range(6):
                            prefix_copy = prefix_copy + order[3][d]
                            if not check_prefix(prefix_copy):
                                prefix_copy = prefix_copy[:-1]
                                continue
                            for e in range(6):
                                prefix_copy = prefix_copy + order[4][e]
                                if not check_prefix(prefix_copy):
                                    prefix_copy = prefix_copy[:-1]
                                    continue
                                for f in range(6):
                                    prefix_copy = prefix_copy + order[5][f]
                                    if not check_prefix(prefix_copy):
                                        prefix_copy = prefix_copy[:-1]
                                        continue
                                    for g in range(6):
                                        prefix_copy = prefix_copy + order[6][g]
                                        if not check_prefix(prefix_copy):
                                            prefix_copy = prefix_copy[:-1]
                                            continue
                                        else:
                                            if prefix_copy not in word_list:
                                                word_list.append(prefix_copy)
                                                #print("Found word blank 3: ",prefix_copy)
                                                #print(prefix_copy,file=possible_words)
                                    prefix_copy = prefix_copy[:-1]
                                prefix_copy = prefix_copy[:-1]
                            prefix_copy = prefix_copy[:-1]
                        prefix_copy = prefix_copy[:-1]
                # ^^ Die 3 Blank ^^
                if not check_prefix(prefix):
                    prefix = prefix[:-1]
                    continue
                for d in range(6):
                    prefix = prefix + order[3][d]
                    # vv Die 4 Blank vv
                    if order[3][d] == "_":
                        for char in string.ascii_uppercase:
                            prefix_copy = prefix[:]
                            prefix_copy = prefix_copy.replace("_",char)
                            for e in range(6):
                                prefix_copy = prefix_copy + order[4][e]
                                if not check_prefix(prefix_copy):
                                    prefix_copy = prefix_copy[:-1]
                                    continue
                                for f in range(6):
                                    prefix_copy = prefix_copy + order[5][f]
                                    if not check_prefix(prefix_copy):
                                        prefix_copy = prefix_copy[:-1]
                                        continue
                                    for g in range(6):
                                        prefix_copy = prefix_copy + order[6][g]
                                        if not check_prefix(prefix_copy):
                                            prefix_copy = prefix_copy[:-1]
                                            continue
                                        else:
                                            if prefix_copy not in word_list:
                                                word_list.append(prefix_copy)
                                                #print("Found word blank 4: ",prefix_copy)
                                                #print(prefix_copy,file=possible_words)
                                    prefix_copy = prefix_copy[:-1]
                                prefix_copy = prefix_copy[:-1]
                            prefix_copy = prefix_copy[:-1]
                    # ^^ Die 4 Blank ^^
                    if not check_prefix(prefix):
                        prefix = prefix[:-1]
                        continue
                    for e in range(6):
                        prefix = prefix + order[4][e]
                        # vv Die 5 Blank vv
                        if order[4][e] == "_":
                            for char in string.ascii_uppercase:
                                prefix_copy = prefix[:]
                                prefix_copy = prefix_copy.replace("_",char)
                                for f in range(6):
                                    prefix_copy = prefix_copy + order[5][f]
                                    if not check_prefix(prefix_copy):
                                        prefix_copy = prefix_copy[:-1]
                                        continue
                                    for g in range(6):
                                        prefix_copy = prefix_copy + order[6][g]
                                        if not check_prefix(prefix_copy):
                                            prefix_copy = prefix_copy[:-1]
                                            continue
                                        else:
                                            if prefix_copy not in word_list:
                                                word_list.append(prefix_copy)
                                                #print("Found word blank 5: ",prefix_copy)
                                                #print(prefix_copy,file=possible_words)
                                    prefix_copy = prefix_copy[:-1]
                                prefix_copy = prefix_copy[:-1]
                        # ^^ Die 5 Blank ^^
                        if not check_prefix(prefix):
                            prefix = prefix[:-1]
                            continue
                        for f in range(6):
                            prefix = prefix + order[5][f]
                            # vv Die 6 Blank vv
                            if order[5][f] == "_":
                                for char in string.ascii_uppercase:
                                    prefix_copy = prefix[:]
                                    prefix_copy = prefix_copy.replace("_",char)
                                    for g in range(6):
                                        prefix_copy = prefix_copy + order[6][g]
                                        if not check_prefix(prefix_copy):
                                            prefix_copy = prefix_copy[:-1]
                                            continue
                                        else:
                                            if prefix_copy not in word_list:
                                                word_list.append(prefix_copy)
                                                #print("Found word blank 6: ",prefix_copy)
                                                #print(prefix_copy,file=possible_words)
                                    prefix_copy = prefix_copy[:-1]
                            # ^^ Die 6 Blank ^^
                            if not check_prefix(prefix):
                                prefix = prefix[:-1]
                                continue
                            for g in range(6):
                                prefix = prefix + order[6][g]
                                # vv Die 7 Blank vv
                                if order[6][g] == "_":
                                    for char in string.ascii_uppercase:
                                        prefix_copy = prefix[:]
                                        #print(prefix_copy)
                                        prefix_copy = prefix_copy.replace("_",char)
                                        if not check_prefix(prefix_copy):
                                            continue
                                        else:
                                            if prefix_copy not in word_list and len(prefix_copy)==7:
                                                word_list.append(prefix_copy)
                                                #print("Found word blank 7: ",prefix_copy)
                                                #print(prefix_copy,file=possible_words)
                                # ^^ Die 7 Blank ^^
                                if not check_prefix(prefix):
                                    prefix = prefix[:-1]
                                    continue
                                else:
                                    if prefix not in word_list and len(prefix)==7:
                                        word_list.append(prefix)
                                        #print(prefix,file=possible_words)
                                prefix=prefix[:-1]
                            prefix=prefix[:-1]
                        prefix=prefix[:-1]
                    prefix=prefix[:-1]
                prefix=prefix[:-1]
            prefix=prefix[:-1]
        prefix=prefix[:-1]
    prefix=prefix[:-1]
    for i in range(len(rest)):
        perm(prefix_dice+[rest[i]], rest[:i] + rest[i+1:])

print("Building trie")
word_list = []
word_trie = build_word_trie()
print("Searching for words...")
perm([],dice)
possible_words = open("found_words.txt","w")
print_to_file(possible_words,word_list)
print("Writing words to found_words.txt")
possible_words.close()
