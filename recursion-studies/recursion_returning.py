class recursionReturningStudies:

    # what is the return of this fuction?
    def recursionReturningNone(self, someValue):
        if someValue == 10:
            return
        
        val = self.recursionReturningNone(someValue+1)
        #print(val)
        return val
    # for someValue initialized with 0, the return is None, printed 10 times



    # what is the return of this fuction?
    def recursionReturningOneTimeOnly(self, someValue):
        if someValue == 10:
            return 1
        
        val = self.recursionReturningOneTimeOnly(someValue+1)
        #print(val)
        return val
    # for someValue initialized with 0, the return is one 1 printed 10 times



    # what is the return of this fuction?
    def recursionSummingAndReturningOneValue(self, someValue):
        if someValue == 10:
            return 1
        
        val = (1 + self.recursionSummingAndReturningOneValue(someValue+1))
        #print(val)
        return val
    # for someValue initialized with 0, the return is 2, 3, 4, 5, 6, 7, 8, 9, 10, 11



    # what is the return of this fuction?
    def recursionReturningOneValueAndSummingAfter(self, someValue):
        if someValue == 10:
            return 1
        
        val = (self.recursionReturningOneValueAndSummingAfter(someValue+1) + 1)
        print(val)
        return val
    # for someValue initialized with 0, the return is 2, 3, 4, 5, 6, 7, 8, 9, 10, 1
    

rec = recursionReturningStudies()

rec.recursionReturningNone(0)
rec.recursionReturningOneTimeOnly(0)
rec.recursionSummingAndReturningOneValue(0)
rec.recursionReturningOneValueAndSummingAfter(0)