#User function Template for python3
import heapq
class node:
    def __init__(self, freq, symbol, left=None, right= None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
    def __lt__(self,nxt):
        return self.freq < nxt.freq


def getList(ans,node, val = ''):
    
    newval = val + str(node.huff)
    
    if node.left:
        getList(ans, node.left, newval)
    if node.right:
        getList(ans, node.right, newval)
    
    if not node.left and not node.right:
        ans.append(newval)
            

class Solution:
    

    def huffmanCodes(self,S,f,N):
        # Code here
        nodes = []
        for x in range(len(S)):
            heapq.heappush(nodes,node(f[x],S[x]))
        
        while len(nodes) > 1:
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)
            
            left.huff = '0'
            right.huff = '1'
            
            newnode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
            heapq.heappush(nodes, newnode)
        
        ans = []
        getList(ans,nodes[0])
        return ans
            