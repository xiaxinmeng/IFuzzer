
import os

executable= 'D:\\VS2022\\VC\\Tools\\MSVC\\14.30.30705\\bin\\HostX86\\x64\\link.exe'

cmd310 = ["/LIBPATH:D:\\python310\\lib\\site-packages\\torch\\lib", "/LIBPATH:D:\\python310\\libs", "/LIBPATH:D:\\python310\\PCbuild\\amd64", "/LIBPATH:D:\\VS2019\\VC\\Tools\\MSVC\\14.29.30133\\ATLMFC\\lib\\x64", "/LIBPATH:D:\\VS2019\\VC\\Tools\\MSVC\\14.29.30133\\lib\\x64", "/LIBPATH:C:\\Program Files (x86)\\Windows Kits\\NETFXSDK\\4.8\\lib\\um\\x64", "/LIBPATH:C:\\Program Files (x86)\\Windows Kits\\10\\lib\\10.0.19041.0\\ucrt\\x64", "/LIBPATH:C:\\Program Files (x86)\\Windows Kits\\10\\lib\\10.0.19041.0\\um\\x64", "/LIBPATH:D:\\VS2019\\VC\\Tools\\MSVC\\14.29.30133\\lib\\x64", "/LIBPATH:D:\\VS2019\\VC\\Tools\\MSVC\\14.29.30133\\atlmfc\\lib\\x64", "/LIBPATH:D:\\VS2019\\VC\\Auxiliary\\VS\\lib\\x64", "/LIBPATH:C:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.19041.0\\ucrt\\x64", "/LIBPATH:C:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.19041.0\\ucrt_enclave\\x64", "/LIBPATH:C:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.19041.0\\um\\x64", "/LIBPATH:C:\\Program Files (x86)\\Windows Kits\\NETFXSDK\\4.8\\lib\\um\\x64", "/LIBPATH:D:\\python310\\libs", "c10.lib", "torch.lib", "torch_cpu.lib", "torch_python.lib"]
rc = os.spawnv(os.P_WAIT, executable, cmd310)
