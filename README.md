# wayland-pixel-crosshair

A pixel crosshair overlay tool for Wayland.

## Installation

Install or run with `uv` as a tool, a `pixel-crosshair` binary will be exposed under `$HOME/.local/bin`

## Usage

Run `pixel-crosshair run` and it will show a default green dot at the screen center.\
You must keep the process running to keep showing the overlay.\
It is recommended to make this a systemd service and let systemd handle this prolonged process.
