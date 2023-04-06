def no_need_re():
    text = "tf.where(condition, x=None, y=None, name=None) tf.batch_gather ..."
    pattern_list = ['tf.batch_gather', 'None']
    for item in pattern_list:
        text=text.replace(item, '`'+item+'`')

    print(text)

no_need_re()