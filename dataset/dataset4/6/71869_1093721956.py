class Endday(models.Model):
  company = models.TextField(null=True)
  eop = models.TextField(max_length=100000) 