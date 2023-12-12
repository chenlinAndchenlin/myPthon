// var j
// console.log(j)
// var i=null
// console.log()
// string -> number  :  parseInt(字符串)
// var a = "10086";
// a = parseInt(a);  // 变成整数
// console.log(a + 10); // 10096
//
// // number -> string  : 数字.toString() 或者 数字 + ""
// var a = 100;
// var b = a.toString()+"chen";
// var c = a + ""+"chenlin";
// console.log(b);
// console.log(c);

// number -> string: 数字转化成16进制的字符串
// var m = 122;
// var n = m.toString(16);
// console.log(n);
// console.log(typeof n)
//
//
// // 进制转换
// var a = 10;
// // 16进制的数字是多少
// var x = a.toString(16);  // a
// console.log(x);
// console.log(typeof x)
// // AB的十进制是多少
// var d = parseInt("AB", 16); // 171
// console.log(d );
// console.log(typeof d)
// var c = 2;
// var x = c.toString(2);  // a
// console.log(x);
// console.log(typeof x)
// console.log(c<<2)
// var x = (c<<2).toString(2);  // a
// console.log(x);
// console.log(typeof x)
//
// var a = 0;
// console.log(a++ && a);
// console.log(a)
// var a = 0;
// console.log(++a && a);
// console.log(a)

// var b = 0;
// var c = 0;
// b++;
// ++c;
// console.log(b == c)  // js中没有 a += 1这种语法...
// var s = " I have a apple. "
// console.log(s.replace("a","A"))

var arr = [1, 2, 3, 4, 5];
var arr1 = new Array(11, 12, 13, 14, 15);

// console.log(arr.length)  // 5
// console.log(arr)
// console.log(arr.push(7))
// console.log(arr)// 6  返回数组的长度
// console.log(arr.pop())
// console.log(arr)// 7  返回数组的最后一个元素并从原数组中删除
// console.log(arr.shift()) // 1

// arr1.forEach(function (item,index) {
//         console.log(item,index)
//     })
// console.log(arr.join())
// console.log(arr.join('__'))
//     // '2,3,4,5'
//     arr.join('__')
    // '2__3__4__5'

 // function chi(a,b,c){
 //        console.log(a);
 //        console.log(b);
 //        console.log(c);
 //    }
 //
 //    chi('小明')
 //    chi("小明","小红")
 //    chi("小明","小红","小花")
 //    chi("小明","小红","小花","小李")

 function shuijiao2(a,b,c){
        var e =10
        console.log(a);
        console.log(b);
        console.log(c);
        return e++,console.log(e),e++,console.log(e),"给你们上点难度"   //  "睡觉了";"兄弟们";return "给你们上点难度"
    }
    var g=  shuijiao2("小明","小红","小花")
    console.log(g)