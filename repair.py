def repair(spec, errors):

    if "missing contacts table" in errors:
        spec["database"]["tables"].append("contacts")

    if "missing contacts endpoint" in errors:
        spec["api"]["endpoints"].append("/contacts")

    return spec