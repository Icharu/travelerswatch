#!/usr/bin/env python3
"""Time the watchman hook per prompt.

Usage: python3 -I tests/bench_hook.py <hook.sh> <runs> <project_dir> [<project_dir> ...]

Each project_dir is passed as CLAUDE_PROJECT_DIR; the hook gets a minimal UserPromptSubmit
JSON on stdin, exactly as Claude Code would send it. Prints median / mean / p95 / max wall
time per run (process start to exit) and the size of the injected text.
"""
import os
import statistics
import subprocess
import sys
import time

STDIN = b'{"session_id":"bench","hook_event_name":"UserPromptSubmit","prompt":"x"}'


def main() -> int:
    if len(sys.argv) < 4:
        print(__doc__)
        return 2
    hook, runs, projects = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
    print(f"| Project | Runs | Median (ms) | Mean (ms) | p95 (ms) | Max (ms) | Injected chars | ≈ tokens |")
    print(f"|---|---|---|---|---|---|---|---|")
    for project in projects:
        env = dict(os.environ, CLAUDE_PROJECT_DIR=project)
        times, out = [], b""
        for _ in range(runs):
            start = time.perf_counter()
            out = subprocess.run(["bash", hook], input=STDIN, env=env, capture_output=True).stdout
            times.append((time.perf_counter() - start) * 1000)
        times.sort()
        chars = len(out.decode("utf-8"))
        p95 = times[max(0, int(runs * 0.95) - 1)]
        print(f"| {os.path.basename(project.rstrip('/'))} | {runs} | {statistics.median(times):.1f} | "
              f"{statistics.mean(times):.1f} | {p95:.1f} | {times[-1]:.1f} | {chars} | {chars // 4} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
