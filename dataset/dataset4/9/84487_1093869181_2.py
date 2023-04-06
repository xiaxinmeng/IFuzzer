
listener_client["faked"] = (None, Mock(side_effect=RuntimeError("BROKEN")))
