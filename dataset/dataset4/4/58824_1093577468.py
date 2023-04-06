vars = 'Knight', ('Gwain', 'Gallahad', 'Lancelot'), 30
c.execute('''SELECT * FROM loyalsubjects
             WHERE rank = ? 
             AND name IN (??)
             AND age >= ?
          ''', vars)