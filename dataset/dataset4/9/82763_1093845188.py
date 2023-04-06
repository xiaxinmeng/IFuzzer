def actual_re_demo():
    import re
    # This is an indefinite string...
    text = "tf.where(condition, x=None, y=None, name=None) tf.batch_gather ..."

    # Converting fields that need to be matched into regular expressions is also an indefinite string
    pattern_str = re.compile('(tf\\.batch_gather)|(None)|(a1)')

    #I don't know how many, so it's over \ \ 100 \ \ n
    x = re.sub(pattern_str, '`'+'\\1\\2'+'`', text)

    print(x)

    # hope if：tf.Prefix needs to match,The result will be:`tf.xx`，

    # But in fact, it's not just TF. As a prefix, it's a random character, it can be a suffix, it can be other characters.

    #  If more than 100, the result is=>：989¡¢£¤¥¦§89¨©ª«¬­®¯89°±²³´µ¶·89¸¹º»¼½¾¿890123`, name=`[None@ABCDEFG89HIJKLMNO89PQRSTUVW89XYZ](mailto:None@ABCDEFG89HIJKLMNO89PQRSTUVW89XYZ)[\]^_89`abcdefg89hijklmno89pqrstuvw89xyz{|}~8901234567890123456789

    # I noticed in the comment area that it was caused by a confusion of Radix, which seems to be embarrassing.