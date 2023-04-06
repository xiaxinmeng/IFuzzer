import os
import sys
import time
import stat
import socket
import email
import email.message
import re
import io
import tempfile
from test import support
from test.support import os_helper
import unittest
import textwrap
import mailbox
import glob
import test_mailbox

def test_mboxmmdf_to_mboxmmdf():
    for class_ in (mailbox.mboxMessage, mailbox.MMDFMessage):
        msg_mboxMMDF = class_(test_mailbox._sample_message)
        msg_mboxMMDF.set_flags('RODFA')
        msg_mboxMMDF.set_from('foo@bar')
        for class2_ in (mailbox.mboxMessage, mailbox.MMDFMessage):
            msg2 = class2_(msg_mboxMMDF)
            TestMessageConversion.assertEqual(msg2.get_flags(), 'RODFA')
            TestMessageConversion.assertEqual(msg2.get_from(), 'foo@bar')

TestMessageConversion = test_mailbox.TestMessageConversion()
test_mboxmmdf_to_mboxmmdf()
