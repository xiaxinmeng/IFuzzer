class ErrorRecognizingURLopener(urllib.FancyURLopener):
    http_error_default = urllib.URLopener.http_error_default

urllib._urlopener = ErrorRecognizingURLopener()