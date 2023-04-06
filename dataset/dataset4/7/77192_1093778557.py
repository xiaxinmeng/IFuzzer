import sys

import pathlib



class DummyImportHook(object):

    def __init__(self, *args):

        self.is_script_path_to_sys_path_be_done = False