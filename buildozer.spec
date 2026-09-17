[app]
title = 星言
package.name = xingyan
package.domain = com.xingyan
source.dir = .
source.include_exts = py,png,jpg,kv,json,xlsx,md
version = 1.0.0
# ✅ 不写 hostpython3，Python 3.11
requirements = python3==3.11,kivy==2.3.1,pypinyin==0.53.0,openpyxl==3.1.5
orientation = portrait
icon.filename = icon.png
presplash.filename = icon.png
android.presplash_color = #1a1a2e
fullscreen = 0
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# ✅ 关键：目标 API 28（对应 Android 9），避免 35 的 Gradle 冲突
android.api = 28
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.private_storage = True
android.logcat_filters = *:S python:D
android.copy_libs = 1
android.archs = arm64-v8a
android.optimize_python = True

# ✅ 新写法（消除 deprecated 警告）
p4a.bootstrap = sdl2

# ✅ 强制 Gradle 7.5.1（避开 8.x + targetSdk 35 的坑）
android.gradle_version = 7.5.1
android.gradle_dependencies = 
android.enable_androidx = True

[buildozer]
log_level = 2
# ✅ 强制 stable（防止被 master 覆盖）
p4a.branch = stable
build_dir = .buildozer
bin_dir = bin
warn_on_root = 1
