len = _tcslen(ppPaths[index]);
_tcsncpy(szCur, ppPaths[index], len);
szCur += len;
dataSize -= len;