import os

settPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "web"))
serverUrl = "http://192.168.0.108:8010"

def prepareFiles(reg=".js"):
    filesString = ""
    for root, dirs, files in os.walk(settPath):
        for file in files:
            if (file.endswith(reg)):
                with open(os.path.join(root, file), "r") as f:
                    filesString += f"\n/* {file} */\n\n{f.read()}\n"
    return filesString

with open(os.path.join(settPath, "index.html"), "r") as f:
    data = f.read()

startSCRIPTS = data.find("<!-- START SCRIPTS -->")
endSCRIPTS = data.find("<!-- END SCRIPTS -->")
data = data[:startSCRIPTS] + data[endSCRIPTS + len("<!-- END SCRIPTS -->"):]

startSTYLES = data.find("<!-- START STYLES -->")
endSTYLES = data.find("<!-- END STYLES -->")
data = data[:startSTYLES] + data[endSTYLES + len("<!-- END STYLES -->"):]

scripts = prepareFiles()
styles = prepareFiles(".css")

data = data.replace("/*$SCRIPTS$*/", scripts)
data = data.replace("/*$STYLES$*/", styles)
data = data.replace("var serverUrl = \"\";", f"var serverUrl = \"{serverUrl}\"")

with open(os.path.join(settPath, "androidWeb.html"), "w") as f:
    f.write(data)

