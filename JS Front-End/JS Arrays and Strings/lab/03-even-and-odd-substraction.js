function solve(numbers) {
    let evenNumbers = 0;
    let oddNumbers = 0;
    for (let num of numbers) {
        if (num % 2 === 0) {
            evenNumbers += num;
        } else {
            oddNumbers += num
        }
    }
    console.log(evenNumbers - oddNumbers)
}

solve([3,5,7,9])
