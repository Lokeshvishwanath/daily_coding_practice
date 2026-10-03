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