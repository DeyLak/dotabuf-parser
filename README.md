# Deploying and using on windows

1. Install latest python(3.6) version from <https://www.python.org/downloads/>
1. Download the last file from <http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml> (lxml‑3.7.3‑cp36‑cp36m‑win_amd64.whl)
1. Put it to the root of the repository (Same place, as README file)
1. Run install_dependencies.bat
1. Create file input.txt in the root directory, it should contain team's names each one on new line
1. Open command line window in this folder(shift + right click in Explorer -> select Open command line window here option)
1. Run `python index.py` Parsed teams can be found in output.txt file