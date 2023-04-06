with patch.object(sub.__class__.spam, '__doc__', 'Spam'):
    self.assertEqual(sub.__class__.spam.__doc__, 'Spam')