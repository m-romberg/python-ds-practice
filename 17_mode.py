def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    # O(n^2)
    # Writing out the counter would be O(n)
    # Also there is a built in function
    counter = {num: nums.count(num) for num in nums}
    max_key = max(counter, key=counter.get)
    return max_key
