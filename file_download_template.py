from pyodide.http import pyfetch

import pandas as pd

filename = "https://data.cityofnewyork.us/resource/8wbx-tsch.json"

async def download(url, filename):

    response = await pyfetch(url)

    if response.status == 200:

        with open(filename, "wb") as f:

            f.write(await response.bytes())

await download(filename, "nycdata.txt")

print("done")