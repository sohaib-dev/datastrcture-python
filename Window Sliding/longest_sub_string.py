
# str_1 = 'abcadaabcbb'
#
# l,r = 0, 1
# max_str_len = 0
# distinct_char = set()
# for i in range(len(str_1)):
#     while str_1[i] in distinct_char:
#         distinct_char.remove(str_1[l])
#         l += 1
#     distinct_char.add(str_1[i])
#     max_str_len = max(max_str_len, i-l+1)
#
# print(max_str_len)
#
# lst = [7 ,2 ,5 ,1 ,6 ,4]
# l, r = 0, 1
# max_profit = 0
#
# for i in range(len(lst)-1):
#     max_profit = max(max_profit, lst[r]-lst[l])
#     if lst[l] > lst[r]:
#         l = r
#     r += 1
#
# print(max_profit)
#
# t = 'ABC'
# s = 'ADOBECODEBANC'
#
# t_hash = dict()
# s_hash = dict()
# for val in t:
#     t_hash[val] = 1 + t_hash.get(val, 0)
# l, r = 0, 0
# max_str = ''
#
# for i in range(len(s)):
#     if len(t_hash) == len(s_hash):
#         for val in t_hash:
#         # if
#         max_str = s[l:r]
#         while s[l] in t_hash:
#
#     if s[r] in t_hash:
#         t_hash[s[r]] = 1 + t_hash.get(s[r], 0)
#     r += 1
#
#
# print(max_str)


# O(n) solution for finding
# maximum sum of a subarray of size k


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if s == t:
        return s
    if len(s) < len(t):
        return ''

    l, r = 0, len(t)
    enumerate
    min_substr = ''
    is_substr = False
    substr = ''
    while r < len(s)+1:
        for i in t:
            if i in s[l:r]:
                is_substr = True
            else:
                is_substr = False
                break
        if is_substr:
            if min_substr == '':
                min_substr = s[l:r]
            substr = min(min_substr, s[l:r+1])
            l += 1
            min_substr = min_substr[1:]
            for j in min_substr:
                if j not in t:
                    # min_substr = min_substr[1:]
                    l += 1
                else:
                    break
            for i in t:
                if i in s[l:r]:
                    is_substr = True
                else:
                    is_substr = False
                    break
            if is_substr:
                if min_substr == '':
                    min_substr = s[l:r]
                substr = min(min_substr, s[l:r + 1])

        r += 1
    print(substr)
    return substr

# print(minWindow("bdab", "ab"))
l1 = {'a': 1,'b':2,'c':3}
for i, j in enumerate(l1,5):
    print(i, " => ", l1[j])
