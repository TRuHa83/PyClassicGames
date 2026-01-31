# -*- mode: python ; coding: utf-8 -*-
import sys


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('data', 'data'), ('assets', 'assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

# FIX LINUX: Eliminar librerías de sistema (GLib, Gio) del paquete.
if sys.platform.startswith('linux'):
    sys_libs = ['libglib', 'libgio', 'libgobject', 'libgthread']
    a.binaries = [x for x in a.binaries if not any(lib in x[0] for lib in sys_libs)]

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PyClassicGames',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='PyClassicGames',
)