if name is None:
   self._name = f'Task-{_task_name_counter()}'
elif isinstance(name, str):
   self._name = name
else:
   self._name = str(name)