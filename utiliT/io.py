from yaml import load
from yaml import SafeLoader
from pathlib import Path
import json
import pickle
import toml


class ConfigHelper(dict):

    def __init__(self) -> None:
        pass

    def load_dict(self, dictionary: dict):
        self.__dict__.update(**dictionary)
        self.update(dictionary)

    def load_yaml(self, yaml_: str):
        if Path(yaml_).suffix != '.yaml' and Path(yaml_).suffix != '.yml':
            raise ValueError('Input File not a .yaml File')
        with open(yaml_) as f:
            data = load(f, Loader=SafeLoader)
        self.load_dict(data)

    def load_json(self, json_: str, json_string=False):
        if json_string:
            data = json.loads(json_)
        else:
            if Path(json_).suffix != '.json':
                raise ValueError('Input File not a .json File')
            with open(json_) as f:
                data = json.load(f)
        self.load_dict(data)

    def load_toml(self, toml_: str, toml_string=False):
        if toml_string:
            data = toml.loads(toml_)
        else:
            if Path(toml).suffix != '.toml':
                raise ValueError('Input File not a .json File')
            with open(toml_) as f:
                data = toml.load(f)
        self.load_dict(data)


def pickle_reader(file_name):
    if Path(file_name).suffix != '.pickle':
        raise ValueError('File Name not a .pickle File')
    with open(file_name, 'rb') as f:
        data = pickle.load(f)
    return data


def pickle_writer(file_name, object):
    if Path(file_name).suffix != '.pickle':
        raise ValueError('File Name not a .pickle File')
    with open(file_name, 'wb') as f:
        pickle.dump(object, f)


def read_txt(file_name, single_string=False):
    with open(file_name) as f:
        lines = f.readlines()
    if single_string:
        return ' '.join(lines)
    return lines


def read_json(json_, json_string=False):
    if json_string:
        data = json.loads(json_)
    else:
        if Path(json_).suffix != '.json':
            raise ValueError('Input File not a .json File')
        with open(json_) as f:
            data = json.load(f)
    return data


def read_yaml(yaml_):
    if Path(yaml_).suffix != '.yaml' and Path(yaml_).suffix != '.yml':
        raise ValueError('Input File not a .yaml File')
    with open(yaml_) as f:
        data = load(f, Loader=SafeLoader)
    return data


def load_toml(toml_: str, toml_string=False):
    if toml_string:
        data = toml.loads(toml_)
    else:
        if Path(toml).suffix != '.toml':
            raise ValueError('Input File not a .json File')
        with open(toml_) as f:
            data = toml.load(f)
    return data