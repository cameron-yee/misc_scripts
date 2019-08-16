#!/usr/local/bin/python3
import sys
import re

def formatEntry(matches):
    return '\t{{\n\t\t"state": "{}",\n\t\t"abb": "{}"\n\t}},\n'.format(matches[0], matches[1])


def getMatches(string):
    matches = re.findall('([A-Za-z]+\s{0,1}[A-Za-z]+)', string)

    if len(matches) != 2:
        raise ValueError('String does not match "<STATE NAME> - <STATE ABRV>"')

    return matches


def setEntries(lines):
    entries = []

    for line in lines:
        matches = getMatches(line)
        entry = formatEntry(matches)
        entries.append(entry)

    return entries


def readFile(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        return lines


def writeEntriesToFile(file_path):
    lines = readFile(file_path)

    entries = setEntries(lines)

    with open(file_path, 'w+') as f:
        f.write('[\n')
        f.writelines(entries)
        f.write(']')


if __name__ == '__main__':
    writeEntriesToFile(sys.argv[1])
