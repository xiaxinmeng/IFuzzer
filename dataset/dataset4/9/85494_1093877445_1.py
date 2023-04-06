
def test_subprocess_wait_no_same_group(self):
        # start the new process in a new session
        connect = self.loop.subprocess_shell(
                        functools.partial(MySubprocessProtocol, self.loop),
                        'exit 7', stdin=None, stdout=None, stderr=None,
                        start_new_session=True)
        transp, proto = self.loop.run_until_complete(connect)
        self.assertIsInstance(proto, MySubprocessProtocol)
        self.loop.run_until_complete(proto.completed)
        self.assertEqual(7, proto.returncode)
        transp.close()
