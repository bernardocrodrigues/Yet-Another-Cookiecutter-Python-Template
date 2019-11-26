
import os
import sys
import pytest
from mock import Mock, PropertyMock
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
import {{cookiecutter.module_name}}


def test_{{cookiecutter.module_name}}():

    {{cookiecutter.module_name}}.main()