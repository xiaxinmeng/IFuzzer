def item_cache_key(items: List[SingleItem]):
  return (timestamp for timestamp, data in items)