
import ssl

ssl._create_stdlib_context = ssl.create_default_context
