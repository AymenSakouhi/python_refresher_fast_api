const arr = [1, 2, 3, 4, 5, 6];

const newArr = arr.slice(0, 3);
console.log(arr);
console.log(newArr);

arr.splice(2, 1);
arr.splice(2, 0, 10);
console.log(arr);

const random = arr[Math.ceil(Math.random() * arr.length - 1)];
console.log(random);
// google problem that I got from a video to solve for no reason and then I will complete the challenge to learn python
class My_Array {
  constructor(integers) {
    this.integers = integers;
  }

  insertValue(int) {
    this.integers.push(int);
    console.log(`new integers: `, this.integers);
  }

  removeValue(int) {
    const temp = this.integers;
    const index = temp.indexOf(int);
    temp.splice(index, 1);
    this.integers = temp;
    console.log(`new integers: ${this.integers} or ${temp}`);
  }

  getRandomValue() {
    const random = Math.floor(Math.random() * (this.integers.length - 1));
    return this.integers[random];
  }
}

const temp = new My_Array([1, 2, 3, 4, 5]);
temp.insertValue(6);
temp.removeValue(4);
console.log(temp.getRandomValue());
// solved this in 5 mins. the guy in the vid is just too much
