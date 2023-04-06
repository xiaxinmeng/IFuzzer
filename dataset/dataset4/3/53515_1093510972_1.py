# each employee references the parent company
for e in company.employees:
    assert e.company is company