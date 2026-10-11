# day57_valid_anagram.py

class Solution:

    def is_anagram(self, s, t):

        if len(s) != len(t):
            return False

        count = {}

        # Count characters in s
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Subtract characters in t
        for char in t:

            if char not in count:
                return False

            count[char] -= 1

            if count[char] < 0:
                return False

        return True


def main():

    s = "anagram"
    t = "nagaram"

    solution = Solution()

    result = solution.is_anagram(s, t)

    print("String 1:", s)
    print("String 2:", t)
    print("Are Anagrams?", result)


if __name__ == "__main__":
    main()




# day55_group_anagrams.py

class Solution:

    def group_anagrams(self, strs):

        groups = {}

        for word in strs:

            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())


def main():

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    solution = Solution()

    result = solution.group_anagrams(strs)

    print("Input:", strs)
    print("Grouped Anagrams:")

    for group in result:
        print(group)


if __name__ == "__main__":
    main()