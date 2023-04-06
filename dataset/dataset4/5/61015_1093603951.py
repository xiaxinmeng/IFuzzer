#!/usr/bin/python3.3
#-*- coding: latin1 -*-
from email.message import Message
from email import policy
from email.parser import FeedParser

Parser= FeedParser(policy=policy.SMTP)
Parser.feed('From jarausch@igpm.rwth-aachen.de  Tue Apr 24 15:09:24 2012\n')
Parser.feed('X-Status:    \n')  # this triggers the bug
Parser.feed('From: Helmut Jarausch <jarausch@igpm.rwth-aachen.de>\n')

Msg= Parser.close()
Msg_as_str= Msg.as_string(unixfrom=True)