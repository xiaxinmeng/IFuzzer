
import time
from unittest.mock import call
from unittest.mock import patch


with patch("time.sleep") as mock_obj:
    time.sleep(1)
    time.sleep(2)

    print("mock_obj.call_args_list")
    print(mock_obj.call_args_list)

    print("mock_obj.call_args_list == [(1,), (2,)]")
    print(mock_obj.call_args_list == [(1,), (2,)])
    print("mock_obj.call_args_list == [call(1,), call(2,)]")
    print(mock_obj.call_args_list == [call(1,), call(2,)])
