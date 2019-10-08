Adjust the `pages` variable to your required URLs.
The first parameter is the directory name.

```python
pages = [
    Page('desktop',
         'https://www.ebay-kleinanzeigen.de/s-anzeige/...'),
	 ...
]
```

After downloading you get a file structure like this:

```bash
.
├── LICENSE
├── README.md
├── desktop
│   ├── 0.jpg
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   └── desc.txt
├── dip
│   ├── 0.jpg
│   └── desc.txt
└── main.py
```
