from email.header import Header

hdrin = 'Received: from mailout00.controlledmail.com (mailout00.controlledmail.com [72.81.252.19]) by mailwash7.pair.com (Postfix) with ESMTP id 16BB5BAD5 for <bcc@kitterman.com>; Sun, 13 Mar 2011 23:46:05 -0400 (EDT)'

print(Header(hdrin))