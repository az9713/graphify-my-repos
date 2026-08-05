# Installing Claude Code on WSL2: A Troubleshooting Guide

## The Problem

Running the official Claude Code install command in WSL2:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Fails with:

```
curl: (56) OpenSSL SSL_read: error:0A000119:SSL routines::decryption failed or bad record mac
```

This is caused by a [well-known WSL2 networking bug](https://github.com/microsoft/WSL/issues/4698) where the Hyper-V virtual network adapter corrupts packets during large SSL/TLS transfers. curl uses OpenSSL which fails hard on corrupted records, while wget uses GnuTLS which handles it gracefully.

## Quick Fix

```bash
wget -qO /tmp/install.sh https://claude.ai/install.sh
sed -i 's/if command -v curl/if false/' /tmp/install.sh
sed -i 's/"$binary_path" install/"$binary_path" install --force/' /tmp/install.sh
bash /tmp/install.sh
```

This downloads the install script with wget (GnuTLS), patches it to skip curl, and adds `--force` to bypass the network check during setup.

## Permanent Fix

Switch WSL2 to mirrored networking (Windows 11 23H2+) by creating `%USERPROFILE%\.wslconfig`:

```ini
[wsl2]
networkingMode=mirrored
```

Then restart WSL: `wsl --shutdown`

## Full Guide

See [wsl_install_guide.md](wsl_install_guide.md) for the complete troubleshooting journey, including all failed solutions and detailed root cause analysis.

## Environment Tested

- Windows 10 (MINGW64_NT-10.0-26200)
- WSL2 with Ubuntu 24.04.2 LTS
- OpenSSL 3.0.13 / curl with OpenSSL backend
