# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from PyInstaller.utils.hooks import collect_all

# 获取当前 Python 环境的 site-packages 路径
site_packages = None
for path in sys.path:
    if 'site-packages' in path:
        site_packages = path
        break
if site_packages is None:
    raise RuntimeError("Cannot find site-packages directory")

print(f"Using site-packages: {site_packages}")

# ======================= 正确收集模型文件的函数 =======================
def collect_models(root_dir,des_dir):
    models = []
    for root, _, files in os.walk(root_dir):
        rel_path = os.path.relpath(root, root_dir)
        for file in files:
            src_file = os.path.join(root, file)
            dest_dir = os.path.join(des_dir, rel_path)
            models.append( (src_file, dest_dir) )
    return models

datas = []
binaries = []
hiddenimports = []

tmp_ret = collect_all('requests')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('zeroconf')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('openvr')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('translators')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('wsgiref.simple_server')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('engineio. async_eventlet')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

packageList=["exejs","translators","niquests","urllib3_future","wassima","pathos","ppft","dill","cryptography","py7zr","multivolumefile","bcj","inflate64","pyppmd","pyzstd","Cryptodome","webview","proxy_tools","pythonnet","pythonnet-3.0.5.dist-info",'clr_loader','flask_socketio','socketio','engineio','bidict','simple_websocket','wsproto','opuslib']
for i in packageList: 
    # 使用动态路径
    datas+=collect_models(os.path.join(site_packages, i), i)

datas.append(('templates','templates'))
datas.append(('ffmpeg/bin/*', 'ffmpeg/bin'))
datas.append(('opusdll/*', 'opusdll'))
datas.append(('font/*', 'font'))

# 使用动态路径
datas.append((os.path.join(site_packages, 'miniaudio.py'), '.'))
datas.append((os.path.join(site_packages, 'clr.py'), '.'))
datas.append((os. path.join(site_packages, 'bottle.py'), '.'))
binaries.append((os. path.join(site_packages, '_miniaudio.pyd'), '.'))

#hiddenimports.append('engineio.async_drivers.eventlet')
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt5'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='VRCLS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=True, 
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='VRCLS',
)
