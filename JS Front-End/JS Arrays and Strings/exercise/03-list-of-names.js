function solve2(names) {
    names
        .sort((a, b) => a.localeCompare(b))
        .forEach((name, numberOfName) => console.log(`${numberOfName + 1}.${name}`));
}

solve2 (["John", "Bob", "Christina", "Ema"])