if __name__ == '__main__':
    number = 1000000
    while number:
        number -= 1
        asyncio.run(main())
    print("are you ok")
    # time_stage = timeit.timeit("asyncio.run(main())", globals=globals(), number=100000)
    # print(time_stage)