from unittest.mock import patch, Mock
p = patch('requests.get', autospec=True)
manager = Mock()
manager.attach_mock(p.start(), 'requests_get')

import requests
requests.get('https://google.com')
print(manager.mock_calls)
p.stop()
print(manager.mock_calls)