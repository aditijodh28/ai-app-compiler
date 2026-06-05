def validate(spec):

    errors = []

    if "contacts" not in spec["database"]["tables"]:
        errors.append("missing contacts table")

    if "/contacts" not in spec["api"]["endpoints"]:
        errors.append("missing contacts endpoint")

    return errors