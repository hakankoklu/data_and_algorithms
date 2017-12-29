def remove_element(ll, el):
    return [l for l in ll if l != el]

def spell(word, dice):
    if word == '':
        return True
    if not dice:
        return False
    matches = [d for d in dice if word[0] in d]
    print('Letter: ' + word[0])
    print('matches: ' + str(matches))
    print('Next: ' + word[1:])
    # import pdb
    # pdb.set_trace()
    return any([spell(word[1:], remove_element(dice, d)) for d in matches])

word = 'hakan'
dice = ['skjdhfi', 'apfgr', 'regfbfvn', 'lkjsdhfn', 'peelff', 'an']

print(spell(word, dice))