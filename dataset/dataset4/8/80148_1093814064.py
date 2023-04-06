# Seed uname cache to avoid calling uname
platform._uname_cache = platform.uname_result(
    system='Linux',
    node='moon',
    release='5.99.99',
    version='#1 SMP 2020',
    machine='x86_64',
    processor='x86_64')