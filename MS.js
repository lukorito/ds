function solution(ranks) {
    // write your code in JavaScript (Node.js 8.9.4)
    let firstPointer = 0;
    let secondPointer = firstPointer + 1;
    let ranksCounter = 0;
    const sortedArray = ranks.sort((a, b) => a - b)
    while (firstPointer < sortedArray.length) {
        console.log('==========')
        console.log(sortedArray[firstPointer], 'first')
        console.log(sortedArray[secondPointer], 'second')
        console.log('==========')
        if(sortedArray[firstPointer] === sortedArray[secondPointer]) {
            firstPointer+=1
        }
        if (sortedArray[firstPointer] === (sortedArray[secondPointer] + 1)){
            ranksCounter+=1
            secondPointer += 1
        }
        if(secondPointer === sortedArray.length -1){
            secondPointer+=1
            firstPointer+=1
        }
        
    }
    return ranksCounter
}

console.log(solution([3, 4, 3, 0, 2, 2, 3, 0, 0]))

}
ans = max(ans, dec);
    }
return ans;
}

};
0
Reply
Share
Report
Copyright © 2020 Leet