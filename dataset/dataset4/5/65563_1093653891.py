import io
buf = io.BytesIO()
sys.stdout = io.TextIOWrapper(buf,
    encoding='utf-8',
    errors='strict', # or surrogate-escape as this is the default for stdout now? not sure
    line_buffering=True
)