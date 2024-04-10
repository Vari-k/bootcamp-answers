# Middle of the Linked List

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Reverse Nodes in k-Group

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        current = head
        for _ in range(k):
            if not current:
                return head  
            current = current.next

        prev, current = None, head
        for _ in range(k):
            next_temp = current.next  
            current.next = prev  
            prev = current  
            current = next_temp 

        head.next = self.reverseKGroup(current, k)
        
        return prev


# Valid Sudoku

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                
                if num in rows[i]:
                    return False
                rows[i].add(num)
                
                if num in cols[j]:
                    return False
                cols[j].add(num)
                
                boxIndex = (i // 3) * 3 + j // 3
                if num in boxes[boxIndex]:
                    return False
                boxes[boxIndex].add(num)
        
        return True

        
