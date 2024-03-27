# twitter-autoChat
如何使用推特的API功能进行自动按格式发帖？

记录今天学到的方法：

1. 在Twitter开发者平台( https://developer.twitter.com)上创建一个开发者账号和应用程序。

2. 进入“项目和应用程序”页面，创建一个新的项目。

3. 在项目中创建一个新的应用程序。填写应用程序的基本信息，如应用名称、描述、网站URL等。

4. 应用创建完成后，进入应用程序的“Keys and Tokens”选项卡。

5. 在这里您可以获得以下 4 个认证凭据：API密钥（API密钥），API密钥(API密钥秘密)，访问令牌（访问令牌），访问令牌秘密（访问令牌秘密）

其中API Key和API Secret Key是应用程序级别的密钥，Access Token和Access Token Secret是用于代表用户访问Twitter API的令牌。

6. 4个参数，填充到快速开始SDK体验：

https://github.com/zgimszhd61/twitter-autoChat/blob/main/app.py
