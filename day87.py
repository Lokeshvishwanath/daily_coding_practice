# day26_first_last_position.py

class Solution:

    def first_position(self, nums, target):

        left = 0
        right = len(nums) - 1
        answer = -1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                answer = mid
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return answer

    def last_position(self, nums, target):

        left = 0
        right = len(nums) - 1
        answer = -1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                answer = mid
                left = mid + 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return answer

    def search_range(self, nums, target):

        first = self.first_position(nums, target)
        last = self.last_position(nums, target)

        return [first, last]


def main():

    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    solution = Solution()

    result = solution.search_range(nums, target)

    print("Array :", nums)
    print("Target:", target)
    print("Answer:", result)


if __name__ == "__main__":
    main()

#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"enter the number";
    cin>>n;
    for(int i=0;i<n;i++){
        for(int j=n;j>0;j--){
            cout<<"* ";
        }
        cout<<endl;
    }
    
}