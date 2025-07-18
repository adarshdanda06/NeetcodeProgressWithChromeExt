# **Daily Temperatures**

You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

```
Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]

```

Example 2:

```
Input: temperatures = [22,21,20]

Output: [0,0,0]

```

Constraints:

- 1 <= temperatures.length <= 1000.
- 1 <= temperatures[i] <= 100



### Recommended Time & Space Complexity

You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.


### Hint 1

A brute force solution would involve iterating through the array with index i and checking how far is the next greater element to the right of i. This would be an O(n^2) solution. Can you think of a better way?


### Hint 2

Can you consider a reverse approach? For example, in [2, 1, 1, 3], the next greater element for the numbers [2, 1, 1] is 3. Instead of checking for each element individually, can you think of a way where, by standing at the element 3, you compute the result for the elements [2, 1, 1]?  Maybe there's a data structure that is useful here.


### Hint 3

We can use a stack to maintain indices in a monotonically decreasing order, popping indices where the values are smaller than the current element. This helps us find the result by using the difference between indices while considering the values at those indices. Can you see how the stack is useful?


### Hint 4

In the array [2, 1, 1, 3], we don't perform any pop operations while processing [2, 1, 1] because these elements are already in decreasing order. However, when we reach 3, we pop elements from the stack until the top element of the stack is no longer less than the current element. For each popped element, we compute the difference between the indices and store it in the position corresponding to the popped element.