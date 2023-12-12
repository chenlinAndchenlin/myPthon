// var arr = new Array('y', 'z', 'z', 'j', 's', 'n', 'x')
// for (idx in arr) {
//     console.log(idx)
//     console.log(arr[idx]) // 从0开始  索引去值  而且 没有负索引
// }


// var arr = ['q', 'i', 'a', 'o', 'f', 'u']
// for (c of arr) {     // py里面的 for xxx in iterator:
//     console.log(c)
// }

// woshiyigehunxiaodehanshu = Array
// woshilingwaiyigehanshu = 'join'
// i = 'q'
// a = 'i'
// f = 'a'
// u = 'o'
// o = 'f'
// q = 'u'
// arr = new woshiyigehunxiaodehanshu(i, a, f, u, o, q)
// console.log('arr', arr)
// res = arr[woshilingwaiyigehanshu]('')  // <---> arr.join ('')  arr['join']('')
// console.log('res', res)

fruits=['p','e','t']
people=['yi','er','san']

var ret=fruits.map(function (item,index){
    console.log(typeof index)
    console.log(people[index])
    return people[index]+'——'+item
})
console.log(ret)
