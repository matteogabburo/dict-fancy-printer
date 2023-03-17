# dict-pretty-printer
A simple library used to print python dictionaries in a fancier and understandable way 


## Install
To install from master branch just do:
```
pip install git+https://github.com/matteogabburo/dict-pretty-printer
```

If you want to install a specific development branch, use
```
pip install git+https://github.com/matteogabburo/dict-pretty-printer@<branch_name>
```

## Usage

### PrettyPrinter
- Example
```
from goburba.utils import PrettyPrinter
printer = PrettyPrinter()
print(printer(d))
```

### print_pretty_dict
- Example
```
from goburba.utils import print_pretty_dict
d = {"Hi": 1, "I":2, 3: "an", 4 : {"Matteo": 1, 2: "Gabburo"}}
print_pretty_dict(d)
```

### pretty_dict
- Example
```
from goburba.utils import pretty_dict
d = {"Hi": 1, "I":2, 3: "an", 4 : {"Matteo": 1, 2: "Gabburo"}}
d = pretty_dict(d)
print(d)
```