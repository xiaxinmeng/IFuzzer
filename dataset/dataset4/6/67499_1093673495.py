def test_setting_magic_method_for_mock(self):
    m = Mock()
    m.configure_mock(**{'__str__.return_value': "14"})
    self.assertEqual(str(m), "14")
        
def test_setting_magic_method_in_mock_initialization(self):
    m = Mock(**{'__str__.return_value': "12"})
    self.assertEqual(str(m), "12")