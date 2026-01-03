# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:/Kaigo AI/GUI.py'],
    pathex=[],
    binaries=[],
    datas=[('D:/Kaigo AI/Output', 'Output'), ('D:/Kaigo AI/Misc', 'Misc'), ('D:/Kaigo AI/Misc/background.jpg', 'Misc')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\Kaigo AI\\Misc\\Icon.ico'],
)
