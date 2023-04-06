print('new locale:', crt_locale._wsetlocale(0, 'de_DE'))
print('count:', crt_time.wcsftime(wbuf, 1024, '%Z', tm))