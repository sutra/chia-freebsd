--- chia/util/keyring_wrapper.py.orig	2022-03-15 02:48:42 UTC
+++ chia/util/keyring_wrapper.py
@@ -34,9 +34,9 @@ def get_legacy_keyring_instance() -> Optional[LegacyKe
         return MacKeyring()
     elif platform == "win32" or platform == "cygwin":
         return WinKeyring()
-    elif platform == "linux":
+    elif platform == "linux" or platform.startswith("freebsd"):
         keyring: CryptFileKeyring = CryptFileKeyring()
-        keyring.keyring_key = "your keyring password"
+        keyring.keyring_key = "your keyring password"
         return keyring
     return None
 
