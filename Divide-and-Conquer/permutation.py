def find_permutation_cofficient(n, r):
    p = 1
    for i in range(r):
        p = p * (n - i)
    return p


def permutation_cofficient_dp(n, r):
    dp = [1 for i in range(r + 1)]

    for i in range(1, r + 1):
        dp[i] = dp[i - 1] * (n - i + 1)
    return dp[r]


def permutation_cofficient_recursion(n, r, l=0):
    if l >= r:
        return 1
    return n*permutation_cofficient_recursion(n-1, r, l+1)


def toString(List):
    return ''.join(List)


def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack

def is_safe(_list_obj, l, i):
    if l != 0 and _list_obj[l - 1] == 'A' and _list_obj[i] == 'B':
        return False
    if l != 0 and _list_obj[l - 1] == 'B' and _list_obj[i] == 'A':
        return False

    return True

def permutation(_str, l, r):
    if l==r:
        print(''.join(_str))
        return
    for i in range(l, r):
        if is_safe(_str, l, i):
            _str[i], _str[l] = _str[l], _str[i]
            permutation(_str, l+1, r)
            _str[i], _str[l] = _str[l], _str[i]


def permute1(s, answer):
    if (len(s) == 0):
        print(answer, end="  ")
        return

    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute1(rest, answer + ch)

def compare_list(l1, l2):
    for num1, num2 in zip(l1, l2):
        if num1 < num2:
            print('No')
            return False
    print('Yes')
    return True
def check_permutation_break(str1, str2):
    x1 = sorted([ord(i) for i in str1])
    x2 = sorted([ord(i) for i in str2])
    x1_sum = sum(x1)
    x2_sum = sum(x2)
    if x1_sum > x2_sum:
        compare_list(x1, x2)
    elif x1_sum < x2_sum:
        compare_list(x2, x1)
    else:
        print('No')

def adjacent_swap(_list):
    _list.insert(0, 0)
    swap_count = 0
    for i in range(1, len(_list)-1):
        if _list[i] == i:
            _list[i], _list[i+1] = _list[i+1], _list[i]
            swap_count += 1
    if _list[len(_list)-1] == len(_list)-1:
        _list[len(_list)-1], _list[len(_list)-2] = _list[len(_list)-2], _list[len(_list)-1]
        swap_count += 1
    print(swap_count)

adjacent_swap( [5, 2, 2, 9, 5, 8, 7] )
    # xya -> axy
    # abc -> aby
# check_permutation_break('abe', 'acd')
string = "ABC"
answer = ""
n = len(string)
a = list(string)
# permutation(list(string), 0, len(string))
# permute(a, 0, n)
# permute1(string, answer)

# print(permutation_cofficient_recursion(10, 1))
# print(find_permutation_cofficient(10, 1))
# print(permutation_cofficient_dp(10, 1))
