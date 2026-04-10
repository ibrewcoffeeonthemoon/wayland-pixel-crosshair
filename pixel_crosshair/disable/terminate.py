import os
import signal
import subprocess


def terminate_existing() -> None:
    # get current pid
    current_pid = os.getpid()

    # search for related pids
    output = subprocess.check_output(['pgrep', '-f', 'wayland-pixel-crosshair'], text=True)

    # left only spawned pids
    all_pids = list(map(int, output.strip('\n').split('\n')))
    spawn_pids = list(filter(lambda x: x != current_pid, all_pids))

    # terminal them gracefully
    for pid in spawn_pids:
        os.kill(pid, signal.SIGTERM)
