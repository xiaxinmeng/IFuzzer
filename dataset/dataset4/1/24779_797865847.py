
    # Let g = gcd(da, db). Then
    # 
    #     na   nb    na*(db//g)   nb*(da//g)
    #     -- + -- == ---------- + ----------
    #     da   db    da*(db//g)   db*(da//g)
    #             
    #                na*(db//g) + nb*(da//g)
    #             == -----------------------
    #                       da*db//g
    # 
    # When g is large, this can help decrease the size of the
    # multiplications required.
    # 
    # We'll special-case g == 1, since 60.8% of randomly-chosen
    # integers are coprime.
    # 
    # We can also optimize the normalization of the resulting
    # fraction. Note that the denominator da*db//g can be re-written
    # as (da//g)*(db//g)*g. Helpfully,
    # 
    #     gcd(da//g, numerator) == gcd(da//g, na*(db//g) + nb*(da//g))
    #                           == gcd(da//g, na*(db//g))
    #                           == 1.
    # 
    # The last equality holds because:
    # 
    #     (da//g, na) share no factors: the input was normalized.
    #     (da//g, db//g) share no factors: common ones are removed.
    # 
    # For the same reason, gcd(db//g, numerator) == 1. Applying these,
    # 
    #     gcd(numerator, denominator)
    #         == gcd(numerator, (da//g)*(db//g)*g)
    #         == gcd(numerator, g).
    # 
    # This is useful because the unnormalized denominator could be
    # much larger than g.
