'''
    Configuração dos elementos exportados desse modulo. Inclua qualquer classe função ou exception relevante.
    Ex:
        from .core import Arbiter
        from .elements import Module, Element
        from .exceptions import Host_not_responding, Auto_revive_enabled

    Não use wild cards!
        from .core import *

    Inclua na lista __all__ os mesmos modulos exportados
    Ex:
    __all__ = ['Arbiter', 'Module', 'Element',
           'Host_not_responding', 'Auto_revive_enabled']
'''

from .main import round, actual_round

__all__ = ['round','actual_round']
