# 🌴JAVA-NJUPT
JAVA语言程序设计基础 作业+实验

### 🌱设计理念

定时任务提醒工具

本人也是一个健忘症重度患者，加上现在的各种各样的事情，不得不拥有一个事件提醒的机制，于是萌生想法，做一个APP与微信公众号的成套提醒方案，初期想法不成熟，APP端只能做数据处理，服务端做数据加工，整体流程大致是：用户可语音/文本添加一个提醒事件，APP处理后把数据写入RDS，服务端设定一个定时触发器，每分钟触发一次，将就近的事件装载到任务调度器，任务调度器完成数据的推送，完成后将RDS过期的数据删除，监听下一次的任务


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
![](https://pcdn.wxiou.cn//20200917201314.png)<p align="center">Sever架构</p>


![](https://pcdn.wxiou.cn//20200917203139.png)<p align="center">Severless架构</p>
  

![]()<p align="center">Severless流程图</p>


### 🍉客户端架构


![](https://pcdn.wxiou.cn//20200917183029.png)<p align="center">APP架构</p>


![](https://pcdn.wxiou.cn//20200917192709.png)<p align="center">APP流程图</p>


### 数据库结构设计

* task表

|字段名|ID| year|month|day|hour|minute|text|did|
| ----- | ----- | ----- |----- |----- |----- |----- |----- |----- |
| 类型 |char|char |char|char|char|char|char|int|
|示例|483f09cafa3611ea928300163e2c040a|2020|09|17|08|15|提交作业|0|

```
CREATE TABLE tasks (
	ID VARCHAR (255) NOT NULL,
	YEAR VARCHAR (255) NOT NULL,
	MONTH VARCHAR ( 255 ) NOT NULL,
	DAY VARCHAR ( 255 ) NOT NULL,
	HOUR VARCHAR	( 255 ) NOT NULL,
	MINUTE VARCHAR ( 255 ) NOT NULL,
	text VARCHAR ( 255 ) NOT NULL,
  did INT ( 2 ) NOT NULL 
);
```



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





### 🕙开发时间线
* **2020-09** 完成架构图设计、完成服务端微信推送初始化
* **2020-10** 完成客户端界面设计和功能设计、完成数据库结构设计
* **2020-11** 完成客户端与数据库通信
* **2020-12** 完成服务端

### 🕙开发日志

* **2020-09-17** 完成服务端架构图、客户端架构图的设计 
* **2020-09-18** 完成数据库结构的设计、APP流程图设计
* **2020-09-19** 完成整体软件架构图、完成severless流程图设计
* **2020-09-19** 编写云函数代码，初始化数据库，完成后端代码编写
* **2020-09-20** 生成虚拟数据，完成后端压力测试，修复......
* **2020-09-24** 编写云函数代码，初始化云函数与微信服务器之间的通信

### 🍄开发难点
* 任务调度



### 📢说明
待我写.....



