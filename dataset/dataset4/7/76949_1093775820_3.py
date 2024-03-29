if __name__ == "__main__":
    t1 = StatefulThing()
    t2 = StatefulThing()
    print("> t1, say hello:")
    t1.say_hello()
    print("> t2, say goodbye:")
    t2.say_goodbye()
    print("> t2, say hello:")
    t2.say_hello()
    print("> t1, say hello:")
    t1.say_hello()
    print("> t1, say hello followed by goodbye:")
    t1.say_hello_followed_by_goodbye()
    print("> t2, say goodbye:")
    t2.say_goodbye()
    print("> t2, say hello followed by goodbye:")
    t2.say_hello_followed_by_goodbye()
    print("> t1, say goodbye:")
    t1.say_goodbye()
    print("> t2, say hello:")
    t2.say_hello()
    print("---")
    print( "t1 said {} hellos and {} goodbyes."
           .format(t1.hello_count, t1.goodbye_count) )
    print( "t2 said {} hellos and {} goodbyes."
           .format(t2.hello_count, t2.goodbye_count) )