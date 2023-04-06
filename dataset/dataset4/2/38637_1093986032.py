rx = re.compile(
   r'''^UPDATE\s+\w+\s+SET\s+locked_until\s*=\s*
   (?=(
       ([^=,]+\s*)+
   ))\1
   ,         #trailing literal
   ''', 
   re.I | re.X
)