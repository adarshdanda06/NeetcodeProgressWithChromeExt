# **Find the Duplicate Number**

You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

Example 1:

```
Input: nums = [1,2,3,2,2]

Output: 2

```

Example 2:

```
Input: nums = [1,2,3,4,4]

Output: 4

```

Follow-up: Can you solve the problem without modifying the array nums and using O(1)O(1)O(1) extra space?

Constraints:

- 1 <= n <= 10000
- nums.length == n + 1
- 1 <= nums[i] <= n



### Recommended Time & Space Complexity

You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.


### Hint 1

A naive approach would be to use a hash set, which takes O(1) time to detect duplicates. Although this solution is acceptable, it requires O(n) extra space. Can you think of a better solution that avoids using extra space? Consider that the elements in the given array nums are within the range 1 to len(nums).


### Hint 2

We can use the given input array itself as a hash set without creating a new one. This can be achieved by marking the positions (0-indexed) corresponding to the elements that have already been encountered. Can you implement this?


### Hint 3

We iterate through the array using index i. For each element, we use its absolute value to find the corresponding index and mark that position as negative: nums[abs(nums[i]) - 1] *= -1. Taking absolute value ensures we work with the original value even if it’s already negated. How can you detect duplicates?


### Hint 4

For example, in the array [2, 1, 2, 3], where 2 is repeated, we mark the index corresponding to each element as negative. If we encounter a number whose corresponding position is already negative, it means the number is a duplicate, and we return it.