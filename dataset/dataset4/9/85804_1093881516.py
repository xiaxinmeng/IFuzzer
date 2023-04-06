def testBindingError(self):
        '''
        test list of Records with incomplete record leading to
        "You did not supply a value for binding 2"
        '''
        listOfRecords=[{'name':'Pikachu', 'type':'Electric'},{'name':'Raichu' }]
        resultList=self.checkListOfRecords(listOfRecords,'Pokemon','name')