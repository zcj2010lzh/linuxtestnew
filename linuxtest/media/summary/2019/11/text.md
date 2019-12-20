1.注册 
在注册页面向http://47.103.205.169/api/register/发POST请求，需要带的参数account(学号),password(密码),username(用户名),group(组),email(邮箱) 若注册成功，code:1,失败code:0
2登录
在登录页面向http://47.103.205.169/api/login/发POST请求，需要带的参数account,password.若成功则返回code:1,且会返回一段token(这个token每次登录都在变，在请求周总结时作为用户标识)，失败返回code:0
3周总结
	有三种情况
		1.往 http://47.103.205.169/api/summary/?token='登录时返回的token' 发送GET请求代表从数据库拿回该用户的周总结 若成功那回，会返回一个状态码code:1,且以列表字典形式返回每篇周总结(每篇周总结包括作者,发表时间，标题，内容)
		2.往 http://47.103.205.169/api/summary/?token='登录时返回的token' 发送POST请求则应带参数title与content参数 同样，成功则返回code:1
		3.往 http://47.103.205.169/api/summary/?token='登录时返回的token' 发送DELETE请求加文章名，则会删除该周总结(此处可能会把所有这种文章名周总结删除，没写好，就是除了删除自己的，还因该会把别人的同名文章删除) 删除成功返回code:1


4.已存在帐号 201803343 密码 zhaoqian123 

5 后台 http://47.103.205.169/admin/
后台帐号 flyingdigital
密码 zhaoqian123
可以去简陋后台手动操作数据