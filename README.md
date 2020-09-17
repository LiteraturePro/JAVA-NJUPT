# 🌴JAVA-NJUPT
JAVA语言程序设计基础 作业+实验

### 🌱设计理念



### 🔧技术和工具

##### **技术**
* **JAVA**
* **Python**
* **MySQL**
* **Android**
* **阅读开发文档的能力**

##### 工具
* **Tencent Severless**
* **微信公众号**
* **Android Studio**
* **Tencent Relational Database Service(RDS)**
* **百度智能云语音处理**




### 🍊服务端架构
#### SQL数据库结构设计

* task表

|字段名| year|month|day|hour|minute|text|did|
| ----- | ----- |----- |----- |----- |----- |----- |----- |
| 类型 | int |int|int|int|int|char|int|
|示例|2020|09|17|08|15|提交作业|0|

* success 日志表

| 字段名 | time |text|
| ----- | ----- | ----- |
| 类型 | char |char|
|示例|2020.09.17 18:09:45|任务添加成功|

* failure 日志表

| 字段名 | time |text|
| ----- | ----- | ----- |
| 类型 | char |char|
|示例|2020.09.17 18:09:45|语音识别不成功|


![](https://pcdn.wxiou.cn//20200917203139.png)<p align="center">Severless架构</p>

![](https://pcdn.wxiou.cn//20200917201314.png)<p align="center">Sever架构</p>

### 🍉客户端架构


![](https://pcdn.wxiou.cn//20200917183029.png)<p align="center">APP架构</p>


![](https://pcdn.wxiou.cn//20200917192709.png)<p align="center">APP流程图</p>


### 🕙开发时间线
* **2020-09** 完成架构图设计、完成服务端微信推送初始化
* **2020-10** 完成客户端功能设计和界面设计、完成数据库结构设计
* **2020-11** 完成客户端和服务端通信


### 🕙开发日志

* **2020-09-17** 完成服务端架构图、客户端架构图的设计 
* **2020-09-18** 完成数据库结构的设计、微信推送端架构设计
* **2020-09-19** 完成整体软件架构图
* **2020-09-24** 编写云函数代码，初始化云函数与微信服务器之间的通信

### 🍄开发难点
* 任务调度



### 📢说明
待我写.....



