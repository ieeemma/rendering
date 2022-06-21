#!/bin/python

import markdown
from bs4 import BeautifulSoup
import urllib

style = """
body {
    margin: 40px auto;
    max-width: 750px;
    line-height: 1.6;
    font-size: 18px;
    color: #444;
    padding: 0 10px;
}

h1, h2, h3 {
    line-height:1.2
}

a, a:visited {
    color: #07a;
    text-decoration: none;
}

code{white-space: pre-wrap;}
span.smallcaps{font-variant: small-caps;}
span.underline{text-decoration: underline;}
div.column{display: inline-block; vertical-align: top; width: 50%;}
div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
ul.task-list{list-style: none;}
pre > code.sourceCode { white-space: pre; position: relative; }
pre > code.sourceCode > span { display: inline-block; line-height: 1.25; }
pre > code.sourceCode > span:empty { height: 1.2em; }
code.sourceCode > span { color: inherit; text-decoration: inherit; }
div.sourceCode { margin: 1em 0; }
pre.sourceCode { margin: 0; }
@media screen {
div.sourceCode { overflow: auto; }
}
@media print {
pre > code.sourceCode { white-space: pre-wrap; }
pre > code.sourceCode > span { text-indent: -5em; padding-left: 5em; }
}
pre.numberSource code
  { counter-reset: source-line 0; }
pre.numberSource code > span
  { position: relative; left: -4em; counter-increment: source-line; }
pre.numberSource code > span > a:first-child::before
  { content: counter(source-line);
position: relative; left: -1em; text-align: right; vertical-align: baseline;
border: none; display: inline-block;
-webkit-touch-callout: none; -webkit-user-select: none;
-khtml-user-select: none; -moz-user-select: none;
-ms-user-select: none; user-select: none;
padding: 0 4px; width: 4em;
color: #aaaaaa;
  }
pre.numberSource { margin-left: 3em; border-left: 1px solid #aaaaaa;  padding-left: 4px; }
div.sourceCode
  {   }
@media screen {
pre > code.sourceCode > span > a:first-child::before { text-decoration: underline; }
}
code span.al { color: #ff0000; font-weight: bold; } /* Alert */
code span.an { color: #60a0b0; font-weight: bold; font-style: italic; } /* Annotation */
code span.at { color: #7d9029; } /* Attribute */
code span.bn { color: #40a070; } /* BaseN */
code span.bu { } /* BuiltIn */
code span.cf { color: #007020; font-weight: bold; } /* ControlFlow */
code span.ch { color: #4070a0; } /* Char */
code span.cn { color: #880000; } /* Constant */
code span.co { color: #60a0b0; font-style: italic; } /* Comment */
code span.cv { color: #60a0b0; font-weight: bold; font-style: italic; } /* CommentVar */
code span.do { color: #ba2121; font-style: italic; } /* Documentation */
code span.dt { color: #902000; } /* DataType */
code span.dv { color: #40a070; } /* DecVal */
code span.er { color: #ff0000; font-weight: bold; } /* Error */
code span.ex { } /* Extension */
code span.fl { color: #40a070; } /* Float */
code span.fu { color: #06287e; } /* Function */
code span.im { } /* Import */
code span.in { color: #60a0b0; font-weight: bold; font-style: italic; } /* Information */
code span.kw { color: #007020; font-weight: bold; } /* Keyword */
code span.op { color: #666666; } /* Operator */
code span.ot { color: #007020; } /* Other */
code span.pp { color: #bc7a00; } /* Preprocessor */
code span.sc { color: #4070a0; } /* SpecialChar */
code span.ss { color: #bb6688; } /* SpecialString */
code span.st { color: #4070a0; } /* String */
code span.va { color: #19177c; } /* Variable */
code span.vs { color: #4070a0; } /* VerbatimString */
code span.wa { color: #60a0b0; font-weight: bold; font-style: italic; } /* Warning */

pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.codehilite .hll { background-color: #ffffcc }
.codehilite { background: #ffffff; }
.codehilite .c { color: #999988; font-style: italic } /* Comment */
.codehilite .err { color: #a61717; background-color: #e3d2d2 } /* Error */
.codehilite .k { color: #000000; font-weight: bold } /* Keyword */
.codehilite .o { color: #000000; font-weight: bold } /* Operator */
.codehilite .ch { color: #999988; font-style: italic } /* Comment.Hashbang */
.codehilite .cm { color: #999988; font-style: italic } /* Comment.Multiline */
.codehilite .cp { color: #999999; font-weight: bold; font-style: italic } /* Comment.Preproc */
.codehilite .cpf { color: #999988; font-style: italic } /* Comment.PreprocFile */
.codehilite .c1 { color: #999988; font-style: italic } /* Comment.Single */
.codehilite .cs { color: #999999; font-weight: bold; font-style: italic } /* Comment.Special */
.codehilite .gd { color: #000000; background-color: #ffdddd } /* Generic.Deleted */
.codehilite .ge { color: #000000; font-style: italic } /* Generic.Emph */
.codehilite .gr { color: #aa0000 } /* Generic.Error */
.codehilite .gh { color: #999999 } /* Generic.Heading */
.codehilite .gi { color: #000000; background-color: #ddffdd } /* Generic.Inserted */
.codehilite .go { color: #888888 } /* Generic.Output */
.codehilite .gp { color: #555555 } /* Generic.Prompt */
.codehilite .gs { font-weight: bold } /* Generic.Strong */
.codehilite .gu { color: #aaaaaa } /* Generic.Subheading */
.codehilite .gt { color: #aa0000 } /* Generic.Traceback */
.codehilite .kc { color: #000000; font-weight: bold } /* Keyword.Constant */
.codehilite .kd { color: #000000; font-weight: bold } /* Keyword.Declaration */
.codehilite .kn { color: #000000; font-weight: bold } /* Keyword.Namespace */
.codehilite .kp { color: #000000; font-weight: bold } /* Keyword.Pseudo */
.codehilite .kr { color: #000000; font-weight: bold } /* Keyword.Reserved */
.codehilite .kt { color: #445588; font-weight: bold } /* Keyword.Type */
.codehilite .m { color: #009999 } /* Literal.Number */
.codehilite .s { color: #dd1144 } /* Literal.String */
.codehilite .na { color: #008080 } /* Name.Attribute */
.codehilite .nb { color: #0086B3 } /* Name.Builtin */
.codehilite .nc { color: #445588; font-weight: bold } /* Name.Class */
.codehilite .no { color: #008080 } /* Name.Constant */
.codehilite .nd { color: #3c5d5d; font-weight: bold } /* Name.Decorator */
.codehilite .ni { color: #800080 } /* Name.Entity */
.codehilite .ne { color: #990000; font-weight: bold } /* Name.Exception */
.codehilite .nf { color: #990000; font-weight: bold } /* Name.Function */
.codehilite .nl { color: #990000; font-weight: bold } /* Name.Label */
.codehilite .nn { color: #555555 } /* Name.Namespace */
.codehilite .nt { color: #000080 } /* Name.Tag */
.codehilite .nv { color: #008080 } /* Name.Variable */
.codehilite .ow { color: #000000; font-weight: bold } /* Operator.Word */
.codehilite .w { color: #bbbbbb } /* Text.Whitespace */
.codehilite .mb { color: #009999 } /* Literal.Number.Bin */
.codehilite .mf { color: #009999 } /* Literal.Number.Float */
.codehilite .mh { color: #009999 } /* Literal.Number.Hex */
.codehilite .mi { color: #009999 } /* Literal.Number.Integer */
.codehilite .mo { color: #009999 } /* Literal.Number.Oct */
.codehilite .sa { color: #dd1144 } /* Literal.String.Affix */
.codehilite .sb { color: #dd1144 } /* Literal.String.Backtick */
.codehilite .sc { color: #dd1144 } /* Literal.String.Char */
.codehilite .dl { color: #dd1144 } /* Literal.String.Delimiter */
.codehilite .sd { color: #dd1144 } /* Literal.String.Doc */
.codehilite .s2 { color: #dd1144 } /* Literal.String.Double */
.codehilite .se { color: #dd1144 } /* Literal.String.Escape */
.codehilite .sh { color: #dd1144 } /* Literal.String.Heredoc */
.codehilite .si { color: #dd1144 } /* Literal.String.Interpol */
.codehilite .sx { color: #dd1144 } /* Literal.String.Other */
.codehilite .sr { color: #009926 } /* Literal.String.Regex */
.codehilite .s1 { color: #dd1144 } /* Literal.String.Single */
.codehilite .ss { color: #990073 } /* Literal.String.Symbol */
.codehilite .bp { color: #999999 } /* Name.Builtin.Pseudo */
.codehilite .fm { color: #990000; font-weight: bold } /* Name.Function.Magic */
.codehilite .vc { color: #008080 } /* Name.Variable.Class */
.codehilite .vg { color: #008080 } /* Name.Variable.Global */
.codehilite .vi { color: #008080 } /* Name.Variable.Instance */
.codehilite .vm { color: #008080 } /* Name.Variable.Magic */
.codehilite .il { color: #009999 } /* Literal.Number.Integer.Long */
"""

template = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <style>{}</style>
    <title>Light transport simulation</title>
  </head>
<body>
<h1>Table of contents</h1>
{}
<hr>
{}
</body>
"""

with open("notes.md", "r") as f:
    src = f.read()

i = 0
lines = src.split("\n")

def urlize(name):
    return urllib.parse.quote(name.replace(" ", "-").lower(), safe='')

def parse(depth):
    global i
    blocks = {}

    while i < len(lines):
        line = lines[i]

        if line.startswith("```"):
           i += 1
           while not line.startswith("```"): i += 1
           i += 1
        elif line.startswith("#"):
            title = line.lstrip("#")
            n = len(line) - len(title)
            if n <= depth:
                return blocks
            else:
                i += 1
                t = title.strip()
                blocks[(t, f"#{urlize(t)}")] = parse(n)
        else:
            i += 1

    return blocks

index = parse(0)

html = markdown.markdown(
    src,
    extensions=["codehilite", "fenced_code", "markdown_katex"],
    extension_configs={
        "codehilite": {},
        "markdown_katex": {"insert_fonts_css": False}
    }
)

soup = BeautifulSoup(html, "lxml")

for tag in soup.find_all("span", class_="katex-html"):
    tag.decompose()

for tag in soup.find_all(("h1", "h2", "h3", "h4", "h5", "h6")):
    tag.attrs["id"] = urlize(tag.text)

def gen_list(ds):
    out = []
    for (name, href), v in ds.items():
        out.append(f'<li><a href="{href}">{name}</a>{gen_list(v)}</li>')
    if out:
        return "<ul>" + "".join(out) + "</ul>"
    else:
        return ""

out = gen_list(index)

final = template.format(style, out, str(soup))

with open("build/notes.html", "w") as f:
    f.write(final)
