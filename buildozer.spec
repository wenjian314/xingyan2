[app]
# (str) Title of your application
title = 星言

# (str) Package name
package.name = xingyan

# (str) Package domain (needed for android/ios packaging)
package.domain = com.xingyan

# (str) Source directory (only one)
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,json,xlsx,md

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3==3.10.12,hostpython3==3.10.12,kivy==2.3.1,pypinyin==0.53.0,openpyxl==3.1.5

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) Application icon
icon.filename = icon.png

# (str) Presplash image
presplash.filename = icon.png

# (str) Presplash color (for android)
android.presplash_color = #1a1a2e

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (int) Target Android API level (for android)
android.api = 28

# (int) Minimum API level (for android)
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir (False)
android.private_storage = True

# (str) Android logcat filters
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a reference (True) or make a reference (False)
android.copy_libs = 1

# (str) The Android arch to build for (one of armeabi-v7a, arm64-v8a, x86, x86_64)
android.archs = arm64-v8a,armeabi-v7a

# (bool) Optimize Python bytecode before packaging (default False)
android.optimize_python = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug, 3 = verbose)
log_level = 2
p4a.branch = master

# (str) Path to build artifacts
build_dir = .buildozer

# (str) Path to output directory
bin_dir = bin

# (bool) Warn if user runs as root
warn_on_root = 1
