def get_identifiers(template):
    return list(
        set(
            filter(
                lambda v: v is not None,
                (mo.group('named') or mo.group('braced') 
                 for mo in template.pattern.finditer(template.template))
            )
        )
    )