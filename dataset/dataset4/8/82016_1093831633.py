class InnerClass():
    @store_namespace(locals())
    def method() -> 'InnerClass':
        ...