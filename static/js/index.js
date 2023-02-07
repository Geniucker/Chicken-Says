window.onload = function() {
    var btn1 = document.getElementById("btn1");
    var btn2 = document.getElementById("btn2");
    var inp1 = document.getElementById("inp1");
    var inp2 = document.getElementById("inp2");


    btn1.onclick = function() {
        inp2.value = "鸡正在思考，请稍后..."
        var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
        httpRequest.open('POST', 'encode', true); //第二步：打开连接
        httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
        httpRequest.send("q="+inp1.value);//发送请求 将情头体写在send中
        httpRequest.onreadystatechange = function () {//请求后的回调接口，可将请求成功后要执行的程序写在其中
            if (httpRequest.status >= 200 && httpRequest.status < 400) {
                inp2.value = httpRequest.responseText;//获取到服务端返回的数据
            }
            else {
                inp2.value = "鸡想不出来qaq。可能是字太多了"
            }
        };
    }
    btn2.onclick = function() {
        inp1.value = "鸡正在思考，请稍后..."
        var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
        httpRequest.open('POST', 'decode', true); //第二步：打开连接
        httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
        httpRequest.send("q="+inp2.value);//发送请求 将情头体写在send中
        httpRequest.onreadystatechange = function () {//请求后的回调接口，可将请求成功后要执行的程序写在其中
            if (httpRequest.status >= 200 && httpRequest.status < 400) {
                inp1.value = httpRequest.responseText;//获取到服务端返回的数据
            }
            else {
                inp1.value = "鸡想不出来qaq。可能是字太多了"
            }
        };

    }
};