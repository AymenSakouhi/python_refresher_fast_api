const arr = [1, 2, 3, 4, 5, 6];

const newArr = arr.slice(0, 3);
console.log(arr);
console.log(newArr);

arr.splice(2, 1);
arr.splice(2, 0, 10);
console.log(arr);

const random = arr[Math.ceil(Math.random() * arr.length - 1)];
console.log(random);
