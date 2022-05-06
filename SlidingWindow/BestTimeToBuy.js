var maxProfit = function(prices) {
    var buy = 0;
    var sell = 1;
    var bestPro = 0;
    
    while(sell < prices.length){
        if(prices[buy] < prices[sell]){
            var profit = prices[sell] - prices[buy]
            bestPro = Math.max(bestPro, profit)
        }
        else {
            buy = sell
        }
        sell++
    }
    return bestPro;
};

console.log(maxProfit([7,1,5,3,6,4]));
console.log(maxProfit([7,6,4,3,1]));