import asyncio
from unittest.mock import patch, Mock

with patch.object(asyncio.get_event_loop(), '_accept_connection2', Mock()) as f:
    print(f)
    f()