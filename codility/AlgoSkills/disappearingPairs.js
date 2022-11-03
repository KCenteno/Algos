// first we want to try and get it to were it finds pairs that are right next to one

function solution(S){
let arr = S.split("A"||"B"||"C");
console.log(arr)
let temp = [];

    for(var i = 0; i < arr.length; i++) {
        for(var j = i + 1; j < arr.length-1; j++) {
            if(arr[i] === arr[j]) {
                temp.push(arr[i])
            }
        }
    }
    return temp;
}


solution("ABCCBA");