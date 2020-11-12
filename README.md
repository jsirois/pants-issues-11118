A/: run and test work
---------------------
+ `python_library()`
+ `pex_binary` no sources, entry_point, explicit dependencies on `python_library`

```
$ ./pants run path/to/package/src/package:main
Package(version='42')
```

+ `python_tests()`

```
$ ./pants test path/to/package/test

✓ path/to/package/test/test_package.py succeeded.
```

```
$ ./pants test path/to/package/test/test_package.py 

✓ path/to/package/test/test_package.py succeeded.
```

B/: run and test work
---------------------
+ `python_library` sources for all except `pex_binary` sources
+ `pex_binary` sources
+ `python_tests()`

Same run and test successes a A.

C/: run fails, test fails
-------------------------
+ `pex_binary` sources

```
$ ./pants run path/to/package/src/package:main
16:07:00.65 [INFO] initializing pantsd...
16:07:01.19 [INFO] pantsd initialized.
Traceback (most recent call last):
  File "/home/jsirois/Documents/toolchain-labs/issues/11118/c/.pants.d/tmpure1pomm/main.pex/.bootstrap/pex/pex.py", line 443, in execute
  File "/home/jsirois/Documents/toolchain-labs/issues/11118/c/.pants.d/tmpure1pomm/main.pex/.bootstrap/pex/pex.py", line 375, in _wrap_coverage
  File "/home/jsirois/Documents/toolchain-labs/issues/11118/c/.pants.d/tmpure1pomm/main.pex/.bootstrap/pex/pex.py", line 406, in _wrap_profiling
  File "/home/jsirois/Documents/toolchain-labs/issues/11118/c/.pants.d/tmpure1pomm/main.pex/.bootstrap/pex/pex.py", line 494, in _execute
  File "/home/jsirois/Documents/toolchain-labs/issues/11118/c/.pants.d/tmpure1pomm/main.pex/.bootstrap/pex/pex.py", line 596, in execute_entry
  File "/home/jsirois/Documents/toolchain-labs/issues/11118/c/.pants.d/tmpure1pomm/main.pex/.bootstrap/pex/pex.py", line 604, in execute_module
  File "/usr/lib/python3.6/runpy.py", line 208, in run_module
    return _run_code(code, {}, init_globals, run_name, mod_spec)
  File "/usr/lib/python3.6/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/home/jsirois/Documents/toolchain-labs/issues/11118/c/.pants.d/tmpure1pomm/path/to/package/src/package/package.py", line 3, in <module>
    from ._version import ___version___ as version
ModuleNotFoundError: No module named 'package._version'
```

+ `python_tests()`

```
$ ./pants test path/to/package/test
16:17:24.16 [WARN] Completed: Run tests - path/to/package/test/test_package.py failed (exit code 2).
============================= test session starts ==============================
platform linux -- Python 3.6.12, pytest-6.0.2, py-1.9.0, pluggy-0.13.1 -- /usr/bin/python3.6
cachedir: .pytest_cache
rootdir: /tmp/process-execution81sbb2
plugins: cov-2.10.1
collecting ... collected 0 items / 1 error

==================================== ERRORS ====================================
____________ ERROR collecting path/to/package/test/test_package.py _____________
ImportError while importing test module '/tmp/process-execution81sbb2/path/to/package/test/test_package.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/home/jsirois/.cache/pants/named_caches/pex_root/installed_wheels/80c6a3b6446950ab184d83f405467154af4c5277/pytest-6.0.2-py3-none-any.whl/_pytest/python.py:552: in _importtestmodule
    mod = import_path(self.fspath, mode=importmode)
/home/jsirois/.cache/pants/named_caches/pex_root/installed_wheels/80c6a3b6446950ab184d83f405467154af4c5277/pytest-6.0.2-py3-none-any.whl/_pytest/pathlib.py:520: in import_path
    importlib.import_module(module_name)
/usr/lib/python3.6/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:994: in _gcd_import
    ???
<frozen importlib._bootstrap>:971: in _find_and_load
    ???
<frozen importlib._bootstrap>:955: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:665: in _load_unlocked
    ???
/home/jsirois/.cache/pants/named_caches/pex_root/installed_wheels/80c6a3b6446950ab184d83f405467154af4c5277/pytest-6.0.2-py3-none-any.whl/_pytest/assertion/rewrite.py:170: in exec_module
    exec(co, module.__dict__)
path/to/package/test/test_package.py:1: in <module>
    from package.package import Package
path/to/package/src/package/package.py:3: in <module>
    from ._version import ___version___ as version
E   ModuleNotFoundError: No module named 'package._version'
=========================== short test summary info ============================
ERROR path/to/package/test/test_package.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================


𐄂 path/to/package/test/test_package.py failed.
```

D/: run works, test fails
-------------------------
+ `python_library()`
+ `pex_binary` no sources, entry_point, explicit dependencies on `python_library`

Same run success a A.

```
$ ./pants test path/to/package/test/test_package.py 
16:18:14.15 [ERROR] Exception caught: (pants.engine.internals.scheduler.ExecutionError)
  File "/home/jsirois/.cache/pants/setup/bootstrap-Linux-x86_64/2.0.0_py36/lib/python3.6/site-packages/pants/bin/local_pants_runner.py", line 289, in run
    engine_result = self._run_v2()
  File "/home/jsirois/.cache/pants/setup/bootstrap-Linux-x86_64/2.0.0_py36/lib/python3.6/site-packages/pants/bin/local_pants_runner.py", line 195, in _run_v2
    return self._maybe_run_v2_body(goals, poll=False)
  File "/home/jsirois/.cache/pants/setup/bootstrap-Linux-x86_64/2.0.0_py36/lib/python3.6/site-packages/pants/bin/local_pants_runner.py", line 217, in _maybe_run_v2_body
    poll_delay=(0.1 if poll else None),
  File "/home/jsirois/.cache/pants/setup/bootstrap-Linux-x86_64/2.0.0_py36/lib/python3.6/site-packages/pants/init/engine_initializer.py", line 127, in run_goal_rules
    goal_product, params, poll=poll, poll_delay=poll_delay
  File "/home/jsirois/.cache/pants/setup/bootstrap-Linux-x86_64/2.0.0_py36/lib/python3.6/site-packages/pants/engine/internals/scheduler.py", line 569, in run_goal_rule
    self._raise_on_error([t for _, t in throws])
  File "/home/jsirois/.cache/pants/setup/bootstrap-Linux-x86_64/2.0.0_py36/lib/python3.6/site-packages/pants/engine/internals/scheduler.py", line 539, in _raise_on_error
    wrapped_exceptions=tuple(t.exc for t in throws),

Exception message: 1 Exception encountered:

  ResolveError: No owning targets could be found for the file `path/to/package/test/test_package.py`.

Please check that there is a BUILD file in `path/to/package/test` with a target whose `sources` field includes `path/to/package/test/test_package.py`. See https://www.pantsbuild.org/docs/targets for more information on target definitions.
If you would like to ignore un-owned files, please pass `--owners-not-found-behavior=ignore`.


(Use --print-stacktrace to see more error details.)
```

E/: run works, test fails
-------------------------
+ `python_library()`
+ `pex_binary` sources

Same run success a A.

+ `python_tests()`

```
$ ./pants test path/to/package/test
16:04:25.19 [WARN] Completed: Run tests - path/to/package/test/test_package.py failed (exit code 2).
============================= test session starts ==============================
platform linux -- Python 3.6.12, pytest-6.0.2, py-1.9.0, pluggy-0.13.1 -- /usr/bin/python3.6
cachedir: .pytest_cache
rootdir: /tmp/process-executionOUo4x5
plugins: cov-2.10.1
collecting ... collected 0 items / 1 error

==================================== ERRORS ====================================
____________ ERROR collecting path/to/package/test/test_package.py _____________
ImportError while importing test module '/tmp/process-executionOUo4x5/path/to/package/test/test_package.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/home/jsirois/.cache/pants/named_caches/pex_root/installed_wheels/80c6a3b6446950ab184d83f405467154af4c5277/pytest-6.0.2-py3-none-any.whl/_pytest/python.py:552: in _importtestmodule
    mod = import_path(self.fspath, mode=importmode)
/home/jsirois/.cache/pants/named_caches/pex_root/installed_wheels/80c6a3b6446950ab184d83f405467154af4c5277/pytest-6.0.2-py3-none-any.whl/_pytest/pathlib.py:520: in import_path
    importlib.import_module(module_name)
/usr/lib/python3.6/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:994: in _gcd_import
    ???
<frozen importlib._bootstrap>:971: in _find_and_load
    ???
<frozen importlib._bootstrap>:955: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:665: in _load_unlocked
    ???
/home/jsirois/.cache/pants/named_caches/pex_root/installed_wheels/80c6a3b6446950ab184d83f405467154af4c5277/pytest-6.0.2-py3-none-any.whl/_pytest/assertion/rewrite.py:170: in exec_module
    exec(co, module.__dict__)
path/to/package/test/test_package.py:1: in <module>
    from package.package import Package
E   ModuleNotFoundError: No module named 'package'
=========================== short test summary info ============================
ERROR path/to/package/test/test_package.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================


𐄂 path/to/package/test/test_package.py failed.
```
