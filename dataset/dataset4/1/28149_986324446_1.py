
@pytest.mark.asyncio
async def test_resource_leakage_wf2_callback():
    # handle the cancellation-completion race condition with a callback
    await _resource_handling_test(wait_for2.wait_for, race_handler=cleanup_resource)


@pytest.mark.asyncio
async def test_resource_leakage_wf2_except():
    # handle the cancellation-completion race condition as an exception
    await _resource_handling_test(wait_for2.wait_for, use_special_raise=True)
