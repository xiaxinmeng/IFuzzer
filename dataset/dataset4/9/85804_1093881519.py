def testBindingError(self):
        '''
        test list of Records with incomplete record leading to
        "You did not supply a value for binding 2"
        see https://bugs.python.org/issue41638
        '''
        listOfRecords=[{'name':'Pikachu', 'type':'Electric'},{'name':'Raichu' }]
        for executeMany in [True,False]:
            try:
                self.checkListOfRecords(listOfRecords,'Pokemon','name',executeMany=executeMany)
                self.fail("There should be an exception")
            except Exception as ex:
                if self.debug:
                    print(str(ex))
                self.assertTrue('no value supplied for column' in str(ex))   