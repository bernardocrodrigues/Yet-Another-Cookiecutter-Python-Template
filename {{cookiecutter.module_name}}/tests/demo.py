
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
import {{cookiecutter.module_name}}


{{cookiecutter.module_name}}.main()