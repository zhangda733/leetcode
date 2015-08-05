# -*- coding:utf-8 -*-

'''
Created on 2015年8月4日

@author: dazhang

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Recurution can work and pass, but is too slow.
'''
class Solution2:
    def __init__(self):
        self.maxLength = 0
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root == None:
            return 0
        self.travel(root, 1)
        return self.maxLength
    
    def travel(self, root, length):
        print self.maxLength
        if root.left == None and root.right == None:
            self.maxLength = max(self.maxLength, length)
            return 
        if root.left != None:
            self.travel(root.left, length + 1)
        if root.right != None:
            self.travel(root.right, length + 1)
        
class Solution:
    def __init__(self):
        self.maxLength = 0
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root == None:
            return 0
        nodes = []
        l = []
        length = 0
        maxLength = 0
        nodes.append(root)
        l.append(0)
        while(len(nodes) > 0):
            length += 1
            #print(length)
            #print(l)
            cur = nodes.pop()
            curL = l.pop()
            if cur.right == None and cur.left == None:
                maxLength = max(length, maxLength)
                #print l
                if len(l) > 0:
                    length = l[len(l) - 1]
            if cur.right != None:
                nodes.append(cur.right)
                l.append(length)
            if cur.left != None:
                nodes.append(cur.left)
                l.append(length)
        return maxLength      

if __name__ == '__main__':
    root = TreeNode(1)
    l1 = TreeNode(2)
    l2 = TreeNode(3)
    l3 = TreeNode(4)
    l4 = TreeNode(5)
    l5 = TreeNode(5)
    l6 = TreeNode(5)
    root.left = l1
    root.right = l2
    l1.left = l3
    l2.left = l4
    l4.left = l5
    l5.left = l6
    s = Solution()
    print(s.maxDepth(root))
    pass