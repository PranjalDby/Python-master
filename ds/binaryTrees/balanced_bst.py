
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = -1


class Balanced_Bst:

    def insert_bst(self,root,data):
        if root == None:
            newnode = Node(data)
            newnode.data = data
            root = newnode
        
        if data < root.data:
            root.left =  self.insert_bst(root.left,data)

        elif data > root.data:
            root.right = self.insert_bst(root.right,data)

        root.height = max(self.getHeight(root.left),self.getHeight(root.right)) + 1

        bf = self.get_balance_factor(root)

        return self.balancing(root,bf,data)
        
    

    def balancing(self,root,bf,key) :
        if root != None:
            # LL-case
            if bf > 1 and key < root.left.data:
                return self.right_rotate(root)
            
            if bf < -1 and key > root.right.data:
                return self.Left_Rotate(root)
            
            # L-R case
            if bf > 1 and key > root.left.data:
                root.left = self.Left_Rotate(root.left)
                return self.right_rotate(root)
            
            if bf < -1 and key < root.right.data:
                root.right = self.right_rotate(root.right)
                return self.Left_Rotate(root)
                
        return root
            

    def right_rotate(self,root):
        print('Called RIGHT-ROTATION')
        y = root.left
        t2 = y.right
        y.right = root
        root.left = t2
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    
    def Left_Rotate(self,root):
        print('CALLED LEFT-ROTATE')
        y = root.right
        t2 = y.left
        y.left = root
        root.right = t2
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    
    def getHeight(self,root):
        if root == None:
            return -1
        
        return root.height

        
    def get_balance_factor(self,root):
        if root == None:
            return 0
        
        return (self.getHeight(root.left) - self.getHeight(root.right))
    

    def inorder_trav(self,root):
        if root == None:
            return
        
        self.inorder_trav(root.left)
        print(root.data)
        self.inorder_trav(root.right)
        

instance = Balanced_Bst()

root = None
root = instance.insert_bst(root,41)
root = instance.insert_bst(root,65)
root = instance.insert_bst(root,50)
root = instance.insert_bst(root,20)
root = instance.insert_bst(root,11)
root = instance.insert_bst(root,29)
root = instance.insert_bst(root,26)
root = instance.insert_bst(root,30)
root = instance.insert_bst(root,31)
# instance.insert_bst(root,32)

instance.inorder_trav(root)