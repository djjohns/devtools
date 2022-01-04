class First():
    def __init__(self):
        print("Inherited from First")
        life = 42
        print(life)
        
        
class Second(First):
    def __init__(self):
        print("Inherited from Second")
        super().__init__()
        # First.__init__(self)
        
        
class Third(Second):
    def __init__(self):
        print("Inherited from Third")
        super().__init__()

        
class Fourth(Third):
    def __init__(self):
        print('Inherited from Fourth')
        super().__init__()
        print('What is the meaning of life?')

        
call_class = Fourth()