// function yzz(name,age){
//     console.log(arguments)
//     console.log(age)
// }
// yzz(age=18,name='yzz')

// console.log('我要开始dubug')
// setTimeout(function(){
//      debugger;
//     },3000);
//
// console.log('你看看我会不会运行');
// var a = function () {
//     console.log('我是定时器')
// };
// setInterval(a, 1000);

// 1.创建方式:
// d = new Date();
// d = new Date
// var tm = d.getTime();
// console.log(tm)
//
// //获取年份
// var year = d.getFullYear();
// console.log(year);
// //获取月份
// var month = d.getMonth() + 1;    //  国外月份从0开始
// console.log(month);
// //获取日期
// var date = d.getDate();
// console.log(date);
// //获取小时
// var hour = d.getHours();
// console.log(hour);
// //获取分钟
// var minute = d.getMinutes();
// console.log(minute);
// //获取秒
// var second = d.getSeconds();
// console.log(second);
// date = `${year}-${month}-${date} ${hour}:${minute}:${second}`;
// console.log(date);
eval(function (p, a, c, k, e, d) {
    e = function (c) {
        return (c < a ? '' : e(parseInt(c / a))) + ((c = c % a) > 35 ? String.fromCharCode(c + 29) : c.toString(36))
    };
    if (!''.replace(/^/, String)) {
        while (c--) d[e(c)] = k[c] || e(c);
        k = [function (e) {
            return d[e]
        }];
        e = function () {
            return '\\w+'
        };
        c = 1
    }
    ;
    while (c--) if (k[c]) p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]);
    return p
}('0.1(\'我爱你\')', 62, 2, 'console|log'.split('|'), 0, {}))