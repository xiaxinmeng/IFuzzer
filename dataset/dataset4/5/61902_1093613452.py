with self.assertRaises(KeyError) as cm:
    os.environ[missing]
self.assertEqual(cm.excecption.args[0], missing)