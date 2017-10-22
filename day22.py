    def getHeight(self,root):
        #Write your code here
        return -1 if root is None else max(1+ self.getHeight(root.left),1+self.getHeight(root.right))