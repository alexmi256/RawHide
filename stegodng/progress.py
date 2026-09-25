"""Progress-bar helpers (tqdm wrappers).

All progress output goes to stderr so stdout stays parseable for
``auto-config`` / ``wrote`` / ``recovered`` lines. ``progress=True``
forces bars on, ``progress=False`` disables them, and
``progress=None`` (the default) shows them only when stderr is a TTY
so non-interactive runs and captured test output stay quiet.
"""
from __future__ import annotations

import sys
from contextlib import contextmanager


def enabled(progress: bool | None) -> bool:
    """Resolve ``True``/``False``/``None`` (auto) to a concrete flag."""
    if progress is None:
        try:
            return sys.stderr.isatty()
        except Exception:
            return False
    return bool(progress)


@contextmanager
def bar(total=None, desc: str = "", unit: str = "it",
        disable: bool = False, position: int = 0, leave: bool = True):
    """Yield a tqdm bar, or a silent no-op fallback.

    Falls back to a no-op when tqdm is unavailable (e.g. minimal
    installs) so encode/decode keep working without progress.
    """
    try:
        from tqdm import tqdm
    except ImportError:
        class _Noop:
            def update(self, n=1):
                pass

            def close(self):
                pass
        yield _Noop()
        return
    pbar = tqdm(total=total, desc=desc, unit=unit, unit_scale=True,
                disable=disable, position=position, leave=leave,
                dynamic_ncols=True)
    try:
        yield pbar
    finally:
        pbar.close()
