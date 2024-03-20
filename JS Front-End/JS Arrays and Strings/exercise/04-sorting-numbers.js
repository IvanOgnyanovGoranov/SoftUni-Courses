function solve(listOfNumbers) {
    listOfNumbers.sort((a, b) => a - b)
    newList = []
    while (listOfNumbers.length > 0) {
        newList.push(listOfNumbers.shift())
        if (listOfNumbers.length > 0) {
            newList.push(listOfNumbers.pop())
        }
    }
    return newList
}

solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56])