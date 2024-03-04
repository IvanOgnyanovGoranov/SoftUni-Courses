function operations(num1, num2, operator) {
    if ('*' === operator) {
        result = num1 * num2
        console.log(result)
    }
    else if ('/' === operator) {
        result = num1 / num2
        console.log(result) }
    else if ('+' === operator) {
        result = num1 + num2
        console.log(result)}
    else if ('-' === operator) {
        result = num1 - num2
        console.log(result)}    
    else if ('%' === operator) {
        result = num1 % num2
        console.log(result)}
    else if ('**' === operator) {
        result = num1 ** num2
        console.log(result)}
}

operations(2, 3, '*')