import re
if 'pyarrow' in sys.modules.keys():
  pyarrow_version = sys.modules['pyarrow'].__version__
  f = re.search("0.15.+", pyarrow_version)
  if f == None:
    for key in list(sys.modules.keys()):
      if key.startswith('pyarrow'):
        del sys.modules[key]
    print(f"unloaded pyarrow {pyarrow_version}")
    import pyarrow
    pyarrow_version = sys.modules['pyarrow'].__version__
    print(f"loaded pyarrow {pyarrow_version}")
    del(pyarrow_version)

  else: 
    print(f"You're running pyarrow {pyarrow_version} and are good to go!")