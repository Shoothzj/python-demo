### 下载预训练文件
```bash
curl -OL https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models-zh-CN.pbmm
curl -OL https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models-zh-CN.scorer
```

### 报错
#### Sox找不到 
```
SoX not found, use 16000hz files or install it: No such file or directory
```
```
brew install sox
```