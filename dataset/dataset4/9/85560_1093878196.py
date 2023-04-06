
answers_field_order=sorted(
    set(j for i in data['items'] for j in i),
    key=cmp_to_key(lambda x,y:(
        -1 if (x,y) in answer_order 
        else (0 if x==y else 1)))
        )
