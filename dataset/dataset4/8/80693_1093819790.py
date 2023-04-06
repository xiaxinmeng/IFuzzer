class CustomExecutor:
	...

custom_executor = CustomExecutor()
custom_future = custom_executor.submit(workload, context=context_information)
...
assert custom_future.context_has_some_property()
assert custom_future.result_has_some_property()