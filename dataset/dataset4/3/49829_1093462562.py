class Interface(TabbedPane):
   class FirstTab(Pane):
        label = 'First Tab'
        LineEdit('First Name', length=20)
        LineEdit('Last Name', length=30)
        ComboBox('Title', length=10,
                 list=['Mr', 'Mrs', 'Ms', 'Dr', 'BDFL'])
   class SecondTab(Pane):
        label = 'Second Tab'
        LineEdit('City', length=20)
        LineEdit('Street', length=30)