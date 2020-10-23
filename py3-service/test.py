#!/usr/bin/python3
# https://github.com/sciter-sdk/pysciter
import sciter

if __name__ == '__main__':
    frame = sciter.Window(ismain=True, uni_theme=True)
    frame.load_file("../common-ui/index.html")
    frame.expand()
    frame.run_app()