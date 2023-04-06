
@pytest.mark.asyncio
async def test_resource_leakage1():
    await _resource_handling_test(asyncio.wait_for)

@pytest.mark.asyncio
async def test_resource_leakage2():
    await _resource_handling_test(wait_for2.wait_for)

@pytest.mark.asyncio
async def test_resource_leakage3():
    await _resource_handling_test(wait_for)
