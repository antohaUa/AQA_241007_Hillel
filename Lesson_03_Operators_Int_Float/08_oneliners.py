import calendar

# -c option
# python -c "import secrets; print(secrets.token_hex(8))"
# python -c "import json; d1={'name': 'Tom', 'age': 25, 'city': 'New York'};print(json.dumps(d1, indent=4, sort_keys=True))
# python -c "import requests; print(requests.get(url = 'https://api.open-meteo.com/v1/forecast?latitude=50.45&longitude=30.523&current=temperature_2m').text)"


# -m option
# python -m http.server 8000  # http server
# python -m calendar 2001     # certain year calendar
# python -m timeit -s "a='text'; f'{a}'"  # timimg profiler
# python -m dis <python_file> # bytecodepython -r "import requests; print(requests.get(url = 'https://google.com').text)" dissasembler
# python -OO -m py_compile <python_file> # pyc file creation 2 stage of optimization
# python -m zipapp zip_app -c  # creation of zip files containing Python code (pyz)
