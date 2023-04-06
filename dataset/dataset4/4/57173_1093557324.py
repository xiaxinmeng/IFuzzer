import locale
ianaLanguageSubtag='en'       # the desired national locale
locale.setlocale(locale.LC_ALL,
  (ianaLanguageSubtag, locale.getpreferredencoding())) #(1)
locale.setlocale(locale.LC_ALL,
  locale.normalize(ianaLanguageSubtag))                #(2)