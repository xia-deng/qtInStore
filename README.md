# qtInStore
桌面入库系统
1.Pycharm 集成PyQt步骤：https://blog.csdn.net/jiyanglin/article/details/79952713
<1>pip install pyqt5 pip install pyqt5-tools
<2>Pycharm 中：settings->tools->external tools进行添加【配置后，可以在pycharm中tools->external tools直接调用对应的pyqt功能】
<3>设置Qt Designer
修改三个地方，其他地方默认：
Name：Qt Designer
Programs：D:\Program Files\Python35\Lib\site-packages\pyqt5-tools\designer.exe
Working directory：$ProjectFileDir$
<4>、配置PyUIC
设置四个地方，其他可以默认（我也不知道怎么改，那就默认吧）
Name：PyUIC
Programs：D:\Program Files\Python35\python.exe
Parameters：-m PyQt5.uic.pyuic  $FileName$ -o $FileNameWithoutExtension$.py
Working directory：$ProjectFileDir$
