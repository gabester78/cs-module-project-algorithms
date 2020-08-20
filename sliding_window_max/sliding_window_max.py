'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):

    # grab length of nums array
    n = len(nums)

    # var to grab group's max number
    max = 0

    # hold max numbers appended from last loop from windows
    arr = []

    # loop through nums array arguement from nums[0] - nums[2]
    for i in range(n - k + 1):

        # updates max to current window being viewed
        max = nums[i]

        # loop through the window to find the highest value
        for j in range(1, k):

            # compares index of i from original loop to nested loop
            # value of j
            if nums[i + j] > max:

                # if value is greater, add it to max var
                max = nums[i + j]

        # append value to arr var
        arr.append(max)

    return arr


if __name__ == '__main__':
    # Use queue instead of nested loops
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
