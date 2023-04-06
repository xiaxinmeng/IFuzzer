# Copyright 2021 Google LLC.
# SPDX-License-Identifier: Apache-2.0
import contextlib
import os

@contextlib.contextmanager
def my_tmp_file():
  with tempfile.NamedTemporaryFile('w') as f:
    yield f