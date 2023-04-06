console
## 1. Understand CPython's deviation from libexpat 2.4.1 upstream
# git clone --depth 1 https://github.com/python/cpython  # i.e. main
# git clone --depth 1 --branch R_2_4_1 https://github.com/libexpat/libexpat libexpat_2_4_1
# diff --color=always -r -u libexpat_2_4_1/expat/lib/ cpython/Modules/expat/ | less

## 2. Understand jouve CPython's deviation from libexpat 2.4.4 upstream
# git clone --depth 1 --branch expat_R_2_4_4 https://github.com/jouve/cpython jouve_cpython
# git clone --depth 1 --branch R_2_4_4 https://github.com/libexpat/libexpat libexpat_2_4_4
# diff --color=always -r -u libexpat_2_4_4/expat/lib/ jouve_cpython/Modules/expat/ | less
