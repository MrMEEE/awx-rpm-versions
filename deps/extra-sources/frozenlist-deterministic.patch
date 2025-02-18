diff -uNr frozenlist-1.4.1/packaging/pep517_backend/_backend.py frozenlist-1.4.1-new/packaging/pep517_backend/_backend.py
--- frozenlist-1.4.1/packaging/pep517_backend/_backend.py	2023-12-15 05:14:12.000000000 +0100
+++ frozenlist-1.4.1-new/packaging/pep517_backend/_backend.py	2024-03-30 10:34:34.887986351 +0100
@@ -286,7 +286,7 @@
     """
     with maybe_prebuild_c_extensions(
             line_trace_cython_when_unset=False,
-            build_inplace=False,
+            build_inplace=True,
             config_settings=config_settings,
     ):
         return _setuptools_build_wheel(
