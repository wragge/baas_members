#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

BAAS_MEMBERS = 'texts/baas_members_1914.txt'
BAAS_MEMBERS_AUS = 'texts/baas_members_1914_{}.txt'


def find_women_members():

    with open(BAAS_MEMBERS, 'r') as members:
        total = 0
        women = {'total': 0, 'Miss': 0, 'Mrs': 0, 'Lady': 0}
        titles = ['Mrs', 'Miss', 'Lady', 'Dr']
        patterns = []
        for title in titles:
            patterns.append([title, re.compile('[,\.]{1} ' + title + '[, \.]{1}')])
        for line in members:
            if re.search(r'^\d{4}\. ', line):
                total += 1
                for title, pattern in patterns:
                    if pattern.search(line):
                        if title == 'Dr':
                            print line
                        else:
                            women['total'] += 1
                            women[title] += 1
                        break
        print total
        print women


def find_women_australian_members():
    total = 0
    locations = ['melbourne', 'sydney', 'adelaide', 'brisbane']
    women = {'total': 0, 'Miss': 0, 'Mrs': 0, 'Lady': 0}
    titles = ['Mrs', 'Miss', 'Lady', 'Dr']
    patterns = []
    for title in titles:
        patterns.append([title, re.compile('[,\.]{1} ' + title + '[, \.]{1}')])
    for location in locations:
        print location.upper()
        local_total = 0
        local_women = {'total': 0, 'Miss': 0, 'Mrs': 0, 'Lady': 0}
        with open(BAAS_MEMBERS_AUS.format(location), 'r') as members:
            for line in members:
                # This is still going to miss some names such as Von Mueller
                # Probably easier just to clean the data!
                if re.search(r'^[A-Z§♦*^i.]{1}[^,.]+[,.\s]{1} ', line):
                    total += 1
                    local_total += 1
                    for title, pattern in patterns:
                        if pattern.search(line):
                            if title == 'Dr':
                                print line
                            else:
                                women['total'] += 1
                                women[title] += 1
                                local_women['total'] += 1
                                local_women[title] += 1
                                break
            print local_total
            print local_women
    print total
    print women

