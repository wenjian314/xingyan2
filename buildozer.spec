[app]
title = 星言
package.name = xingyan
package.domain = com.xingyan
source.dir = .
source.include_exts = py,png,jpg,kv,json,xlsx,md
version = 1.0.0
requirements = python3==3.11,kivy==2.3.1,pypinyin==0.53.0,openpyxl==3.1.5
orientation = portrait
icon.filename = icon.png
presplash.filename = icon.png
android.presplash_color = #1a1a2e
fullscreen = 0
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 28
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.private_storage = True
android.logcat_filters = *:S python:D
android.copy_libs = 1
android.archs = arm64-v8a
android.optimize_python = True

# ⭐ 用 p4a.bootstrap（新写法，不报 deprecated 警告）
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
p4a.branch = stable
build_dir = .buildozer
bin_dir = bin
warn_on_root = 1
