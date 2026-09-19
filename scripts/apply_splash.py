import pathlib

idx = pathlib.Path("build/web/index.html")
html = idx.read_text()

splash_script = (
    '<style>html,body{background-color:#FFFFFF !important}</style>\n'
    '<script>\n'
    'function removeSplashFromWeb(){var s=document.getElementById("splash");'
    'if(s){s.style.opacity="0";setTimeout(function(){s.remove()},500)}}\n'
    'flet.flutterAppLoaded.then(function(){removeSplashFromWeb()});\n'
    '</script>\n'
    '</head>'
)

splash_body = (
    '<body>\n'
    '<div id="splash" style="position:fixed;top:0;left:0;width:100%;height:100%;'
    'background:#FFFFFF;display:flex;flex-direction:column;align-items:center;'
    'justify-content:center;z-index:99999;transition:opacity .5s ease">\n'
    '<img src="assets/loading.png" alt="RangoonX" style="width:min(40vw,180px);'
    'height:auto;margin-bottom:28px;animation:pulse 2s infinite ease-in-out">\n'
    '<div style="width:min(50vw,160px);height:3px;background:#E5E7EB;'
    'border-radius:3px;overflow:hidden;position:relative">\n'
    '<div style="position:absolute;height:100%;background:#3B82F6;'
    'border-radius:3px;animation:loadingBar 1.5s infinite ease-in-out"></div>\n'
    '</div>\n'
    '</div>\n'
    '<style>\n'
    '@keyframes pulse{0%{transform:scale(.96);opacity:.85}'
    '50%{transform:scale(1.04);opacity:1}100%{transform:scale(.96);opacity:.85}}\n'
    '@keyframes loadingBar{0%{left:-50%;width:30%}'
    '50%{left:25%;width:50%}100%{left:100%;width:30%}}\n'
    '</style>'
)

html = html.replace("</head>", splash_script)
html = html.replace("<body>", splash_body)
idx.write_text(html)
print("Custom splash applied to build/web/index.html")
