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

// Another Mock interview from google that I had personally and solved in 55 mins.

const fileLogs = `2017-02-01T20:00 OperationA Start
              2017-02-01T20:01 OperationA End
              2017-02-01T20:08 OperationB Start
              2017-02-01T20:09 OperationC Start
              2017-02-01T20:10 OperationB End
              2017-02-01T20:12 OperationC End`;

const fileLogsOperations = fileLogs.split('\n').map((e) => e.trim());
console.log(fileLogsOperations);

const arrOfCompletedLogsDurations = [];

for (var i = 0; i < fileLogsOperations.length; i++) {
  // format = "2017-02-01T20:00 OperationA Start"
  const name = fileLogsOperations[i].split(' ')[1];
  const indexOfStart = fileLogsOperations[i].includes(' Start');

  if (fileLogsOperations[i].includes(name) && indexOfStart) {
    const endIndex = fileLogsOperations.findIndex(
      (ele) => ele.includes(' End') && ele.includes(name)
    );
    console.log(endIndex);

    if (endIndex) {
      arrOfCompletedLogsDurations.push(
        new Date(fileLogsOperations[endIndex].split(' ')[0]) -
          new Date(fileLogsOperations[i].split(' ')[0])
      );
    }
  }
}

// [duration1, duration2, duration3]

const average =
  arrOfCompletedLogsDurations.reduce((acc, curr) => acc + curr, 0) /
  arrOfCompletedLogsDurations.length;

// Print average duration in "X days, Y hours, Z minutes, W seconds" format
function formatDuration(ms) {
  let totalSeconds = Math.floor(ms / 1000);
  const days = Math.floor(totalSeconds / (24 * 3600));
  totalSeconds %= 24 * 3600;
  const hours = Math.floor(totalSeconds / 3600);
  totalSeconds %= 3600;
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  return `${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds`;
}

console.log(formatDuration(average));
