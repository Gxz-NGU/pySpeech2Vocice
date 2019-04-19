### 录音转文字的识别（中文）
通过pyaudio进行录音文件的保存，即保存为wav格式，可以自己设置时间
通过科大讯飞的webAPI进行json数据的返回，以python语言来进行开发
### 运行方法
#### 1.pip install PyAudio
如果你是python 3.7版本的用户，请对应[Python3.7 无法安装pyaudio](https://blog.csdn.net/weixin_43038622/article/details/84304620)这个博客写的文章，自己手动安装一下wheel
#### 2.打开main.py文件
输入你在讯飞开放平台的appid，secret_key，语音转写服务。
#### 3.打开RecorderConfig.py文件
可设置录音时长，文件存放路径，以及文件名。文件自动保存为.wav格式，文件名后面不需要写后缀名
### 使用的是讯飞开放平台上python调用webAPI的demo
发现了一处逻辑错误：
在 文件中144行的位置：`# "filename": self.gene_params(api_upload).get("slice_id"), 讯飞平台demo的逻辑错误`   这里filename 的值不太对，需改为`"filename":sig.getNextSliceId(),`程序才可正常运行，调试了一下午。
### 放到github的目的：
1.保留一下程序
2.如果有需要用python写录音转文字识别的小伙伴可以参考
3.python功底不好，希望有人能提下pr改改结构
4.官方demo无法成功运行，还得自己调试，很消耗时间成本，放上来，希望其他人别再这上面耗成本了
### PS：官方的javaSDK没有问题可成功运行，就是webAPI的python demo有些问题