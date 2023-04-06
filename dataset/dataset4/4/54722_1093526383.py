for item in TableA.findall():
  TableB.new_item(name=item.name)
  connection.commit()