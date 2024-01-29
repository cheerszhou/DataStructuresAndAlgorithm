# 左右指针的常用算法

# 1.二分查找
def binary_search(nums: list[int], target: int) -> int:
    # 一左一右两指针相向而行
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# 2.两数之和
# 力扣第 167 题「两数之和 II]
#
# 给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列 ，
# 请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是
# numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
#
# 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
#
# 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
#
# 你所设计的解决方案必须只使用常量级的额外空间。

def two_sum(nums: list[int], target: int) -> list[int]:
    # 一左一右两指针相向而行
    left, right = 0, len(nums) - 1
    while left < right:
        a_sum = nums[left] + nums[right]
        if a_sum == target:
            # 题目要求索引从1开始
            return [left + 1, right + 1]
        elif a_sum < target:
            # 让sum大一点
            left += 1
        else:
            # 让sum小一点
            right -= 1

    return [-1, -1]


# 3.反转数组
# 力扣第 344 题「反转字符串」就是类似的需求，让你反转一个 char[] 类型的字符数组，我们直接看代码吧：

# 判断参数是否为字符串
def is_string(value) -> bool:
    return isinstance(value, list)


# def reverse_string(s:list[str]):
def reverse_string(a_string):
    assert is_string(a_string), '输入的实参必须为字符串'
    # 一左一右两指针相向而行
    left = 0
    right = len(a_string) - 1
    while left < right:
        # 交换a_string[left]和a_string[right]
        temp = a_string[left]
        a_string[left] = a_string[
            right]  # 报错: (<class 'TypeError'>, TypeError("'str' object does not support item assignment")
        a_string[right] = temp
        left += 1
        right -= 1


def reverseString(s):
    left, right = 0, len(s) - 1

    while left < right:
        # 交换左右两侧的字符
        s[left], s[right] = s[right], s[left]

        # 移动指针
        left += 1
        right -= 1


# 4.回文串判断
# 首先明确一下，回文串就是正着读和反着读都一样的字符串。
#
# 比如说字符串 aba 和 abba 都是回文串，因为它们对称，反过来还是和本身一样；反之，字符串 abac 就不是回文串。
def isPalindrome(s: str) -> bool:
    # 一左一右两指针相向而行
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# 力扣第 5 题「最长回文子串」
# 给你一个字符串 s，找到 s 中最长的回文子串。
#
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

# 找回文串的难点在于，回文串的的长度可能是奇数也可能是偶数，解决该问题的核心是从中心向两端扩散的双指针技巧。
# 
# 如果回文串的长度为奇数，则它有一个中心字符；如果回文串的长度为偶数，则可以认为它有两个中心字符。所以我们可以先实现这样一个函数：
def palindrome(s: str, left: int, right: int) -> str:
    # 在 s 中寻找以 s[l] 和 s[r] 为中心的最长回文串

    # 防止索引越界
    while left >= 0 and right < len(s) and s[left] == s[right]:
        # 双指针, 向两边展开
        left -= 1
        right += 1
    # 返回范围为l..r的最长回文串
    return s[left + 1: right]


# 这样，如果输入相同的 l 和 r，就相当于寻找长度为奇数的回文串，如果输入相邻的 l 和 r，则相当于寻找长度为偶数的回文串。
#
# 那么回到最长回文串的问题，解法的大致思路就是：
#
#
# for 0 <= i < len(s):
#     找到以 s[i] 为中心的回文串
#     找到以 s[i] 和 s[i+1] 为中心的回文串
#     更新答案
# 翻译成代码，就可以解决最长回文子串这个问题：

def longest_palindrome(s: str) -> str:
    res = ""
    for i in range(len(s)):
        # 以 s[i] 为中心的最长回文字串
        s1 = palindrome(s, i, i)
        # 以 s[i] 和 s[i+1] 为中心的最长回文字串
        s2 = palindrome(s, i, i + 1)
        # res = longest(res, s1, s2)
        res = res if len(res) > len(s1) else s1
        res = res if len(res) > len(s2) else s2

    return res


if __name__ == '__main__':
    numbers = [1, 7, 11, 15]
    target = 12
    print(two_sum(numbers, target))
    numbers = [2, 3, 4]
    target = 6
    print(two_sum(numbers, target))

    string = list('ahahbbbb')
    reverse_string(string)
    # reverseString(string)
    original_string = "Hello, World!"
    reversed_string = ''.join(reversed(original_string))
    print(reversed_string)
    print("".join(string))

    a_str = 'bb'
    # print(a_str.join(['1','3','4']))
    print(a_str + (' 是回文串' if isPalindrome(a_str) else ' 不是回文串'))
    # print('{} 是回文串'.format(a_str) if isPalindrome(a_str) else '{} 不是回文串'.format(a_str))
    print(f'{a_str} 是回文串' if isPalindrome(a_str) else f'{a_str} 不是回文串')

    a_str = 'cbbd'
    print(f'{a_str} 的最长回文字串为 {longest_palindrome(a_str)}')