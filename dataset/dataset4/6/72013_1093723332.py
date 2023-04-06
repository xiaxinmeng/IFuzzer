import marshal

value = (       # tuple1
        "this is a string", #string1
        [
            1,  # int1
            2,  # int2
            3,  # int3
            4   # int4
        ],
        (       #tuple2
            "more tuples",  #string2
            1.0,    # float1
            2.3,    # float2
            4.5     # float3
        ),
        "this is yet another string"
    )

dump = marshal.dumps(value)

data = bytearray(dump)
data[10] = 40
data[4] = 16
data[103] = 143
data[97] = 245
data[78] = 114
data[35] = 188

marshal.loads(bytes(data))