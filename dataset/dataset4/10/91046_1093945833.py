def test_normal_posix_in_opt(self):
          """Test a 'standard' install layout on *nix
          
          This uses '/opt/python9.8' as PREFIX
          """
          ns = MockPosixNamespace(
              PREFIX="/opt/python9.8",
              argv0="python",
              ENV_PATH="/usr/bin:/opt/python9.8/bin",
          )
          ns.add_known_xfile("/opt/python9.8/bin/python")
          ns.add_known_file("/opt/python9.8/lib/python9.8/os.py")
          ns.add_known_dir("/opt/python9.8/lib/python9.8/lib-dynload")
  
          # This shouldn't matter:
          ns.add_known_file("/opt/lib/python98.zip")
  
          expected = dict(
              executable="/opt/python9.8/bin/python",
              base_executable="/opt/python9.8/bin/python",
              prefix="/opt/python9.8",
              exec_prefix="/opt/python9.8",
              module_search_paths_set=1,
              module_search_paths=[
                  "/opt/python9.8/lib/python98.zip",
                  "/opt/python9.8/lib/python9.8",
                  "/opt/python9.8/lib/python9.8/lib-dynload",
              ],
          )
          actual = getpath(ns, expected)
          self.assertEqual(expected, actual)