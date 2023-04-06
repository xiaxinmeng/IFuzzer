import datetime

def test(text):
    try:
        d = datetime.datetime.strptime(text, '%Y%m%dT%H%M')
    except ValueError:
        pass
    else:
        print("%s without seconds => %s" % (text, d))
        return
    d = datetime.datetime.strptime(text, '%Y%m%dT%H%M%S')
    print("%s with seconds => %s" % (text, d))

test('20110817T1234')
test('20110817T12345')
test('20110817T123456')