#!/usr/bin/env python

import yaml

def main():
    with open('assets/important_words/pos_1.yml', 'r', encoding='utf8') as source:
        PRE = yaml.load(source)
    with open('assets/important_words/pos_2.yml', 'r', encoding='utf8') as source:
        MIDPRE = yaml.load(source)
    with open('assets/important_words/pos_3.yml', 'r', encoding='utf8') as source:
        MIDPOST = yaml.load(source)
    with open('assets/important_words/pos_4.yml', 'r', encoding='utf8') as source:
        POST = yaml.load(source)
    type = "number"
    naming_list = [
        pre + midpre + midpost + post
        for pre in PRE['all']
        for midpre in MIDPRE['all']
        for midpost in MIDPOST['all']
        for post in POST[type]
    ]

    with open('assets/result.txt', 'w', encoding='utf8') as outp:
        outp.write('\n'.join(naming_list))

if __name__ == '__main__':
    main()
