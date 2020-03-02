let s = "abcdefghib";
let maxLen = 0;
let current = s[0];
let longest = s[0];
const things = [0, 1, 2, 3, 4, 5, 6, 7, 8];
for (let i of things) {
const next = i + 1;
// const nextChar = s[next];
// console.log(`s[next]: ${s[next]}`);
// const currentChar = s[i];
// console.log(`s[i]: ${s[i]}`);
// console.log(`${s[next]} >= ${s[i]}: ${s[next] >= s[i]}`);
if (s[next] >= s[i]) {
current += s[next];
if (current.length > maxLen) {
longest = current;
}
} else {
current = s[next];
}
}
console.log("Longest substring in alphabetical order is: " + longest);
