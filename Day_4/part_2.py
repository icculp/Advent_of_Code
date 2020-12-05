#!/usr/bin/env python3
"""
    Day 3 of Advent of Code 2020
"""
import re


def part_two():
    """ Validate passport data """
    with open('input') as input:
        inp = input.readlines()

    passports = []
    new = []
    for i in range(len(inp)):
        if inp[i][0] == '\n':
            passports.append(new)
            new = []
            continue
        else:
            new.append(inp[i])
    for i in range(len(passports)):
        passports[i] = [passports[i][j].strip('\n').split(' ') for j in range(len(passports[i]))]
        helper = []
        for k in range(len(passports[i])):
            print(passports[i])
            print(passports[i][k])
            helper = [passports[i][k][l].split(':') for l in range(len(passports[i][k]))]
            passports[i][k] = helper
            helper = []
    p = dict()
    print()
    print()
    for i in range(len(passports)):
        for j in range(len(passports[i])):
            for li in passports[i]:
                for lis in li:
                    '''print(lis)'''
                    if p.get(i) is None:
                        p.update({i: {lis[0]: lis[1]}})
                    else:
                        p[i].update({lis[0]: lis[1]})
    print(p)
    count = 0
    for key in p.keys():
        if len(p[key].keys()) == 8:
            pass
        elif len(p[key].keys()) == 7 and 'cid' not in p[key].keys():
            pass
        else:
            continue

        byr = eval(p[key]['byr'])
        if byr < 1920 or byr > 2002 or len(str(byr)) != 4:
            continue
        else:
            '''print(byr)'''
            pass
        iyr = eval(p[key]['iyr'])
        if iyr < 2010 or iyr > 2020 or len(str(iyr)) != 4:
            '''print(iyr)'''
            continue
        else:
            '''print(iyr)'''
            pass
        eyr = eval(p[key]['eyr'])
        if eyr < 2020 or eyr > 2030 or len(str(eyr)) != 4:
            '''print(eyr)'''
            continue
        else:
            '''print(eyr)'''
            pass
        hgt = p[key]['hgt']
        if re.match('\d+(in|cm)$', hgt) is not None:
            '''print(hgt)'''
            if hgt.strip('0123456789') == 'cm':
                '''print(hgt)'''
                if eval(hgt.strip('cm')) < 150 or eval(hgt.strip('cm')) > 193:
                    '''print(hgt)'''
                    continue
                else:
                    '''print(hgt)'''
                    pass
            if hgt.strip('0123456789') == 'in':
                '''print(hgt)'''
                if eval(hgt.strip('in')) < 59 or eval(hgt.strip('in')) > 76:
                    '''print(hgt)'''
                    continue
                else:
                    '''print(hgt)'''
                    pass
        else:
            '''print("[{}]".format(hgt))'''
            pass
        hcl = p[key]['hcl']
        if re.match('^#[a-f0-9]{6}$', hcl) is not None:
            '''print(hcl)'''
            pass
        else:
            '''print(hcl)'''
            continue
        ecl = p[key]['ecl']
        if re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', ecl):
            '''print(ecl)'''
            pass
        else:
            '''print(ecl)'''
            continue
        pid = p[key]['pid']
        if re.match('^\d{9}$', pid):
            '''print(pid)'''
            pass
        else:
            print(pid)
            continue

        count += 1

    return count


if __name__ == '__main__':
    count = part_two()
    print("\n\nCount: [{}]".format(count))
