## Network(proxy) related errors
With key worlds of "proxy", "ProtocolError" or "403", try:
```bash
# Usually do this before using pip/conda...
unset https_proxy
unset http_proxy
```

or

```bash
# Usually do this before using git push...
# export https_proxy=http://10.200.13.85:3128
# export http_proxy=http://10.200.13.85:3128
# 最新proxy地址
export https_proxy=proxy-dku.oit.duke.edu:3128
export http_proxy=proxy-dku.oit.duke.edu:3128
```