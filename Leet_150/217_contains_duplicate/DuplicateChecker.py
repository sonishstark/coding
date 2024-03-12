class DuplicateChecker(object):
    def containsDuplicate(nums):
        nums.sort()  # Sort the array
    # Check adjacent elements for duplicates
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True  # Duplicate found
        return False  # No duplicate found

def main():
    # Getting number of elements from user
    n = int(input("Enter the number of elements: "))
    # Storing the array elements from user
    nums = []
    print("INPUT:")
    for _ in range(n):
        nums.append(int(input()))
    
    has_duplicate = containsDuplicate(nums)

    # Print the result
    if has_duplicate:
        print("OUTPUT: true")
    else:
        print("OUTPUT: false")

if __name__ == "__main__":
    main()