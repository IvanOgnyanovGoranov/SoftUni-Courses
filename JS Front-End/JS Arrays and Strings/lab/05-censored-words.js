function solve(text, singleWord) {
    while (text.includes(singleWord)) {
        text = text.replace(singleWord, '*'.repeat(singleWord.length))
    }
    console.log(text)
}

solve('A small sentence with some words', 'small')