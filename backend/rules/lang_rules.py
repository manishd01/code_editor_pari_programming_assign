def python_rules(prefix):
    if prefix.endswith("pri"):
        return "print(\"Hello world\")"

    elif prefix.endswith("def"):
        return "def function_name():\n    pass"

    elif prefix.endswith("class"):
        return "class MyClass:\n    def __init__(self):\n        pass"

    elif prefix.endswith("if"):
        return "if condition:\n    pass"

    elif prefix.endswith("elif"):
        return "elif condition:\n    pass"

    elif prefix.endswith("else"):
        return "else:\n    pass"

    elif prefix.endswith("for"):
        return "for i in range(10):\n    print(i)"

    elif prefix.endswith("while"):
        return "while condition:\n    break"

    elif prefix.endswith("try"):
        return "try:\n    pass\nexcept Exception as e:\n    print(e)"

    elif prefix.endswith("except"):
        return "except Exception as e:\n    print(e)"

    elif prefix.endswith(":"):
        return "    "

    elif prefix.startswith("imp") or prefix.endswith("import"):
        return "import module_name"

    elif prefix.endswith("from"):
        return "from module import something"

    elif prefix.endswith("ret"):
        return "return value"

    elif prefix.endswith("lam"):
        return "lambda x: x * 2"

    elif prefix.endswith("with"):
        return "with open('file.txt') as f:\n    data = f.read()"

    elif prefix.endswith("json"):
        return "import json\njson.loads('{}')"

    elif prefix.endswith("os"):
        return "import os\nprint(os.listdir())"

    elif prefix.endswith("req"):
        return "import requests\nresponse = requests.get('https://api.example.com')"

    elif prefix.endswith("df"):
        return "import pandas as pd\ndf = pd.DataFrame()"

    elif prefix.endswith("np"):
        return "import numpy as np\narr = np.array([1, 2, 3])"

    elif prefix.endswith("plt"):
        return "import matplotlib.pyplot as plt\nplt.plot([1,2,3])\nplt.show()"

    elif prefix.endswith("init"):
        return "def __init__(self):\n    self.value = None"

    elif prefix.endswith("self"):
        return "self.attribute"

    elif prefix.endswith("main"):
        return "if __name__ == '__main__':\n    main()"

    return ""

def cpp_rules(prefix):
    if prefix.endswith("inc"):
        return "#include <iostream>"

    elif prefix.endswith("vec"):
        return "#include <vector>\nstd::vector<int> v;"

    elif prefix.endswith("mai"):
        return (
            "int main() {\n"
            "    std::cout << \"Hello\" << std::endl;\n"
            "    return 0;\n"
            "}"
        )

    elif prefix.endswith("cl"):
        return (
            "class MyClass {\n"
            "public:\n"
            "    MyClass() {}\n"
            "};"
        )

    elif prefix.endswith("for"):
        return "for (int i = 0; i < 10; i++) {\n    std::cout << i;\n}"

    elif prefix.endswith("if"):
        return "if (condition) {\n    \n}"

    elif prefix.endswith("whi"):
        return "while (condition) {\n    \n}"

    elif prefix.endswith("std"):
        return "std::cout << value << std::endl;"

    return ""

def html_rules(prefix):
    if prefix.endswith("<h1"):
        return "<h1>Your heading</h1>"

    elif prefix.endswith("<div"):
        return "<div>\n    \n</div>"

    elif prefix.endswith("<p"):
        return "<p>Your text here</p>"

    elif prefix.endswith("<ul"):
        return "<ul>\n    <li>Item</li>\n</ul>"

    elif prefix.endswith("<img"):
        return "<img src=\"image.png\" alt=\"\">" 

    elif prefix.endswith("<a"):
        return "<a href=\"#\">Link</a>"

    elif prefix.endswith("<but"):
        return "<button>Click me</button>"

    elif prefix.endswith("<in"):
        return "<input type=\"text\" placeholder=\"Enter text\">"

    elif prefix.endswith("<ht"):
        return "<html>\n<head>\n<title>Page</title>\n</head>\n<body>\n\n</body>\n</html>"

    elif prefix.endswith("<bo"):
        return "<body>\n\n</body>"

    elif prefix.endswith("<ta"):
        return "<table>\n    <tr><th>Header</th></tr>\n</table>"

    return ""

def javascript_rules(prefix):
    if prefix.endswith("con"):
        return "console.log()"

    elif prefix.endswith("fun"):
        return "function myFunction() {\n    \n}"

    elif prefix.endswith("arr"):
        return "const arr = []"

    elif prefix.endswith("obj"):
        return "const obj = {}"

    elif prefix.endswith("map"):
        return "array.map(item => item)"

    elif prefix.endswith("fil"):
        return "array.filter(item => condition)"

    elif prefix.endswith("then"):
        return ".then(response => console.log(response))"

    elif prefix.endswith("cat"):
        return "class MyClass {\n    constructor() {}\n}"

    elif prefix.endswith("imp"):
        return "import something from 'module'"

    elif prefix.endswith("exp"):
        return "export default function() {}"

    elif prefix.endswith("asy"):
        return "async function name() {\n    \n}"

    elif prefix.endswith("awa"):
        return "await fetch(url)"

    elif prefix.endswith("if"):
        return "if (condition) {\n    \n}"

    elif prefix.endswith("for"):
        return "for (let i = 0; i < 10; i++) {\n    console.log(i)\n}"

    elif prefix.endswith("whi"):
        return "while (condition) {\n    \n}"

    elif prefix.endswith("try"):
        return "try {\n    \n} catch (e) {\n    console.error(e)\n}"

    return ""
