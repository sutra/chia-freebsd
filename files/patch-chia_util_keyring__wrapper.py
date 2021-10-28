--- chia/util/keyring_wrapper.py.orig	2021-10-27 02:29:18 UTC
+++ chia/util/keyring_wrapper.py
@@ -34,9 +34,9 @@ def get_legacy_keyring_instance() -> Optional[LegacyKe
         return MacKeyring()
     elif platform == "win32" or platform == "cygwin":
         return WinKeyring()
-    elif platform == "linux":
+    elif platform == "linux" or platform.startswith("freebsd"):
         keyring: CryptFileKeyring = CryptFileKeyring()
-        keyring.keyring_key = "your keyring password"  # type: ignore
+        keyring.keyring_key = "your keyring password"  # type: ignore
         return keyring
     return None
 
