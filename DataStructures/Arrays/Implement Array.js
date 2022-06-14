// Implementing Basic Array from Object
class MyArray {
    constructor() {
        this.length = 0;
        this.data = {};
    }

    get(index) {
        return this.data[index];
    }

    push(value) {
        this.data[this.length] = value;
        this.length++;
        return this.length;
    }

    pop() {
        const lastItem = this.data[this.length - 1];
        delete this.data[this.length - 1];
        this.length--;
        return lastItem;
    }

    delete(index) {
        const item = this.data[index];
        this.shiftItems(index);
        return item
    }

    shiftItems(index) {
        for (let i = index; i < this.length - 1; i++) {
            this.data[i] = this.data[i + 1];
        }
        // delete the last item in the array because we move it up already
        delete this.data[this.length - 1];
        // decrease the length of array
        this.length--;
    }

    unshift(value) {
        for (let i = 0; i < this.length; i++) {
            this.data[i] = this.data[i + 1];
        }
        this.data[0] = value;
        this.length++;
    }

}


const strings = ['a', 'b', 'c', 'd'];
const numbers = [1,2,3,4,5];


//push
strings.push('e');

//pop
strings.pop();
strings.pop();

//unshift
strings.unshift('x')

//splice
strings.splice(2, 0, 'alien');

console.log(strings)