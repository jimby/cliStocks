import importlib, importlib.util

def module_directory(name_module, path):
    p =  importlib.util.spec_from_file_location(name_module, path)
    import_module = importlib.util.module_from_spec(p)
    p.loader.exec_module(import_module)
    return import_module

    result = module_directory("result", "../Modules/test1.py")

    print(result.sub(3,2))
    print(result.lower_case('SaFa'))
