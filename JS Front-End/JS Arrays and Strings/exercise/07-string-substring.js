function solve(word, text) {
    const words = text.toLowerCase().split(' ');
    const isIncluded = words.includes(word.toLowerCase())

    if (isIncluded) {
        return word;
    }

    return `${word} not found!`;
}


console.log(solve('javascript', 'JavaScriptt is the best programming language'))