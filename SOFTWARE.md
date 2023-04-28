# Recommended Software

To complete the challenges, you may require the following software.

Completing the CTF is entirely possible on any OS, but I recommend Linux (obvious reasons).


- An SSH client:
  - Ubuntu: `apt install openssh-client`
  - Fedora: `dnf install openssh-client`
  - Windows:
    - PuTTY: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
    - MobaXTerm: https://mobaxterm.mobatek.net/download.html
- NetCat & Nmap
  - Ubuntu: `apt install ncat nmap`
  - Fedora: `dnf install nmap-ncat-2 nmap`
  - Windows: https://nmap.org/download.html
- WireShark:
  - Ubuntu: `add-apt-repository ppa:wireshark-dev/stable && apt-get update && apt-get install wireshark`
  - Fedora: `dnf install wireshark-qt && usermod -a -G wireshark $USER`
  - Windows: https://www.wireshark.org/download.html
  - Lab PC: Go to windows link above and download PortableApps version
- Python 3.8+: https://www.python.org/downloads/
- 7-zip (or similar): https://7-zip.org/download.html
- git (2.36.0+ recommended):
  - Ubuntu: `add-apt-repository ppa:git-core/ppa && apt-get update && apt-get install git`
  - Fedora: `dnf install git`
  - Windows: https://git-scm.com/
- Strings:
  - Ubuntu: `apt install binutils`
  - Fedora: `dnf install binutils`
  - Windows: https://learn.microsoft.com/en-gb/sysinternals/downloads/strings
