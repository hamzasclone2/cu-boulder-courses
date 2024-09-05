#!/usr/bin/env python
# coding: utf-8

# # Final Exam Instructions
# 
# Instructions are provided as part of a reading along with this final exam. Please ensure that you have read them carefully before attempting this exam.

# # Problem 1 (15 points)
# 
# You are given a list of $n$ rods of various lengths as a list `[1[0], l[1],...,l[n-1]]`.
# 
# Your job is to attach the rods in some order to make a single rod of length $\texttt{l[0]} + \texttt{l[1]} + \cdots + \texttt{l[n-1]}$.
# 
# However, if you attach two rods of length $\ell, m$, you have to pay a cost $\ell + m$.
# 
# --- 
# 
# ### Example
# ~~~
# l = [1, 5, 2, 4, 3, 2]
# ~~~
# Here is one sequence of attachments:
#  1. Attach rod 1, 5: new rod of length 6 is formed and cost so far = 6. Lengths: `[6, 2, 4, 3, 2]`
#  2. Attach rod 2, 2: new rod of length 4 is formed and cost so far = 6 + 4 = 10, Lengths: `[6, 4, 4, 3]`.
#  3. Attach rod 4, 3: new rod of length 7 is formed and cost so far = 10 + 7 = 17, Lengths: `[6,4, 7]`.
#  4. Attach rod 6, 7: new rod of length 13 is formed and cost so far = 17 + 13 = 30, Lengths = `[13, 4]`.
#  5. Attach rod 13, 4: new rod of length 17 is formed and cost so far = 30 + 17 = 47. Lengths = `[17]`.
#  
# Total cost of attachment is 47 if we did it in the manner above.
# 
# Here is another way to do the same:
#  1. Attach rods 1, 2: cost so far = 3, Lengths = `[3, 5, 4, 3, 2]`.
#  2. Attach rods 2, 3: cost so far = 3+5 = 8, Lengths = `[5, 5, 4, 3]`
#  3. Attach rods: 3, 4: cost so far=  8 + 7 = 15, Lenghts = `[5, 5, 7]`
#  4. Attach rods: 5, 5: cost so far = 15 + 10 = 25, lengths = `[10, 7]`
#  5. Attach rods: 10, 17: cost so far = 25 + 17 = 42, lengths = `[17]`.
#  Total Cost = 42.
#  
# The second approach is more efficient in terms of cost than the first.
#  
# ---
# 
# 
# 
# Given a list of rod lengths write an algorithm to attach them all into a single rod while minimizing the total cost paid. Your function should simply return the total cost. There is no need to compute the sequence of joins to be made.
# 
# First write your pseudocode below and figure out the best way to implement it so that you can find the best cost in $\Theta(n \log(n))$ steps given $n$ rods. The pseudocode is for your own benefit: we will not be grading your answer.
# 
# __Hint:__ Think about the similarities between this problem and Huffman codes that you studied.

# YOUR ANSWER HERE

# Implement the function `findOptimalJoiningCost` below. Given a list of rod lengths, it should return the optimal cost. You can use pythons inbuilt heap routines. https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

# In[96]:


import heapq

def findOptimalJoiningCost(lengths):
    # your code here
    heapq.heapify(lengths)
    cost = 0
    while(len(lengths) > 1):
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)
        new = first + second
        cost += new
        heapq.heappush(lengths, new)
    return cost


# In[97]:


print('-- Test 1 --')
l1 = [1, 5, 2, 4, 3, 2]
c1 = findOptimalJoiningCost(l1)
print(c1)
assert c1 == 42

print('-- Test 2 --')
l2 = [4, 7, 6, 3, 4, 2 ]
c2 = findOptimalJoiningCost(l2)
print(c2)
assert c2 == 65

print('-- Test 3 --')
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c3 = findOptimalJoiningCost(l3)
print(c3)
assert c3 == 173

print('-- Test 4 --')
l4 = list(range(10000))
c4 = findOptimalJoiningCost(l4)
print(c4)
assert c4 == 652216969

print('-- Test 5 --')
l5 = list(range(100000))
c5 = findOptimalJoiningCost(l5)
print(c5)
assert c5 == 81780799249

print('All tests passed: 15 points')


# ## Problem 2 (15 points)
# 
# In this problem, you are given a list of numbers `l: [l[0], ..., l[n-1]]`. Your goal is to partition this into two  lists `l1, l2` such that each element `l[i]` belongs to exactly one of `l1, l2` and the difference between the sums of the two lists is minimized:
#  $$\min\ | \text{sum}(\texttt{l1}) - \text{sum}(\texttt{l2}) | $$
#  
#  where $\text{sum}(\texttt{l})$ for a list $l$ denotes the sum of the elements in a list.
# 
# 
# ### Example
# 
# ~~~
# l = [ 1, 5, 7, 8, 4, 6, 15]
# ~~~
# 
# Partition it as 
# ~~~ 
# l1 = [1, 7, 15], l2 = [5, 8, 4, 6] 
# ~~~
# 
# Note that in this case `sum(l1) = sum(l2) = 23`. Thus, we have minimized the absolute difference to 0, which is the best possible.
# 
# 
# ### Dynamic Programming 
# $$\newcommand\minAbsDiff{\textsf{minAbsDiff}}$$
# Let  $\minAbsDiff(i, s_1, s_2)$ denote the minimum difference achievable when considering the sublist `[l[i],...,l[n-1]]` with $s_1$ being the sum of elements already committed to list `l1` and $s_2$ being the sum of elements already committed to `l2`.
# 
# 
# $$\minAbsDiff(i, s_1, s_2) = \begin{cases}
# ??? & i \geq n \ \leftarrow\ \text{sublist is empty}\\
# \min(\minAbsDiff(i+1, ??? , s_2) , \minAbsDiff(i+1, s_1,??? )) & i \leq n-1 \ \leftarrow\ \text{assign l[i] to l1 or l2}\\
# \end{cases}$$
# 
# Implement the function `computeBestPartition(l)` that takes in a list `l` and returns the partition as a tuple of lists `(l1, l2)`.
# 
# 
# * Assume that all elements of the list `l` are positive whole numbers.
# * Complete and memoize the recurrence above.
# * Recover the solution 
# 

# In[104]:


def computeBestPartition(l):
    n = len(l)
    assert n >= 1
    assert all(elt >= 1 and elt== int(elt) for elt in l)
    # your code here
    return minAbsDiff(0, [], [], l)
    
def minAbsDiff(i, l1, l2, l):
    n = len(l)
        
    if(i >= n):
        return (l1, l2)
    else:
        temp1 = l1.copy()
        temp1.append(l[i])
        temp2 = l2.copy()
        temp2.append(l[i])
        
        (a, b) = minAbsDiff(i+1, temp1, l2, l)
        (x, y) = minAbsDiff(i+1, l1, temp2, l)
        
        dif1 = abs(sum(a) - sum(b))
        dif2 = abs(sum(x) - sum(y))
        
        if(dif1 <= dif2):
            return (a, b)
        else:
            return (x, y)        


# In[105]:


def checkIfPartition(l, l1, l2):
    assert all((elt in l1 and elt not in l2) or (elt in l2 and elt not in l1) for elt in l)
    assert all(elt in l for elt in l1)
    assert all(elt in l for elt in l2)

print('-- Test 1 --')
l = [ 1, 5, 7, 8, 4, 6, 15]
(l1, l2) = computeBestPartition(l)
print(l1, l2, sum(l1), sum(l2))
assert sum(l1) == sum(l2)
checkIfPartition(l, l1, l2)
print('passed.')
print('-- Test 2 --')
l = [1, 10, 14, 16, 19, 22, 29 ,41,  15, 18]
(l1, l2) = computeBestPartition(l)
print(l1, l2, sum(l1), sum(l2))
assert abs(sum(l1) - sum(l2)) <= 1
checkIfPartition(l, l1, l2)
print('passed.')
print('-- Test 3 --')
l = [5, 16, 21, 13, 15, 18, 19, 14, 12, 2, 4]
(l1, l2) = computeBestPartition(l)
print(l1, l2, sum(l1), sum(l2))
assert abs(sum(l1) - sum(l2)) <= 1
checkIfPartition(l, l1, l2)
print('passed.')
print('-- Test 4 --')
l = [4, 15, 17, 12, 19, 20, 21,  29, 18, 14,  13, 11, 8, 5, 6]
(l1, l2) = computeBestPartition(l)
print(l1, l2, sum(l1), sum(l2))
assert abs(sum(l1) - sum(l2)) <= 0
checkIfPartition(l, l1, l2)
print('passed.')
print('All tests passed: 15 points!')


# ## Problem 3
# 
# You are giving a binary search tree $T$ and your goal is to _find the longest path in the tree_. 
#  - A path can go from a node to its parent or to one of its children.
#  - Each node can occur at most once in a path.
#  - The length of the path is the number of nodes in it.
#  
# ### Example 1
# 
# Consider the tree below
# 
# <img src="tree1.png" width="25%">
# 
# The longest path is shown in red. It has 7 nodes. Note that the longest path is not unique in this case. There is another path of length 7 that passes through the tree's root.
# 

# ### Example 2
# 
# Consider the tree below
# 
# <img src="tree2.png" width="15%">
# 
# The longest path is shown in red. It has length 7.
# 
# ---
# 
# Given a tree represented by the `TreeNode` class instance below, complete the function `getLongestPath` that returns the length of the longest path. For your convenience, we have a field called `depth` at each node of the tree which represents the length of the longest path from that node down to a leaf.

# ## Hint
# 
# Use divide and conquer by  considering
#  - longest path length in the left subtree
#  - longest path length in the right subtree
#  - longest path that passes through the current root node.
# 
# The diagram below should help.
# 
# <img src="fig1.png" width="40%">
# 
# The longest path can be entirely in the left subrtree, or right subtree, or in the third case, it can pass through the current root node. In the third case, we can use the `depth` information for left and right subtrees to figure out the length of the longest path.
# 

# In[106]:


class TreeNode:
    def __init__(self, key, parent_node=None):
        # this is the key at the current node
        self.key = key
        # store parent node information
        self.parent = parent_node
        # left and right children
        self.left = None
        self.right = None
        # depth
        self.depth = 1
    
    def is_root(self):
        return parent_node == None
    
    def insert(self, new_key):
        key = self.key
        if new_key == key:
            print(f'Already inserted key {key}. Ignoring')
        elif new_key < key:
            if self.left == None:
                new_node = TreeNode(new_key, self)
                self.left = new_node
            else:
                self.left.insert(new_key)
        else: 
            assert new_key > key
            if self.right == None:
                new_node = TreeNode(new_key, self)
                self.right = new_node
            else: 
                self.right.insert(new_key)
        #update the depth
        left_depth = self.left.depth if self.left != None else 0
        right_depth = self.right.depth if self.right != None else 0
        self.depth = max(left_depth, right_depth) + 1


# In[107]:


def getLongestPathLength(rootNode):
    # rootNode is an instance of the TreeNode class
    # The function must return the longest path length
    # your code here
    
    case1 = 0
    case2 = 0
    leftDepth = 0
    rightDepth = 0
    
    if(rootNode.left != None):
        case1 = getLongestPathLength(rootNode.left)
        leftDepth = rootNode.left.depth
        
    if(rootNode.right != None):
        case2 = getLongestPathLength(rootNode.right)
        rightDepth = rootNode.right.depth
        
    case3 = leftDepth + rightDepth + 1
    
    return max(case1, case2, case3)


# In[108]:


def make_tree(l):
    assert len(l) >= 1
    rootNode = TreeNode(l[0])
    for elt in l[1:]:
        rootNode.insert(elt)
    return rootNode

print('-- Test 1 --')
l = [55, 40, 70, 20, 47, 10, 43, 52, 50, 51]
r = make_tree(l)
path_len = getLongestPathLength(r)
print(path_len)
assert path_len == 7
print('passed')
print('-- Test 2 --')
l = [55, 40, 70, 47,  43, 52, 50, 51]
r = make_tree(l)
path_len = getLongestPathLength(r)
print(path_len)
assert path_len == 7
print('-- Test 3 --')
l = [26, 17, 41, 14, 21, 30, 47, 10, 16, 19, 23, 28, 38, 7, 12, 15, 20, 35, 39, 3]
r = make_tree(l)
path_len = getLongestPathLength(r)
print(path_len)
assert path_len == 10
print('-- Test 4--')
l = [7, 4, 18, 3, 6, 11, 19, 2, 9, 14, 22, 12, 17, 20, 21]
r = make_tree(l)
path_len = getLongestPathLength(r)
print(path_len)
assert path_len == 9
print('All Tests Passed: 15 points!')


# ## That's all folks
