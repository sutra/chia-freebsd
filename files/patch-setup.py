--- setup.py.orig	2022-07-05 13:28:45 UTC
+++ setup.py
@@ -1,43 +1,43 @@
 from setuptools import setup
 
 dependencies = [
-    "aiofiles==0.7.0",  # Async IO for files
-    "blspy==1.0.13",  # Signature library
-    "chiavdf==1.0.6",  # timelord and vdf verification
-    "chiabip158==1.1",  # bip158-style wallet filters
-    "chiapos==1.0.10",  # proof of space
-    "clvm==0.9.7",
-    "clvm_tools==0.4.4",  # Currying, Program.to, other conveniences
-    "chia_rs==0.1.2",
-    "clvm-tools-rs==0.1.9",  # Rust implementation of clvm_tools
-    "aiohttp==3.8.1",  # HTTP server for full node rpc
-    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
-    "bitstring==3.1.9",  # Binary data management library
-    "colorama==0.4.4",  # Colorizes terminal output
-    "colorlog==6.6.0",  # Adds color to logs
-    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
-    "cryptography==36.0.2",  # Python cryptography library for TLS - keyring conflict
-    "fasteners==0.16.3",  # For interprocess file locking, expected to be replaced by filelock
-    "filelock==3.4.2",  # For reading and writing config multiprocess and multithread safely  (non-reentrant locks)
-    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
-    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
+    "aiofiles>=0.7.0",  # Async IO for files
+    "blspy>=1.0.13",  # Signature library
+    "chiavdf>=1.0.6",  # timelord and vdf verification
+    "chiabip158>=1.1",  # bip158-style wallet filters
+    "chiapos>=1.0.10",  # proof of space
+    "clvm>=0.9.7",
+    "clvm_tools>=0.4.4",  # Currying, Program.to, other conveniences
+    "chia_rs>=0.1.2",
+    "clvm-tools-rs>=0.1.9",  # Rust implementation of clvm_tools
+    "aiohttp>=3.8.1",  # HTTP server for full node rpc
+    "aiosqlite>=0.17.0",  # asyncio wrapper for sqlite, to store blocks
+    "bitstring>=3.1.9",  # Binary data management library
+    "colorama>=0.4.4",  # Colorizes terminal output
+    "colorlog>=6.6.0",  # Adds color to logs
+    "concurrent-log-handler>=0.9.19",  # Concurrently log and rotate logs
+    "cryptography>=36.0.2",  # Python cryptography library for TLS - keyring conflict
+    "fasteners>=0.16.3",  # For interprocess file locking, expected to be replaced by filelock
+    "filelock>=3.4.2",  # For reading and writing config multiprocess and multithread safely  (non-reentrant locks)
+    "keyring>=23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
+    "keyrings.cryptfile>=1.3.4",  # Secure storage for keys on Linux (Will be replaced)
     #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
     #  See https://github.com/frispete/keyrings.cryptfile/issues/15
-    "PyYAML==6.0",  # Used for config file format
-    "setproctitle==1.2.3",  # Gives the chia processes readable names
-    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
+    "PyYAML>=6.0",  # Used for config file format
+    "setproctitle>=1.2.3",  # Gives the chia processes readable names
+    "sortedcontainers>=2.4.0",  # For maintaining sorted mempools
     # TODO: when moving to click 8 remove the pinning of black noted below
-    "click==7.1.2",  # For the CLI
-    "dnspythonchia==2.2.0",  # Query DNS seeds
-    "watchdog==2.1.7",  # Filesystem event watching - watches keyring.yaml
-    "dnslib==0.9.17",  # dns lib
-    "typing-extensions==4.0.1",  # typing backports like Protocol and TypedDict
-    "zstd==1.5.0.4",
-    "packaging==21.0",
+    "click>=7.1.2",  # For the CLI
+    "dnspythonchia>=2.2.0",  # Query DNS seeds
+    "watchdog>=2.1.7",  # Filesystem event watching - watches keyring.yaml
+    "dnslib>=0.9.17",  # dns lib
+    "typing-extensions>=4.0.1",  # typing backports like Protocol and TypedDict
+    "zstd>=1.5.0.4",
+    "packaging>=21.0",
 ]
 
 upnp_dependencies = [
-    "miniupnpc==2.2.2",  # Allows users to open ports on their router
+    "miniupnpc>=2.2.2",  # Allows users to open ports on their router
 ]
 
 dev_dependencies = [
