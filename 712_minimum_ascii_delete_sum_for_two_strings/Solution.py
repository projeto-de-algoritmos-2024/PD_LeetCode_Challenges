from math import inf


class Solution:
    # recursive solution
    # def minimumDeleteSum(self, s1: str, s2: str) -> int:
    #     if len(s1) <= 0 and len(s2) <= 0:
    #         return 0
    #     if len(s1) <= 0:
    #         return (ord(s2[0]) + self.minimumDeleteSum(self, s1, s2[1:]))
    #     if len(s2) <= 0:
    #         return (ord(s1[0]) + self.minimumDeleteSum(self, s1[1:], s2))
    #     if s1[0] == s2[0]:
    #         return self.minimumDeleteSum(self, s1[1:], s2[1:])
    #     return min(
    #         ord(s1[0]) + self.minimumDeleteSum(self, s1[1:], s2),
    #         ord(s2[0]) + self.minimumDeleteSum(self, s1, s2[1:])
    #     )
    
    # this solution is the iterative version of the solution above
    # uses a matrix to keep track of the previous min values
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # pre-calculate string lengths
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        # pre-alocate the list for performance
        min_values = [[0] * (len_s1 + 1) for _ in range(len_s2 + 1)]
        # min_values = [[] * for _ in range(len(s2) + 1)]
        
        # pre-calculate ascii values for characters
        s1_ord = [ord(c) for c in s1]
        s2_ord = [ord(c) for c in s2]
        
        value = 0
        for i in range(len_s2+1):
            min_values[i][0] = value
            for j in range(1, len_s1+1):
                # look to the upper line
                # look to the left column
                # if the char in the line and column are the same, look to the upper-right diagonal
                # get the min of these possibilities
                upper_value = inf
                diagonal_value = inf
                left_value = inf
                
                # print(i, j)

                if i-1 >= 0:
                    upper_value = min_values[i-1][j] + s2_ord[len_s2-i]
                if i-1 >= 0 and s2[len_s2-i] == s1[len_s1-j]:
                    diagonal_value = min_values[i-1][j-1]
                left_value = min_values[i][j-1] + s1_ord[len_s1-j]
                
                new_value = min(upper_value, left_value, diagonal_value)
                min_values[i][j] = new_value
                
                # for line in min_values:
                #     print(line)
                
            value = value + s2_ord[len_s2-i-1]
        
        return min_values[len_s2][len_s1]
    
print(Solution.minimumDeleteSum(Solution, "delete", "leet"))