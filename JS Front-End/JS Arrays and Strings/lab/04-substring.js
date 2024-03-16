function solve(string, num1, num2) {
    let newStr = string.substring(num1, num2 + num1)
    console.log(newStr)
}

solve('ASentenceToCut', 1, 8)