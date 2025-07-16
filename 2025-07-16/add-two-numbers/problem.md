# **Add Two Numbers**

You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:

```
Input: l1 = [1,2,3], l2 = [4,5,6]

Output: [5,7,9]

Explanation: 321 + 654 = 975.

```

Example 2:

```
Input: l1 = [9], l2 = [9]

Output: [8,1]

```

Constraints:

- 1 <= l1.length, l2.length <= 100.
- 0 <= Node.val <= 9



### Recommended Time & Space Complexity

You should aim for a solution with O(m + n) time and O(1) space, where m is the length of list l1 and n is the length of list l2.


### Hint 1

Try to visualize the addition of two numbers. We know that the addition of two numbers is done by starting at the one's digit. We add the numbers by going through digit by digit. We track the extra value as a carry because the addition of two digits can result in a number with two digits. The carry is then added to the next digits, and so on. How do you implement this in case of linked lists?


### Hint 2

We track the extra value, carry, here as well. We iterate through the lists l1 and l2 until both lists reach null. We add the values of both nodes as well as the carry. If either of the nodes is null, we add 0 in its place and continue the process while tracking the carry simultaneously. Once we complete the process, if we are left with any carry, we add an extra node with that carry value and return the head of the result list.