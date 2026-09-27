# Local wordlists

These entries point to selected files inside the checked out SecLists repository
in `../05_REPOS/SecLists/`. Relative symbolic links keep one authoritative copy
and preserve the upstream directory unchanged.

| File | Source | Purpose | Size |
|---|---|---|---:|
| `common.txt` | [SecLists Discovery/Web-Content/common.txt](https://github.com/danielmiessler/SecLists/blob/39166b57cfcc73afd87081cfb20bd317cdece6ff/Discovery/Web-Content/common.txt) | Small baseline for web paths and content discovery | 38,536 bytes |
| `raft-small-directories.txt` | [SecLists Discovery/Web-Content/raft-small-directories.txt](https://github.com/danielmiessler/SecLists/blob/39166b57cfcc73afd87081cfb20bd317cdece6ff/Discovery/Web-Content/raft-small-directories.txt) | Directory enumeration with ffuf or gobuster | 163,210 bytes |
| `raft-small-words.txt` | [SecLists Discovery/Web-Content/raft-small-words.txt](https://github.com/danielmiessler/SecLists/blob/39166b57cfcc73afd87081cfb20bd317cdece6ff/Discovery/Web-Content/raft-small-words.txt) | General web word/path fuzzing | 348,619 bytes |
| `top-usernames-shortlist.txt` | [SecLists Usernames/top-usernames-shortlist.txt](https://github.com/danielmiessler/SecLists/blob/39166b57cfcc73afd87081cfb20bd317cdece6ff/Usernames/top-usernames-shortlist.txt) | Small username shortlist for authorized CTF exercises | 112 bytes |
| `rockyou.txt.tar.gz` | [SecLists Passwords/Leaked-Databases/rockyou.txt.tar.gz](https://github.com/danielmiessler/SecLists/blob/39166b57cfcc73afd87081cfb20bd317cdece6ff/Passwords/Leaked-Databases/rockyou.txt.tar.gz) | Common-password testing in authorized CTF labs; large compressed list | 53,291,283 bytes |

Upstream repository: https://github.com/danielmiessler/SecLists
Checked out commit: `39166b57cfcc73afd87081cfb20bd317cdece6ff` (shallow clone).
Each listed file is already included in that checkout; these links do not duplicate
the wordlist data. Check the links with `find -L wordlists -maxdepth 1 -type f -printf '%p %s bytes\\n'`.

Use only against systems where testing is authorized. For example:

```sh
ffuf -u https://AUTHORIZED-TARGET/FUZZ -w wordlists/common.txt
gobuster dir -u https://AUTHORIZED-TARGET -w wordlists/raft-small-directories.txt
```
