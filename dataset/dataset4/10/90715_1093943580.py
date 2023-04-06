
import logging
import warnings

import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

logging.captureWarnings(True)

sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.WARNING
)

sentry_sdk.init(
    "<ingest URL>",
    traces_sample_rate=1.0,
    integrations=[
        LoggingIntegration(
            level=logging.INFO,
            event_level=logging.WARNING
        )
    ]
)

warnings.warn("A warning")
warnings.warn("Another warning")
