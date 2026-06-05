def generate_fastapi(spec):

    routes = []

    for endpoint in spec["api"]["endpoints"]:

        routes.append(
            f"""
@app.get("{endpoint}")
def endpoint():
    return {{"status":"ok"}}
"""
        )

    return "\n".join(routes)