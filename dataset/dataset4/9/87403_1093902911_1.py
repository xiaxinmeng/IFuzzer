# Timestamp comparison
self.assertEqual(datetime_in_sgt, datetime_in_utc)
# Timezone comparison
self.assertEqual(datetime_in_sgt.tzinfo, datetime_in_utc.tzinfo)