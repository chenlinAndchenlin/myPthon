/*
if (true) {
    // 使用let声明一个变量age 值为18
    let age = 18;
    console.log(age);
}
console.log(age);
var age=19
console.log(age)*/

//  声明了一个函数test  证明了函数作用域和块级作用域互不干扰
/*function test() {
    let age = 18; // 使用let声明了一个局部变量 age
    if (true) {
        // 使用let声明一个块变量age 值为28
        let age = 28;
        console.log(age);  // 28
    }
    console.log(age);  // 18
}

// 调用test函数
test()*/

// 报错  Cannot access 'age' before initialization
// console.log(age);
// let age = 18;
