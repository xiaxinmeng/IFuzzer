def _aix_bosmp64():
    # type: () -> Tuple[str, int]
    """
    Return a Tuple[str, int] e.g., ['7.1.4.34', 1806]
    The fileset bos.mp64 is the AIX kernel. It's VRMF and builddate
    reflect the current ABI levels of the runtime environment.
    """
    if _have_subprocess:
        # We expect all AIX systems to have lslpp installed in this location
        out = subprocess.check_output(["/usr/bin/lslpp", "-Lqc", "bos.mp64"])
        out = out.decode("utf-8").strip().split(":")  # type: ignore
        # Use str() and int() to help mypy see types
        return str(out[2]), int(out[-1])
    else:
        from os import uname