let dqcode=(function (){
    var url='www.baidu.com';
    var sendrequest=function(ip){
        console.log("dq向", url, "发送请求")
        console.log('ip',ip)
        console.log('port',arguments[1])
    };
    var checkstatus = function() {
        console.log("检查一下状态")
    };
    // 对象   即使是Array  也是对象
    return {"$0x142":sendrequest,
        "$0x2f2":checkstatus}

})()

//自运行实现，对比yzz.js
// let dqcode = (function () {
//     var url = 'www.baidu.com';
//     var sendrequest = function () {
//         console.log("dq向", url, "发送请求")
//
//     };
//     return sendrequest
// })()