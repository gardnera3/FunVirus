# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Virus.py'],
    pathex=[],
    binaries=[],
    datas=[('Assets', 'Assets')],
    hiddenimports=['FUNctionalities.stewietest', 'FUNctionalities.BSOD', 'FUNctionalities.UpdateScreen', 'FUNctionalities.notifications', 'FUNctionalities.plays_sounds', 'FUNctionalities.audio', 'FUNctionalities.youtube', 'FUNctionalities.rotate'],
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
    name='Free_Vbucks_Generator_V2',
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
    icon=['Assets\\exeicon.png'],
)
