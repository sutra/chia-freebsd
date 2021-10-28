--- setup.py.orig	2021-10-27 02:31:39 UTC
+++ setup.py
@@ -1,36 +1,36 @@
 from setuptools import setup
 
 dependencies = [
-    "blspy==1.0.6",  # Signature library
-    "chiavdf==1.0.3",  # timelord and vdf verification
-    "chiabip158==1.0",  # bip158-style wallet filters
-    "chiapos==1.0.4",  # proof of space
-    "clvm==0.9.7",
-    "clvm_rs==0.1.14",
-    "clvm_tools==0.4.3",
-    "aiohttp==3.7.4",  # HTTP server for full node rpc
-    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
-    "bitstring==3.1.9",  # Binary data management library
-    "colorama==0.4.4",  # Colorizes terminal output
-    "colorlog==5.0.1",  # Adds color to logs
-    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
-    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
-    "fasteners==0.16.3",  # For interprocess file locking
-    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
-    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
+    "blspy>=1.0.6",  # Signature library
+    "chiavdf>=1.0.3",  # timelord and vdf verification
+    "chiabip158>=1.0",  # bip158-style wallet filters
+    "chiapos>=1.0.4",  # proof of space
+    "clvm>=0.9.7",
+    "clvm_rs>=0.1.14",
+    "clvm_tools>=0.4.3",
+    "aiohttp>=3.7.4",  # HTTP server for full node rpc
+    "aiosqlite>=0.17.0",  # asyncio wrapper for sqlite, to store blocks
+    "bitstring>=3.1.9",  # Binary data management library
+    "colorama>=0.4.4",  # Colorizes terminal output
+    "colorlog>=5.0.1",  # Adds color to logs
+    "concurrent-log-handler>=0.9.19",  # Concurrently log and rotate logs
+    "cryptography>=3.4.7",  # Python cryptography library for TLS - keyring conflict
+    "fasteners>=0.16.3",  # For interprocess file locking
+    "keyring>=23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
+    "keyrings.cryptfile>=1.3.4",  # Secure storage for keys on Linux (Will be replaced)
     #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
     #  See https://github.com/frispete/keyrings.cryptfile/issues/15
-    "PyYAML==5.4.1",  # Used for config file format
-    "setproctitle==1.2.2",  # Gives the chia processes readable names
-    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
-    "websockets==8.1.0",  # For use in wallet RPC and electron UI
-    "click==7.1.2",  # For the CLI
-    "dnspython==2.1.0",  # Query DNS seeds
-    "watchdog==2.1.3",  # Filesystem event watching - watches keyring.yaml
+    "PyYAML>=5.4.1",  # Used for config file format
+    "setproctitle>=1.2.2",  # Gives the chia processes readable names
+    "sortedcontainers>=2.4.0",  # For maintaining sorted mempools
+    "websockets>=8.1.0",  # For use in wallet RPC and electron UI
+    "click>=7.1.2",  # For the CLI
+    "dnspython>=2.1.0",  # Query DNS seeds
+    "watchdog>=2.1.3",  # Filesystem event watching - watches keyring.yaml
 ]
 
 upnp_dependencies = [
-    "miniupnpc==2.2.2",  # Allows users to open ports on their router
+    "miniupnpc>=2.2.2",  # Allows users to open ports on their router
 ]
 
 dev_dependencies = [
