import re
message = "Flushed to [BigTableReader(path='/data/cassandra/data/log/logEntry_202202-e68971800b2711ecaf770d5fa3f5ae87/md-112-big-Data.db')] (1 sstables, 8,650MiB), biggest 8,650MiB, smallest 8,650MiB"
regex = re.compile(r"Flushed to \[(?P<sstables>[^]]+)+\] \((?P<sstable_count>[^ ]+) sstables, (?P<total_size>[^)]+)\), biggest (?P<biggest_size>[^,]+), smallest (?P<smallest_size>[^ ]+)( \((?P<duration>\d+)ms\))?")
regex.match(message)