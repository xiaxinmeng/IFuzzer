from mailbox import mbox
mb = mbox('mbox')
del mb[len(mb)-1]
mb.close()