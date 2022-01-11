
class Stack:
    def __init__(self):
        '''
        Objective: To initialize data memebers of the Stack
        Input Parameter:
        self(implicit parameter) -object of the type Stack
        Return Value: None
        '''
        self.values=list()
    def push(self,element):
        '''
        Objective: To put an elemenet on top the stack
        Input Parameter:
        self(implicit parameter) -object of the type Stack
        element-value to be inserted
        Return Value: None
        '''
        
        self.values.append(element)   
    def isempty(self):
        '''
        Objective: To determine if the stack is empty
        Input Parameter:
        self(implicit parameter) -object of the type Stack
        element-value to be inserted
        Return Value: true if the stack is empty.else false
        '''
        return len(self.values)==0
    def pop(self):
        '''
        Objective: To remove an element from the top of a stack
        Input Parameter:
        self(implicit parameter) -object of the type Stack
        element-value to be inserted
        Return Value: top element of the stack, if stack is not empty,else None
        '''
       
        
        if(not(self.isempty())):
            return self.values.pop()
        else:
            print('Stack Underflow') 
            return None
    def top(self):
        '''
        Objective: To return the top of the stack
        Input Parameter:
        self(implicit parameter) -object of the type Stack
        element-value to be inserted
        Return Value: top element of the stack, if stack is not empty,else None
        '''

        if(not(self.isempty())):
            return self.values[-1]
        else:
            print('Stack Empyty')
            return None
    def size(self):
        '''
        Objective: To return the number of elements in the stack.
        Input Parameter:
        self(implicit parameter) -object of the type Stack
        element-value to be inserted
        Return Value: Number of elements in stack -  numeric
        '''
        return len(self.values)
    def __str__(self):
        '''
        Objective: To return the string representation of  the stack.
        Input Parameter:
        self(implicit parameter) -object of the type Stack
        element-value to be inserted
        Return Value: string
        '''
        stringRepr=''
        for i in reversed(self.values):
            stringRepr += str(i) +'\t'
        return stringRepr
