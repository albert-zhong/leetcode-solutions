class Solution(object):
    def is_valid_mutation(self, current_mutation, next_mutation):
        changes = 0
        for i in range(len(current_mutation)):
            if current_mutation[i] != next_mutation[i]:
                changes += 1
        return changes == 1
    
    def minMutation(self, start, end, bank):
        queue = []
        queue.append([start, start, 0])
        
        while queue:
            current, previous, steps = queue.pop(0)

            if current == end:
                return steps
            
            for string in bank:
                if string != previous and self.is_valid_mutation(current, string):
                    queue.append([string, current, steps + 1])
                    
        return -1
