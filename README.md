# autobid-assistant 拍牌辅助

python的pyqt4小程序，

需要import和安装包如下：
  - pyqt4
  - pyautogui
  - pyscreenshot

# 工作原理

  - pyautogui 图像识别
  - pyqt4：gui，控制鼠标键盘自动操作等，类似于按键精灵
  - pyscreenshot：截图功能

简单的多线程管理，可以作为是pyqt4的exapmle



### 添加如下功能即可做到全自动化

 - 验证码url截取，识别，自动输入, 出价提交 ref: [mitmproxy ]
 - 通过memory hack获取到数据, ref: [Pymem], [hackManager]


**Free Software**

   [Pymem]: <https://pymem.readthedocs.io/foreword.html>
   [hackManager]: <https://github.com/SirFroweey/hackManager>
   [mitmproxy]: <https://mitmproxy.org/>
