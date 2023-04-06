a = "import os"
self.check_both(a, a)  # Fails, tries to translate "import os" into
"from . import os"