class JobStatus(CaseInsensitiveStrEnum, LenientStrEnum):
    ACTIVE = "active"
    PENDING = "pending"
    TERMINATED = "terminated"