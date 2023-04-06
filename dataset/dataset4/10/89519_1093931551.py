def ClassMethod(func):
  class Wrapped(type(func)):
      def __get__(self, obj, cls=None):
          if cls is None:
              cls = type(obj)
          if hasattr(type(self.__func__), '__get__'):
              return self.__func__.__get__(cls)
          return MethodType(self.__func__, cls)
  return Wrapped(func)