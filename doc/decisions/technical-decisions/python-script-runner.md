# python script runner

**Status**: WIP + RFC + adopting now for pragmatic trial/pilot/PoC

**Date**: 2025-03-31

**Governance**: To Be Discovered; potentially a combo of this repo participants, DHCW CISO, NHS Wales UCB peers, etc.

## Situation - Context and Problem Statement

Generally we are aiming for software engineering to use the python programming language for many needs, such as general purpose scripting, system administration, test automation, AI/ML interconnection, etc.

Specifically we are aiming to make it fast and easy for python programmers to run python scripts that are standalone and as self-supporting as reasonably possible. For example this means a typical one-file python script that can download its own dependencies, create its own virtual environments, and run itself from the command line.

## Background - Decision Drivers

Python has a long history of many ways to launch it that are incompatible, many kinds of dependency management that are incompatible, and many kinds of virtual environment managers that are incompatible. As far as we know, there is no perfect way to write a standalone self-supporting python script.

Therefore we aim to get as close as reasonably possible, using good modern tooling and good modern practices. We're willing to accept some up-front setup, such as ensuring that a system already has a current runtime python and current runtime manager.

Scope:

* In scope: single-file python scripts (or a small set of files that are python scripts and any related files such as assets) that don't use a python package manager.
  
* Out of scope: any larger-scale python projects, such as multi-file python scripts that already have a requirements.txt file, or a python package that's deployable with pip, or a python notebook such as in Jupyter, or a python web app such as with Django, etc.

Background reading:

* [Self-contained python scripts with uv](https://blog.dusktreader.dev/2025/03/29/self-contained-python-scripts-with-uv/)

* [Self-contained python scripts with uv - discussion on Hacker News](https://news.ycombinator.com/item?id=43519669))
  
* [Python specifications: inline script metadata](https://packaging.python.org/en/latest/specifications/inline-script-metadata/)

### Givens

At previous clients, Joel evaluated `pip`, `pipx`, `poetry`, `uv`, by trying them in real use on real projects that had significant needs such as for AI, cloud services, and test automation. Joel chose uv because it provides more-reliable dependency version management, more-batteries-included capabilities, and much faster speed; Digital Health and Care Wales could do a separate architecture decision record for choosing uv, if there's anyone that feels that there's a better choice or a strong need to consider other choices.

"The whole point of uv is to solve the nightmare that is running a script with the right version of python with the right dependencies. "Just use the system python" gets you right back to the start such as, oh no! It didn't parse because it used python 3.11 features and I'm still on 3.6."

## Assessment - Considered Options

Options so far:

* uv with inline script metadata

* uv execute runner

* nuitka compiler

### Option: uv with inline script metadata

To launch a python script that's as self-supporting as reasonable possible, use this the code, as described in the link above:

File `example.py`:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "alfa>=1", 
#   "bravo>=2", 
#   "charlie>=3",
# ]
# ///
import alfa
import bravo
import charlie
```

Change to be executable:

```sh
chmod +x example.py
```

Run:

```sh
./example.py
```

Caveats thanks to [discussion](https://news.ycombinator.com/item?id=43519669):

* The script requires uv to already be installed. Arguably you could make it a shell script that checks if uv is already installed and then installs it via curlpipe if not... but that's quite a bit of extra boilerplate and the curlpipe pattern is bad. … Installing uv will become less of an issue as package managers include uv in their repositories. For example, uv is already available in Alpine Linux and Homebrew:
[https://repology.org/project/uv/versions](https://repology.org/project/uv/versions).

* Inline script metadata is a Python standard. When there is no uv on the system and uv isn't packaged but you have the right version of Python for the script, you can run the script with pipx:
[https://pipx.pypa.io/stable/examples/#pipx-run-examples](https://pipx.pypa.io/stable/examples/#pipx-run-examples). pipx is much more widely packaged:
[https://repology.org/project/pipx/versions](https://repology.org/project/pipx/versions).

* Auto-creating a venv somewhere in your home directory is not really self-contained. If you run the script as a one-off and then delete it, that venv is still there, taking up space. I can't find any assertion in the uv docs that these temporary virtual environments are ever automatically cleaned up.

* This technique doesn't change the semantics of the code itself, it just changes the environment in which the code runs. In that respect it is no different from a `#!/bin/bash` comment at the top of a shell script.

* The showstopper for us is our SCA vulnerability scanner doesn't work with uv yet. You can add an intermediate sca stage that exports the uv dependencies as requirements.txt.

* Windows doesn't support shebang lines as you probably know, but if you associate uv with .py files you'll get the same result. I think it should be something like this: `ftype Python.File=C:\Path\to\uv.exe run %L %*`. If you don't use the CPython installer the Python.File file type might not be defined, so you might need to set that with `assoc` first: `assoc .py=Python.File`.

### Option: uv execute runner

From [discussion](https://news.ycombinator.com/item?id=43519669):

I have my own uv execute script:

File `uve`:

```bash
#!/bin/bash
temp=$(mktemp)
trap 'unlink $temp' EXIT
uv export --script $1 --no-hashes > $temp
uv run --with-requirements $temp vim $1
```

### Option: nuitka compiler

From [discussion](https://news.ycombinator.com/item?id=43519669).

For those who want a really self-contained Python script, I'd like to point out the Nuitka compiler.

I've been using it in production for my gRPC services with no issues whatsoever - just "nuitka --onefile run.py" and that's it. It Just Werks.

Since it's a compiler, the resulting binary is even faster than the original Python program would be if it were bundled via Pyinstaller.

[https://nuitka.net/](https://nuitka.net/)

[https://github.com/kayhayen](https://github.com/kayhayen)

## Recommendation - Decision Outcome

Adopt.

Revisit periodically, such as when there are new capabilities for `uv`, or new launching options for `python`, or new defaults for busybox or Alpine.

Cautions thanks to the original article:

* Be aware the virtual environment is not created/resolved before running. This means that you won't get linting/autocomplete properly for the environment.

* Be aware that the `-S` flag depends on coreutils env, which isn't available by default on some systems, such as the busybox env that you get when using default Alpine. One workaround is to install GNU `coreutils` in your container, or to install `uutils-coreutils` for a more lightweight implementation in Rust.
