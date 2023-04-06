# XXX(nnorwitz): disable this test by looking for extra largfile [sic] resource
# which doesn't exist.  This test takes over 30 minutes to run in general
# and requires more disk space than most of the buildbots.
support.requires(
        'extralargefile',
        'test requires loads of disk-space bytes and a long time to run'
    )