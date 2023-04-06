
@pytest.mark.asyncio
async def test_resource_leakage2():
    await _resource_handling_test(wait_for2.wait_for)
