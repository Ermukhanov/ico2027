#!/usr/bin/env python3
print("Vulnerable pattern: SHA256(secret || message).")
print("Checklist: message -> digest -> secret-length guess -> glue padding -> continue hash.")
print("Safe construction: HMAC-SHA256(secret, message).")
