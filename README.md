# pppppprint

String transformer for oddly specific stuff. Right now it's specifically tuned to my cheap thermal printer.

### input file.txt
```text
=>Right Justify
<=>Centered
[=]Banner
...- #repeating the 4th character
Space|=|Between
```

### cat "input file.txt" | python print.py
```text
                    Right Justify
            Centered
============ Banner ============
--------------------------------
Space                    Between
```

