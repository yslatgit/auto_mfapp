import yaml
import os


#
def read_yaml(name,moudle,conf_yaml_path):
    os.chdir(conf_yaml_path)
    y = yaml.load(open(name, 'r', encoding="utf-8"))
    y = y[moudle]
    return y




if __name__ == '__main__':
   print(read_yaml("conf.yaml","smartisan"))