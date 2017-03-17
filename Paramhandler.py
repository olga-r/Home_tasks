from abc import ABCMeta, abstractmethod
import json
import pickle
import os.path


class ParamHandler(metaclass=ABCMeta):
    types = {}
    """
    Кирилл, подскажите, пожалуйста, как задать значения этого словаря вручную.
    Не получается сделать ссылку на дочерний класс
    """
    
    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(
                'Class "{}" is not ParamHandler!'.format(klass)
            )

        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)
        if klass is None:
            raise ParamHandlerException(
                'Type "{}" not found!'.format(ext)
            )

        return klass(source, *args, **kwargs)

        
class PyParamHandler(ParamHandler):
    def read(self):
        """
        Чтение из pickle файла и присвоение значений в self.params
        """
        with open(self.source, 'rb') as inp:
            self.params = pickle.load(inp)

    def write(self):
        """
        Запись в pickle файл параметров self.params
        """
        with open(self.source, 'wb') as out:
            pickle.dump(self.params, out)

class JsonParamHandler(ParamHandler):
    def read(self):
        """
        Чтение в формате JSON и присвоение значений в self.params
        """
        with open(self.source) as inp:
            self.params = json.load(inp)

    def write(self):
        """
        Запись в формате JSON параметров self.params
        """
        with open(self.source, 'w') as out:
            json.dump(self.params, out)
    
class ParamHandlerException(BaseException):
    pass

ParamHandler.add_type('json', JsonParamHandler)
ParamHandler.add_type('pickle', PyParamHandler)
for k, v in ParamHandler.types.items():
    print(k, v)
filename = ParamHandler.get_instance('./users.json')
filename.read()
for k, v in filename.params.items():
    print(k, v)

filename = ParamHandler.get_instance('./users.pickle')
filename.read()
for k, v in filename.params.items():
    print(k, v)