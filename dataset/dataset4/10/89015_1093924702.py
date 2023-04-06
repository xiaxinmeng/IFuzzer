
def setUpModule():
    support.ignore_deprecations_from("asyncio.base_events", like=r".*loop argument.*")
    support.ignore_deprecations_from("asyncio.unix_events", like=r".*loop argument.*")
    support.ignore_deprecations_from("asyncio.futures", like=r".*loop argument.*")
    support.ignore_deprecations_from("asyncio.runners", like=r".*loop argument.*")
    support.ignore_deprecations_from("asyncio.subprocess", like=r".*loop argument.*")
    support.ignore_deprecations_from("asyncio.tasks", like=r".*loop argument.*")
    support.ignore_deprecations_from("test.test_asyncio.test_queues", like=r".*loop argument.*")
    support.ignore_deprecations_from("test.test_asyncio.test_tasks", like=r".*loop argument.*")

def tearDownModule():
    support.clear_ignored_deprecations()
