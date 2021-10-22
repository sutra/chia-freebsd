--- chia/util/keyring_wrapper.py.orig	2021-10-10 04:37:15 UTC
+++ chia/util/keyring_wrapper.py
@@ -119,12 +119,12 @@ class KeyringWrapper:
             else:
                 keyring = MacKeyring()  # type: ignore
                 keyring_main.set_keyring(keyring)
-        elif platform == "linux":
+        elif platform == "linux" or platform.startswith("freebsd"):
             if supports_keyring_passphrase():
                 keyring = FileKeyring(keys_root_path=self.keys_root_path)  # type: ignore
             else:
                 keyring = CryptFileKeyring()
-                keyring.keyring_key = "your keyring password"  # type: ignore
+                keyring.keyring_key = "your keyring password"  # type: ignore
         else:
             keyring = keyring_main
 
@@ -134,11 +134,11 @@ class KeyringWrapper:
         # If keyring.yaml isn't found or is empty, check if we're using CryptFileKeyring or the Mac Keychain
         filekeyring = self.keyring if type(self.keyring) == FileKeyring else None
         if filekeyring and not filekeyring.has_content():
-            if platform == "linux":
+            if platform == "linux" or platform.startswith("freebsd"):
                 old_keyring = CryptFileKeyring()
                 if Path(old_keyring.file_path).is_file():
                     # After migrating content from legacy_keyring, we'll prompt to clear those keys
-                    old_keyring.keyring_key = "your keyring password"  # type: ignore
+                    old_keyring.keyring_key = "your keyring password"  # type: ignore
                     return old_keyring
             elif platform == "darwin":
                 mac_keychain: MacKeyring = MacKeyring()
