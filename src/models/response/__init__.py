"""
This code does the following:
  1. Finds all modules in the package
  2. Imports them using importlib
  3. Finds all classes defined in those modules
  4. Adds those classes to the package namespace
"""

from types import ModuleType
import pkgutil
import importlib
import inspect

for module in pkgutil.iter_modules(__path__):
    mod: ModuleType = importlib.import_module(f"{__name__}.{module.name}")

    for name, obj in inspect.getmembers(mod, inspect.isclass):
        if obj.__module__ == mod.__name__:
            globals()[name] = obj