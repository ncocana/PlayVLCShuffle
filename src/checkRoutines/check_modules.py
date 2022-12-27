def check_modules():

    try:
        import sys
    except(ImportError):
        raise SystemExit #exit()

    dependencies = ['shlex', 'os', 'subprocess', 'random', 
                    # 'touche turtle' # disparar bloque try
                    ]

    try:
        for dependency in dependencies:
            if dependency not in (sys.stdlib_module_names):
                raise ModuleNotFoundError(str(dependency)) # Builtin exception
    except ModuleNotFoundError as e:
        # sys,exit() cleanup actions specified by finally clauses of try statements are honored
        e_type, e_name, e_trace = sys.exc_info()
        sys.exit("Modulo %s no encontrado" % (str(e_name)))
    except AttributeError as e:
        # python exception message capturing
        sys.exit(str(e))
    else:
        # scope de variables locales en el try /except
        print("Dependencias %s presentes en el sistema" % (', '.join(dependencies)))
    finally:
        print("Dependencias de modulos chequeadas")