    def levelOrder(self,root):
        #Write your code here
        queue = [root]
        while len(queue)!=0:
            c = queue[0]
            queue = queue[1:]
            print(c.data,'',end = '')
            if c.left is not None:
                queue.append(c.left)
            if c.right is not None:
                queue.append(c.right)