# AUTO-LaTex
A python tool to conver screen shot to LaTex use Mathpix OCR API (free for first 1000 query which is enough for me). 

#### Usage

```shell
git clone https://github.com/B0Qi/AUTO-LaTex.git
cd AUTO-LaTex
```

Then new a config.json file which contains your Api keys of [Mathpix API service](https://mathpix.com/ocr).

```json
{
    "app_id": "your id ",
    "app_key": "your key"
}

```



```shell
pip install -r requirements.txt
sudo python ./main.py
```

You can use the default screenshot tools in Liunx and copy the screenshot to clipboard then type  ctrl + alt + M. If  any math formulas are detected, the latex code will be aumantically copied to your clipboard. 
