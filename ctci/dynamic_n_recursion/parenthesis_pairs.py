"""Implement an algorithm to print all valid (e.g.,properly opened and closed) combinations of n-pairs of parentheses.

EXAMPLE: Input: 3. Output: ((())), (()()), ()(()), ()()()"""

def make_parenthesis(n):
    if n == 1:
        return set(['()'])
    parens = set()
    for paren in make_parenthesis(n - 1):
        paren_left = '()' + paren
        parens.add(paren_left)
        paren_right = paren + '()'
        parens.add(paren_right)
        paren_inside = '(' + paren + ')'
        parens.add(paren_inside)
    return parens

num = int(input())
result = make_parenthesis(num)
print(make_parenthesis(num))
print(len(result))
