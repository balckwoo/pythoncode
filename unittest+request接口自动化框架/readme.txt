unittest+request 接口自动化框架相关说明
-COMMON
    用于存放一些封装的公共方法，例如操作excel,操作mysql等；
-CONF
    用于存放配置文件，通过调用conf模块来指定读取；
-DATA
    用于存放各种格式的测试用例数据(excel文件后缀必须为"file.xlsx"，目前封装的操作excel方法不支持xls)
-LOGS
    用于存放日志文件的模块
-REPORTS
    用于存放测试报告，目前调用的是第三方报告模块"unittestreports"
-TESTCASE
    用于存放自动化测试测试用例的模块；
-TOOLS
    用于存放一些自己封装，仅用于当前项目的工具；

-RUN.py
    unittest自动化框架的启动文件；