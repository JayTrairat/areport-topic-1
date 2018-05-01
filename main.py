#!/usr/bin/env python

import yaml

def main():
    with open('assets/important_words/pos_1.yml', 'r', encoding='utf8') as source:
        PRE = yaml.load(source)

    print(PRE)


if __name__ == '__main__':
    main()
