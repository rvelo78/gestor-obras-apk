[app]
title = Gestor de Obras RV
package.name = gestorobras
package.domain = com.rv.gestor
source.dir = .
version = 1.0
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 1

[android]
api = 30
minapi = 21
sdk = 30
ndk = 23b
accept_sdk_license = True
archs = arm64-v8a
permissions = INTERNET,WRITE_EXTERNAL_STORAGE