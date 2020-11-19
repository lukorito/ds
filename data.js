function countingValleys(n, s) {
    let data = {}
    let count = 0
    for(let i = 0; i < n; i++){
        let holder = s[i]
        data[holder]  = data[holder]  ? data[holder] + 1 : 1
    }
    if (data['U'] === data['D']){
        count++
    } else if(data['U'] > data['D']){
        count+=2
    } else if(data['U'] < data['D']) {
        count=0;
    }
    console.log(data)
    return count
}

console.log(countingValleys(8, 'DDUUDDUDUUUD'))