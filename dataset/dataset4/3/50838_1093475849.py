class MySmtpServer( smtpd.SMTPServer, object ):
   def __init__( self, **kwargs ):
      try:
         super( _SmtpSink, self).__init__(**kwargs)
      except Exception as e:
         self.close()   # cleanup asyncore after failure
         raise